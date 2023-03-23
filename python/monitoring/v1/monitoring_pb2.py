# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: monitoring/v1/monitoring.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as github_dot_com_dot_golang_dot_protobuf_dot_ptypes_dot_timestamp_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1emonitoring/v1/monitoring.proto\x12\x1c\x61rangodb.cloud.monitoring.v1\x1a\x16\x63ommon/v1/common.proto\x1a;github.com/golang/protobuf/ptypes/timestamp/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xcb\x01\n\x18GetDeploymentLogsRequest\x12\x15\n\rdeployment_id\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x11\n\tserver_id\x18\x04 \x01(\t\x12,\n\x08start_at\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06\x65nd_at\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05limit\x18\x66 \x01(\x05\"$\n\x13\x44\x65ploymentLogsChunk\x12\r\n\x05\x63hunk\x18\x01 \x01(\x0c\x32\xcc\x02\n\x11MonitoringService\x12{\n\rGetAPIVersion\x12\x1f.arangodb.cloud.common.v1.Empty\x1a!.arangodb.cloud.common.v1.Version\"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/monitoring/v1/api-version\x12\xb9\x01\n\x11GetDeploymentLogs\x12\x36.arangodb.cloud.monitoring.v1.GetDeploymentLogsRequest\x1a\x31.arangodb.cloud.monitoring.v1.DeploymentLogsChunk\"7\x82\xd3\xe4\x93\x02\x31\",/api/monitoring/v1/streaming/deployment-logs:\x01*0\x01\x42\x30Z.github.com/arangodb-managed/apis/monitoring/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'monitoring.v1.monitoring_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/arangodb-managed/apis/monitoring/v1'
  _MONITORINGSERVICE.methods_by_name['GetAPIVersion']._options = None
  _MONITORINGSERVICE.methods_by_name['GetAPIVersion']._serialized_options = b'\202\323\344\223\002 \022\036/api/monitoring/v1/api-version'
  _MONITORINGSERVICE.methods_by_name['GetDeploymentLogs']._options = None
  _MONITORINGSERVICE.methods_by_name['GetDeploymentLogs']._serialized_options = b'\202\323\344\223\0021\",/api/monitoring/v1/streaming/deployment-logs:\001*'
  _GETDEPLOYMENTLOGSREQUEST._serialized_start=180
  _GETDEPLOYMENTLOGSREQUEST._serialized_end=383
  _DEPLOYMENTLOGSCHUNK._serialized_start=385
  _DEPLOYMENTLOGSCHUNK._serialized_end=421
  _MONITORINGSERVICE._serialized_start=424
  _MONITORINGSERVICE._serialized_end=756
# @@protoc_insertion_point(module_scope)