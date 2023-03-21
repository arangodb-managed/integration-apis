# ArangoGraph Insights Platform API's

<img src="https://cloud.arangodb.com/assets/logos/arangograph-logo-auth.svg" alt="ArangoGraph Insights Platform" width="400"/>

This repository contains the interface definition of the API for ArangoGraph Insights Platform, formerly called Oasis.

The entire interface is specified in protocol buffers and uses GRPC underlying as protocol.
A full list of API methods and their arguments is available
[here](https://arangodb-managed.github.io/apis/).

## Maintainers

This provider plugin is maintained by the team at [ArangoDB](https://www.arangodb.com/).

## More information

More information and a getting started guide about the ArangoGraph Insights Platform API is available at [arangodb.com/docs/stable/arangograph](https://www.arangodb.com/docs/stable/arangograph/).

## Examples

The following projects make use of the ArangoGraph Insights Platform API and are good examples of how to use it:

* [oasisctl](https://github.com/arangodb-managed/oasisctl) Commandline utility for ArangoGraph Insights Platform (formerly called ArangoDB Oasis).
* [terraform-provider-oasis](https://github.com/arangodb-managed/terraform-provider-oasis) Terraform plugin for ArangoGraph Insights Platform (formerly called ArangoDB Oasis).

## Building

Building the APIs involves the compilation of the protocol buffers and the generation of a Go client for it.

*Note that it is not needed to go through this build process in order to use the API.*

The build process requires a github personal access token with the following scopes.

* repo
    * repo:status
    * repo_deployment
    * public_repo
    * repo:invite

The token must be placed in a file called `${HOME}/.arangodb/ms/github-readonly-code-acces.token`.

To compile the protobuffer specifications and build
Go wrappers for them, run:

```bash
make build-image
make
```

## Building clients for other languages

Since GRPC is available for many languages (Java, NodeJS, C#, Python...) it is fairly straightforward to create clients for these languages.

To do so, follow language specific instructions on [grpc.io](https://grpc.io/docs/reference/).

*Note that we do not support clients other than the Go client that already included in this repository.*
