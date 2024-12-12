//
// This file is AUTO-GENERATED by protoc-gen-ts.
// Do not modify it manually.
///
import api from '../../api'
import * as googleTypes from '../../googleTypes'
import { Empty as arangodb_cloud_common_v1_Empty } from '../../common/v1/common'
import { IDOptions as arangodb_cloud_common_v1_IDOptions } from '../../common/v1/common'
import { ListOptions as arangodb_cloud_common_v1_ListOptions } from '../../common/v1/common'
import { Version as arangodb_cloud_common_v1_Version } from '../../common/v1/common'

// File: platform/v1/platform.proto
// Package: arangodb.cloud.platform.v1

// Request arguments for ListProviders
export interface ListProvidersRequest {
  // Common list options
  // arangodb.cloud.common.v1.ListOptions
  options?: arangodb_cloud_common_v1_ListOptions;
  
  // If set, the result includes all providers for that are available for the
  // organization identified by this ID.
  // If not set, only providers are returned that are available to all organizations.
  // string
  organization_id?: string;
}

// Request arguments for ListRegions
export interface ListRegionsRequest {
  // Common list options
  // arangodb.cloud.common.v1.ListOptions
  options?: arangodb_cloud_common_v1_ListOptions;
  
  // Required identifier of the provider to list regions for.
  // string
  provider_id?: string;
  
  // If set, the result includes all regions for that are available for the
  // organization identified by this ID.
  // If not set, only regions are returned that are available to all organizations.
  // string
  organization_id?: string;
  
  // If set, the result includes only those regions where the specified deployment model
  // is supported.
  // This is an optional field.
  // string
  model_id?: string;
}

// Provider represents a specific cloud provider such as AWS or GCP.
export interface Provider {
  // System identifier of the provider.
  // string
  id?: string;
  
  // Name of the provider
  // string
  name?: string;
  
  // If set, this provider has not be released as generally available.
  // boolean
  prerelease?: boolean;
}

// List of providers.
export interface ProviderList {
  // Provider
  items?: Provider[];
}

// Region represents a geographical region in which deployments are run.
export interface Region {
  // System identifier of the region.
  // string
  id?: string;
  
  // Identifier of the provider that hosts this region.
  // string
  provider_id?: string;
  
  // Location of the region
  // string
  location?: string;
  
  // Is this region available for creating new deployments?
  // boolean
  available?: boolean;
  
  // If set, this region is low on stock.
  // Creating a deployment may not be possible.
  // boolean
  low_stock?: boolean;
  
  // If set, this region is out of stock.
  // Creating a deployment is currently not possible.
  // boolean
  out_of_stock?: boolean;
  
  // If set, this region has not be released as generally available.
  // boolean
  prerelease?: boolean;
  
  // If set, this region support ML services.
  // boolean
  ml_supported?: boolean;
  
  // sets the sales priority of this region higher number is higher priority
  // number
  priority?: number;
}

// List of regions.
export interface RegionList {
  // Region
  items?: Region[];
}

// PlatformService is the API used to query for cloud provider & regional info.
export interface IPlatformService {
  // Get the current API version of this service.
  // Required permissions:
  // - None
  GetAPIVersion: (req?: arangodb_cloud_common_v1_Empty) => Promise<arangodb_cloud_common_v1_Version>;
  
  // Fetch all providers that are supported by the ArangoDB cloud.
  // Required permissions:
  // - None
  ListProviders: (req: ListProvidersRequest) => Promise<ProviderList>;
  
  // Fetch a provider by its id.
  // Required permissions:
  // - None
  GetProvider: (req: arangodb_cloud_common_v1_IDOptions) => Promise<Provider>;
  
  // Fetch all regions provided by the provided identified by the given context ID.
  // If the given context identifier contains a valid organization ID,
  // the result includes all regions for that organization.
  // Otherwise only regions are returned that are available to all organizations.
  // Required permissions:
  // - None
  ListRegions: (req: ListRegionsRequest) => Promise<RegionList>;
  
  // Fetch a region by its id.
  // Required permissions:
  // - None
  GetRegion: (req: arangodb_cloud_common_v1_IDOptions) => Promise<Region>;
}

// PlatformService is the API used to query for cloud provider & regional info.
export class PlatformService implements IPlatformService {
  // Get the current API version of this service.
  // Required permissions:
  // - None
  async GetAPIVersion(req?: arangodb_cloud_common_v1_Empty): Promise<arangodb_cloud_common_v1_Version> {
    const path = `/api/platform/v1/api-version`;
    const url = path + api.queryString(req, []);
    return api.get(url, undefined);
  }
  
  // Fetch all providers that are supported by the ArangoDB cloud.
  // Required permissions:
  // - None
  async ListProviders(req: ListProvidersRequest): Promise<ProviderList> {
    const path = `/api/platform/v1/providers`;
    const url = path + api.queryString(req, []);
    return api.get(url, undefined);
  }
  
  // Fetch a provider by its id.
  // Required permissions:
  // - None
  async GetProvider(req: arangodb_cloud_common_v1_IDOptions): Promise<Provider> {
    const path = `/api/platform/v1/providers/${encodeURIComponent(req.id || '')}`;
    const url = path + api.queryString(req, [`id`]);
    return api.get(url, undefined);
  }
  
  // Fetch all regions provided by the provided identified by the given context ID.
  // If the given context identifier contains a valid organization ID,
  // the result includes all regions for that organization.
  // Otherwise only regions are returned that are available to all organizations.
  // Required permissions:
  // - None
  async ListRegions(req: ListRegionsRequest): Promise<RegionList> {
    const path = `/api/platform/v1/providers/${encodeURIComponent(req.provider_id || '')}/regions`;
    const url = path + api.queryString(req, [`provider_id`]);
    return api.get(url, undefined);
  }
  
  // Fetch a region by its id.
  // Required permissions:
  // - None
  async GetRegion(req: arangodb_cloud_common_v1_IDOptions): Promise<Region> {
    const path = `/api/platform/v1/regions/${encodeURIComponent(req.id || '')}`;
    const url = path + api.queryString(req, [`id`]);
    return api.get(url, undefined);
  }
}
