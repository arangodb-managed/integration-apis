# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ml/v1/ml.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eml/v1/ml.proto\x12\x14\x61rangodb.cloud.ml.v1\x1a\x16\x63ommon/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\"4\n\nMLServices\x12\x15\n\rdeployment_id\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x32\x87\x03\n\tMLService\x12s\n\rGetAPIVersion\x12\x1f.arangodb.cloud.common.v1.Empty\x1a!.arangodb.cloud.common.v1.Version\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/api/ml/v1/api-version\x12z\n\rGetMLServices\x12#.arangodb.cloud.common.v1.IDOptions\x1a .arangodb.cloud.ml.v1.MLServices\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/ml/v1/mlservices/{id}\x12\x88\x01\n\x10UpdateMLServices\x12 .arangodb.cloud.ml.v1.MLServices\x1a .arangodb.cloud.ml.v1.MLServices\"0\x82\xd3\xe4\x93\x02*\x1a%/api/ml/v1/mlservices/{deployment_id}:\x01*B(Z&github.com/arangodb-managed/apis/ml/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ml.v1.ml_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/arangodb-managed/apis/ml/v1'
  _MLSERVICE.methods_by_name['GetAPIVersion']._options = None
  _MLSERVICE.methods_by_name['GetAPIVersion']._serialized_options = b'\202\323\344\223\002\030\022\026/api/ml/v1/api-version'
  _MLSERVICE.methods_by_name['GetMLServices']._options = None
  _MLSERVICE.methods_by_name['GetMLServices']._serialized_options = b'\202\323\344\223\002\034\022\032/api/ml/v1/mlservices/{id}'
  _MLSERVICE.methods_by_name['UpdateMLServices']._options = None
  _MLSERVICE.methods_by_name['UpdateMLServices']._serialized_options = b'\202\323\344\223\002*\032%/api/ml/v1/mlservices/{deployment_id}:\001*'
  _MLSERVICES._serialized_start=94
  _MLSERVICES._serialized_end=146
  _MLSERVICE._serialized_start=149
  _MLSERVICE._serialized_end=540
# @@protoc_insertion_point(module_scope)
