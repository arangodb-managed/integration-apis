# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1/annotations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61pi/v1/annotations.proto\x12\x15\x61rangodb.cloud.api.v1\x1a google/protobuf/descriptor.proto\"3\n\rMethodProfile\x12\x0f\n\x07timeout\x18\x01 \x01(\r\x12\x11\n\tretryable\x18\x02 \x01(\x08\"!\n\x0eServiceProfile\x12\x0f\n\x07timeout\x18\x01 \x01(\r:X\n\x07profile\x12\x1e.google.protobuf.MethodOptions\x18\xc6\x91\xf7# \x01(\x0b\x32$.arangodb.cloud.api.v1.MethodProfile:b\n\x0f\x64\x65\x66\x61ult_profile\x12\x1f.google.protobuf.ServiceOptions\x18\xc7\x91\xf7# \x01(\x0b\x32%.arangodb.cloud.api.v1.ServiceProfileB)Z\'github.com/arangodb-managed/apis/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1.annotations_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(profile)
  google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(default_profile)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'github.com/arangodb-managed/apis/api/v1'
  _globals['_METHODPROFILE']._serialized_start=85
  _globals['_METHODPROFILE']._serialized_end=136
  _globals['_SERVICEPROFILE']._serialized_start=138
  _globals['_SERVICEPROFILE']._serialized_end=171
# @@protoc_insertion_point(module_scope)
