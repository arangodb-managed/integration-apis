//
// DISCLAIMER
//
// Copyright 2020 ArangoDB GmbH, Cologne, Germany
//
// Author Gergely Brautigam
//

package v1

const (
	// Installation states

	// ExampleInstallationStatusInProgress means that the pod was created successfull and the data is being generated / imported
	ExampleInstallationStatusInProgress = "InProgress"
	// ExampleInstallationStatusCreating means that the database name has been created.
	ExampleInstallationStatusCreating = "Creating"
	// ExampleInstallationStatusCreated means that the database has been successfully created.
	ExampleInstallationStatusCreated = "Created"
	// ExampleInstallationStatusReady means that the data is ready to be used.
	ExampleInstallationStatusReady = "Ready"
	// ExampleInstallationStatusFailed denotes a dataset which has failed to be created.
	ExampleInstallationStatusFailed = "Failed"
	// ExampleInstallationStatusDeleted denotes a dataset of which the database has been deleted.
	ExampleInstallationStatusDeleted = "Deleted"
)
