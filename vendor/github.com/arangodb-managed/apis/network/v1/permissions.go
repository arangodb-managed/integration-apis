//
// DISCLAIMER
//
// Copyright 2021 ArangoDB GmbH, Cologne, Germany
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
// Author Robert Stam
//

package v1

const (
	// PrivateEndpointService permissions

	// PermissionPrivateEndpointServiceGetFeature is needed for getting whether or not the private endpoint service feature is enabled and available for a specific deployment.
	PermissionPrivateEndpointServiceGetFeature = "network.privateendpointservice.get-feature"
	// PermissionPrivateEndpointServiceGet is needed for getting an individual private endpoint service
	PermissionPrivateEndpointServiceGet = "network.privateendpointservice.get"
	// PermissionPrivateEndpointServiceGetByDeploymentID is getting an individual private endpoint service by deployment ID
	PermissionPrivateEndpointServiceGetByDeploymentID = "network.privateendpointservice.get-by-deployment-id"
	// PermissionPrivateEndpointServiceCreate is needed for creating a private endpoint service
	PermissionPrivateEndpointServiceCreate = "network.privateendpointservice.create"
	// PermissionPrivateEndpointServiceUpdate is needed to update the private endpoint service
	PermissionPrivateEndpointServiceUpdate = "network.privateendpointservice.update"
)
