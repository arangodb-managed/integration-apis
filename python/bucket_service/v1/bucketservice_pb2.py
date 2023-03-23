# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bucket-service/v1/bucketservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from common.v1 import icommon_pb2 as common_dot_v1_dot_icommon__pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as github_dot_com_dot_golang_dot_protobuf_dot_ptypes_dot_timestamp_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bucket-service/v1/bucketservice.proto\x12+arangodb.cloud.integration.bucketservice.v1\x1a\x16\x63ommon/v1/common.proto\x1a\x17\x63ommon/v1/icommon.proto\x1a;github.com/golang/protobuf/ptypes/timestamp/timestamp.proto\"Q\n\rBucketRequest\x12@\n\x04tags\x18\n \x03(\x0b\x32\x32.arangodb.cloud.integration.common.v1.KeyValuePair\"\x1b\n\x0bPathRequest\x12\x0c\n\x04path\x18\x03 \x01(\t\"1\n\rRepositoryURL\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0b\x62ucket_path\x18\x02 \x01(\t\"U\n\x08PathSize\x12\x15\n\rsize_in_bytes\x18\x01 \x01(\x04\x12\x17\n\x0fnumber_of_files\x18\x02 \x01(\r\x12\x19\n\x11number_of_folders\x18\x03 \x01(\r\"k\n\nObjectInfo\x12\x11\n\tis_locked\x18\x01 \x01(\x08\x12\x15\n\rsize_in_bytes\x18\x02 \x01(\x04\x12\x33\n\x0flast_updated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\" \n\x0fReadObjectChunk\x12\r\n\x05\x63hunk\x18\x01 \x01(\x0c\"{\n\x10WriteObjectChunk\x12\x46\n\x04path\x18\x01 \x01(\x0b\x32\x38.arangodb.cloud.integration.bucketservice.v1.PathRequest\x12\r\n\x05\x63hunk\x18\x02 \x01(\x0c\x12\x10\n\x08has_more\x18\x03 \x01(\x08\"H\n\x12WriteObjectControl\x12\x19\n\x11\x61llow_more_output\x18\x01 \x01(\x08\x12\x17\n\x0fmax_chunk_bytes\x18\x02 \x01(\x05\x32\xc3\t\n\rBucketService\x12S\n\rGetAPIVersion\x12\x1f.arangodb.cloud.common.v1.Empty\x1a!.arangodb.cloud.common.v1.Version\x12m\n\x0c\x42ucketExists\x12:.arangodb.cloud.integration.bucketservice.v1.BucketRequest\x1a!.arangodb.cloud.common.v1.YesOrNo\x12k\n\x0c\x43reateBucket\x12:.arangodb.cloud.integration.bucketservice.v1.BucketRequest\x1a\x1f.arangodb.cloud.common.v1.Empty\x12k\n\x0c\x44\x65leteBucket\x12:.arangodb.cloud.integration.bucketservice.v1.BucketRequest\x1a\x1f.arangodb.cloud.common.v1.Empty\x12\x88\x01\n\x10GetRepositoryURL\x12\x38.arangodb.cloud.integration.bucketservice.v1.PathRequest\x1a:.arangodb.cloud.integration.bucketservice.v1.RepositoryURL\x12g\n\nDeletePath\x12\x38.arangodb.cloud.integration.bucketservice.v1.PathRequest\x1a\x1f.arangodb.cloud.common.v1.Empty\x12~\n\x0bGetPathSize\x12\x38.arangodb.cloud.integration.bucketservice.v1.PathRequest\x1a\x35.arangodb.cloud.integration.bucketservice.v1.PathSize\x12\x86\x01\n\nReadObject\x12\x38.arangodb.cloud.integration.bucketservice.v1.PathRequest\x1a<.arangodb.cloud.integration.bucketservice.v1.ReadObjectChunk0\x01\x12\x91\x01\n\x0bWriteObject\x12=.arangodb.cloud.integration.bucketservice.v1.WriteObjectChunk\x1a?.arangodb.cloud.integration.bucketservice.v1.WriteObjectControl(\x01\x30\x01\x12\x82\x01\n\rGetObjectInfo\x12\x38.arangodb.cloud.integration.bucketservice.v1.PathRequest\x1a\x37.arangodb.cloud.integration.bucketservice.v1.ObjectInfoB@Z>github.com/arangodb-managed/integration-apis/bucket-service/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bucket_service.v1.bucketservice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z>github.com/arangodb-managed/integration-apis/bucket-service/v1'
  _BUCKETREQUEST._serialized_start=196
  _BUCKETREQUEST._serialized_end=277
  _PATHREQUEST._serialized_start=279
  _PATHREQUEST._serialized_end=306
  _REPOSITORYURL._serialized_start=308
  _REPOSITORYURL._serialized_end=357
  _PATHSIZE._serialized_start=359
  _PATHSIZE._serialized_end=444
  _OBJECTINFO._serialized_start=446
  _OBJECTINFO._serialized_end=553
  _READOBJECTCHUNK._serialized_start=555
  _READOBJECTCHUNK._serialized_end=587
  _WRITEOBJECTCHUNK._serialized_start=589
  _WRITEOBJECTCHUNK._serialized_end=712
  _WRITEOBJECTCONTROL._serialized_start=714
  _WRITEOBJECTCONTROL._serialized_end=786
  _BUCKETSERVICE._serialized_start=789
  _BUCKETSERVICE._serialized_end=2008
# @@protoc_insertion_point(module_scope)