//
// DISCLAIMER
//
// Copyright 2020 ArangoDB GmbH, Cologne, Germany
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Copyright holder is ArangoDB GmbH, Cologne, Germany
//
// Author Gergely Brautigam
//

package v1

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestExampleDatasetURL(t *testing.T) {
	assert.Equal(t, "/Organization/123/ExampleDataset/p1", ExampleDatasetURL("123", "p1"))
	assert.Equal(t, "/Organization/123%2F567/ExampleDataset/ab", ExampleDatasetURL("123/567", "ab"))
	assert.Equal(t, "/Organization/123%2F567/ExampleDataset/a%25b", ExampleDatasetURL("123/567", "a%b"))
}

func TestExampleDatasetInstallationURL(t *testing.T) {
	assert.Equal(t, "/Organization/123/Project/p1/Deployment/c1/ExampleDatasetInstallation/b1", ExampleDatasetInstallationURL("123", "p1", "c1", "b1"))
	assert.Equal(t, "/Organization/123%2F567/Project/ab/Deployment/c2%2F3/ExampleDatasetInstallation/b%2F1", ExampleDatasetInstallationURL("123/567", "ab", "c2/3", "b/1"))
	assert.Equal(t, "/Organization/123%2F567/Project/a%25b/Deployment/e%25f/ExampleDatasetInstallation/b%251", ExampleDatasetInstallationURL("123/567", "a%b", "e%f", "b%1"))
}
