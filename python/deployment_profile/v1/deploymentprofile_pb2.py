# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: deployment-profile/v1/deploymentprofile.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'deployment-profile/v1/deploymentprofile.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-deployment-profile/v1/deploymentprofile.proto\x12#arangodb.cloud.deploymentprofile.v1\x1a\x16\x63ommon/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x98\x01\n\x11\x44\x65ploymentProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x17\n\x0forganization_id\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"p\n\x1dListDeploymentProfilesRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x36\n\x07options\x18\x03 \x01(\x0b\x32%.arangodb.cloud.common.v1.ListOptions\"^\n\x15\x44\x65ploymentProfileList\x12\x45\n\x05items\x18\x01 \x03(\x0b\x32\x36.arangodb.cloud.deploymentprofile.v1.DeploymentProfile2\xf3\x02\n\x18\x44\x65ploymentProfileService\x12\x82\x01\n\rGetAPIVersion\x12\x1f.arangodb.cloud.common.v1.Empty\x1a!.arangodb.cloud.common.v1.Version\"-\x82\xd3\xe4\x93\x02\'\x12%/api/deploymentprofile/v1/api-version\x12\xd1\x01\n\x16ListDeploymentProfiles\x12\x42.arangodb.cloud.deploymentprofile.v1.ListDeploymentProfilesRequest\x1a:.arangodb.cloud.deploymentprofile.v1.DeploymentProfileList\"7\x82\xd3\xe4\x93\x02\x31\",/api/deploymentprofile/v1/deploymentprofiles:\x01*B8Z6github.com/arangodb-managed/apis/deployment-profile/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'deployment_profile.v1.deploymentprofile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/arangodb-managed/apis/deployment-profile/v1'
  _globals['_DEPLOYMENTPROFILESERVICE'].methods_by_name['GetAPIVersion']._loaded_options = None
  _globals['_DEPLOYMENTPROFILESERVICE'].methods_by_name['GetAPIVersion']._serialized_options = b'\202\323\344\223\002\'\022%/api/deploymentprofile/v1/api-version'
  _globals['_DEPLOYMENTPROFILESERVICE'].methods_by_name['ListDeploymentProfiles']._loaded_options = None
  _globals['_DEPLOYMENTPROFILESERVICE'].methods_by_name['ListDeploymentProfiles']._serialized_options = b'\202\323\344\223\0021\",/api/deploymentprofile/v1/deploymentprofiles:\001*'
  _globals['_DEPLOYMENTPROFILE']._serialized_start=174
  _globals['_DEPLOYMENTPROFILE']._serialized_end=326
  _globals['_LISTDEPLOYMENTPROFILESREQUEST']._serialized_start=328
  _globals['_LISTDEPLOYMENTPROFILESREQUEST']._serialized_end=440
  _globals['_DEPLOYMENTPROFILELIST']._serialized_start=442
  _globals['_DEPLOYMENTPROFILELIST']._serialized_end=536
  _globals['_DEPLOYMENTPROFILESERVICE']._serialized_start=539
  _globals['_DEPLOYMENTPROFILESERVICE']._serialized_end=910
# @@protoc_insertion_point(module_scope)
