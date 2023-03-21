//
// DISCLAIMER
//
// Copyright 2023 ArangoDB GmbH, Cologne, Germany
//
// THIS FILE IS GENERATED AUTOMATICALLY
//

package v1

import (
	icommon "github.com/arangodb-managed/internal-apis/common/v1"
)

var ServiceProfileBucketService = icommon.ServiceProfile{
	Name:  "BucketService",
	Route: "/arangodb.cloud.integration.bucketservice.v1.BucketService",
	Methods: []*icommon.MethodProfile{
		{
			Name:            "GetAPIVersion",
			Timeout:         30,
			Retryable:       true,
			StreamsRequests: false,
			StreamsReturns:  false,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "BucketExists",
			Timeout:         30,
			Retryable:       false,
			StreamsRequests: false,
			StreamsReturns:  false,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "CreateBucket",
			Timeout:         30,
			Retryable:       false,
			StreamsRequests: false,
			StreamsReturns:  false,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "DeleteBucket",
			Timeout:         30,
			Retryable:       false,
			StreamsRequests: false,
			StreamsReturns:  false,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "GetRepositoryURL",
			Timeout:         30,
			Retryable:       true,
			StreamsRequests: false,
			StreamsReturns:  false,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "DeletePath",
			Timeout:         30,
			Retryable:       false,
			StreamsRequests: false,
			StreamsReturns:  false,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "GetPathSize",
			Timeout:         30,
			Retryable:       true,
			StreamsRequests: false,
			StreamsReturns:  false,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "ReadObject",
			Timeout:         14400,
			Retryable:       false,
			StreamsRequests: false,
			StreamsReturns:  true,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "WriteObject",
			Timeout:         14400,
			Retryable:       false,
			StreamsRequests: true,
			StreamsReturns:  true,
			HttpRoutes:      []*icommon.HttpRoute{},
		}, {
			Name:            "GetObjectInfo",
			Timeout:         30,
			Retryable:       true,
			StreamsRequests: false,
			StreamsReturns:  false,
			HttpRoutes:      []*icommon.HttpRoute{},
		},
	},
}
