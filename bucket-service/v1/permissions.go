//
// DISCLAIMER
//
// Copyright 2023 ArangoDB GmbH, Cologne, Germany
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

package v1

const (
	// BucketService Bucket permissions

	// PermissionBucketServiceBucketExists is needed to checks if the specified bucket exists
	PermissionBucketServiceBucketExists = "bucketservice.bucket.exists"
	// PermissionBucketServiceBucketCreate is needed to create a bucket
	PermissionBucketServiceBucketCreate = "bucketservice.bucket.create"
	// PermissionBucketServiceBucketDelete is needed to delete a bucket
	PermissionBucketServiceBucketDelete = "bucketservice.bucket.delete"
)

const (
	// BucketService BucketPath permissions

	// PermissionBucketServiceBackupPathGetRepositoryURL is needed to get the URL needed to store/delete objects in a bucket
	PermissionBucketServiceBackupPathGetRepositoryURL = "bucketservice.backuppath.get-repository-url"
	// PermissionBucketServiceBucketPathDelete is needed to delete the specified path (recursively) from the provided bucket
	PermissionBucketServiceBucketPathDelete = "bucketservice.bucketpath.delete"
	// PermissionBucketServiceBucketPathGetSize is needed to get the size of a certain path in a bucket
	PermissionBucketServiceBucketPathGetSize = "bucketservice.bucketpath.get-size"
)

const (
	// BucketService BucketObject permissions

	// PermissionBucketServiceBucketObjectRead is needed to read an object from a bucket
	PermissionBucketServiceBucketObjectRead = "bucketservice.bucketobject.read"
	// PermissionBucketServiceBucketObjectWrite is needed to write an object in a bucket
	PermissionBucketServiceBucketObjectWrite = "bucketservice.bucketobject.write"
	// PermissionBucketServiceBucketObjectGetInfo is needed to get the information of an object in a bucket
	PermissionBucketServiceBucketObjectGetInfo = "bucketservice.bucketobject.get-info"
)
