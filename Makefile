SHELL = bash
SCRIPTDIR := $(shell pwd)
ROOTDIR := $(shell cd $(SCRIPTDIR) && pwd)
INTPROTOSOURCES := $(shell find . -name '*.proto' -not -path './vendor/*' -not -path './vendor-proto/*' -not -path './bin/protobuf/*' -not -path './bin/generated-protobuf/*' -not -path './bin/include/*')
PUBPROTOSOURCES := $(shell find vendor-proto/ -name '*.proto' -not -path './bin/include/*' -not -path 'vendor-proto/vendor-proto/*')
TARGETINTPROTOSOURCES := $(INTPROTOSOURCES:%=bin/protobuf/%)
TARGETPUBPROTOSOURCES := $(PUBPROTOSOURCES:vendor-proto/%=bin/protobuf/%)
BUILDIMAGE := arangodboasis/golang-ci:latest
CACHEVOL := arangodb-cloud-integration-apis-gocache
MODVOL := arangodb-cloud-integration-apis-pkg-mod
HOMEVOL := arangodb-cloud-integration-apis-home

ifndef CIRCLECI
	GITHUB_TOKEN := $(shell cat $(HOME)/.arangodb/ms/github-readonly-code-acces.token)
else
	GITHUB_TOKEN :=
endif

DOCKERARGS := run -t --rm \
	-u $(shell id -u):$(shell id -g) \
	-v $(ROOTDIR):/usr/src \
	-v $(CACHEVOL):/usr/gocache \
	-v $(MODVOL):/go/pkg/mod \
	-v $(HOMEVOL):/home/gopher \
	-e GOCACHE=/usr/gocache \
	-e GOMODCACHE=/go/pkg/mod \
	-e GOSUMDB=off \
	-e CGO_ENABLED=0 \
	-e HOME=/home/gopher \
	-w /usr/src \
	$(BUILDIMAGE)


ifndef CIRCLECI
	DOCKERENV := docker $(DOCKERARGS)
else
	DOCKERENV :=
endif

.PHONY: all
all: generate build check ts python docs

.PHONY: pull-build-image
pull-build-image: 
ifndef CIRCLECI
ifndef OFFLINE
	@docker pull $(BUILDIMAGE)
endif
endif

.PHONY: $(CACHEVOL)
$(CACHEVOL): pull-build-image Makefile
ifndef CIRCLECI
	@docker volume create $(CACHEVOL)
	@docker run -it --rm -v $(CACHEVOL):/usr/gocache \
		$(BUILDIMAGE) \
		sudo chown -R $(shell id -u):$(shell id -g) /usr/gocache
endif

.PHONY: $(MODVOL)
$(MODVOL): pull-build-image Makefile
ifndef CIRCLECI
	@docker volume create $(MODVOL)
	@docker run -it --rm -v $(MODVOL):/go/pkg/mod \
		$(BUILDIMAGE) \
		sudo chown -R $(shell id -u):$(shell id -g) /go/pkg/mod
endif

.PHONY: $(HOMEVOL)
$(HOMEVOL): pull-build-image Makefile
ifndef CIRCLECI
	@docker volume create $(HOMEVOL)
	@docker run -it 	--rm -v $(HOMEVOL):/home/gopher \
		-e GITHUB_TOKEN=$(GITHUB_TOKEN) \
		-e HOME=/home/gopher \
		$(BUILDIMAGE) \
		sudo chown -R $(shell id -u):$(shell id -g) /home/gopher
	@docker run -it --rm -v $(HOMEVOL):/home/gopher \
		-u $(shell id -u):$(shell id -g) \
		-e GITHUB_TOKEN=$(GITHUB_TOKEN) \
		-e HOME=/home/gopher \
		$(BUILDIMAGE) \
		configure-git
endif

# Generate go code for proto files
.PHONY: generate
generate: $(CACHEVOL) $(MODVOL) $(HOMEVOL)
	$(DOCKERENV) \
		go generate ./...

# Build go code 
.PHONY: build
build: generate
	cat go.mod
	go build ./...

# Check go code 
.PHONY: check
check: 
	zutano go check ./...

# Generate API docs
.PHONY: docs
docs: $(CACHEVOL) $(MODVOL) $(HOMEVOL)
	$(DOCKERENV) \
		protoc -I.:vendor-proto:vendor-proto/vendor-proto/ \
			--doc_out=docs $(INTPROTOSOURCES) \
			--doc_opt=html,index-raw.html
	cat docs/header.txt docs/index-raw.html > docs/index.html
	rm docs/index-raw.html

bin/protobuf/%: vendor-proto/%
	@mkdir -p $(shell dirname $@)
	@cp -af $< $@

bin/protobuf/%: %
	@mkdir -p $(shell dirname $@)
	@cp -af $< $@

TSPROTOSOURCES := $(TARGETINTPROTOSOURCES) $(TARGETPUBPROTOSOURCES)
LOCTSPROTOSOURCES := $(TSPROTOSOURCES:bin/protobuf/%=%)

# Generate API as typescript
.PHONY: ts
ts: $(PROTOC) $(TARGETINTPROTOSOURCES) $(TARGETPUBPROTOSOURCES)
	@rm -Rf typescript
	@mkdir -p typescript
	$(DOCKERENV) \
		sh -c "cd bin/protobuf ; protoc -I.:../../vendor-proto:../../vendor-proto/vendor-proto/ --ts_out=../../typescript $(LOCTSPROTOSOURCES) --ts_opt=. "


PYPROTOSOURCES := $(TARGETINTPROTOSOURCES) $(TARGETPUBPROTOSOURCES)
LOCPYPROTOSOURCES := $(PYPROTOSOURCES:bin/protobuf/%=%)

# Generate API as python 
.PHONY: python
python: $(PROTOC) $(TARGETINTPROTOSOURCES) $(TARGETPUBPROTOSOURCES)
	@rm -Rf python
	@mkdir -p python
	$(DOCKERENV) \
		sh -c "cd bin/protobuf ; pip3 install --user grpcio-tools ; python3 -m grpc_tools.protoc -I.:../../vendor-proto:../../vendor-proto/vendor-proto/ --python_out=../../python --pyi_out=../../python --grpc_python_out=../../python $(LOCPYPROTOSOURCES)"

.PHONY: test
test:
	mkdir -p bin/test
	go test -coverprofile=bin/test/coverage.out -v ./... | tee bin/test/test-output.txt ; exit "$${PIPESTATUS[0]}"
	cat bin/test/test-output.txt | go-junit-report > bin/test/unit-tests.xml
	go tool cover -html=bin/test/coverage.out -o bin/test/coverage.html

APISVERSION := $(shell zutano go mod latest github.com/arangodb-managed/apis | awk -F '@' '{ print $$2 }')
.PHONY: update-modules
update-modules:
	zutano update-check --quiet --fail
	test -f go.mod || go mod init
	go mod edit \
		$(shell zutano go mod replacements)
	go get \
		github.com/arangodb-managed/apis@$(APISVERSION)
	go mod tidy -v
	go mod download

	# manually clone the apis repo for .proto files
	rm -Rf vendor-proto
	git clone --branch $(APISVERSION) git@github.com:arangodb-managed/apis.git vendor-proto
	rm -Rf vendor-proto/vendor
	find vendor-proto/ -type f ! -name "*.proto" -delete
	find vendor-proto/ -type d -empty -delete

bootstrap:
	go get github.com/arangodb-managed/zutano
	go get github.com/jstemmer/go-junit-report
	go get github.com/stretchr/testify

check-version:
	zutano check api branch
