# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: crypto/v1/crypto.proto
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
    'crypto/v1/crypto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63rypto/v1/crypto.proto\x12\x18\x61rangodb.cloud.crypto.v1\x1a\x16\x63ommon/v1/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xf0\x03\n\rCACertificate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\nproject_id\x18\x05 \x01(\t\x12+\n\x08lifetime\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpires_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0f\x63\x65rtificate_pem\x18\n \x01(\t\x12\x12\n\nis_deleted\x18\x0b \x01(\x08\x12\x12\n\nis_expired\x18\x0c \x01(\x08\x12\x18\n\x10will_expire_soon\x18\r \x01(\x08\x12\x12\n\nis_default\x18\x0e \x01(\x08\x12\"\n\x1ause_well_known_certificate\x18\x0f \x01(\x08\x12\x0e\n\x06locked\x18\x10 \x01(\x08\x12\x17\n\x0frotation_needed\x18\x11 \x01(\x08\x12\x16\n\x0e\x63loned_from_id\x18\x12 \x01(\t\"K\n\x11\x43\x41\x43\x65rtificateList\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.arangodb.cloud.crypto.v1.CACertificate\"\x7f\n\x19ListCACertificatesRequest\x12\x36\n\x07options\x18\x01 \x01(\x0b\x32%.arangodb.cloud.common.v1.ListOptions\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x16\n\x0e\x63loned_from_id\x18\n \x01(\t\"\xd2\x01\n\x19\x43\x41\x43\x65rtificateInstructions\x12[\n\tplatforms\x18\x01 \x03(\x0b\x32H.arangodb.cloud.crypto.v1.CACertificateInstructions.PlatformInstructions\x1aX\n\x14PlatformInstructions\x12\x10\n\x08platform\x18\x01 \x01(\t\x12\x15\n\rinstall_steps\x18\x02 \x03(\t\x12\x17\n\x0funinstall_steps\x18\x03 \x03(\t2\xcd\x0c\n\rCryptoService\x12w\n\rGetAPIVersion\x12\x1f.arangodb.cloud.common.v1.Empty\x1a!.arangodb.cloud.common.v1.Version\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/crypto/v1/api-version\x12\xa5\x01\n\x12ListCACertificates\x12%.arangodb.cloud.common.v1.ListOptions\x1a+.arangodb.cloud.crypto.v1.CACertificateList\";\x82\xd3\xe4\x93\x02\x35\x12\x33/api/crypto/v1/projects/{context_id}/cacertificates\x12\xc5\x01\n\x1cListCACertificatesWithFilter\x12\x33.arangodb.cloud.crypto.v1.ListCACertificatesRequest\x1a+.arangodb.cloud.crypto.v1.CACertificateList\"C\x82\xd3\xe4\x93\x02=\"8/api/crypto/v1/projects/{project_id}/cacertificates/list:\x01*\x12\x8c\x01\n\x10GetCACertificate\x12#.arangodb.cloud.common.v1.IDOptions\x1a\'.arangodb.cloud.crypto.v1.CACertificate\"*\x82\xd3\xe4\x93\x02$\x12\"/api/crypto/v1/cacertificates/{id}\x12\xb1\x01\n\x1cGetCACertificateInstructions\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x33.arangodb.cloud.crypto.v1.CACertificateInstructions\"7\x82\xd3\xe4\x93\x02\x31\x12//api/crypto/v1/cacertificates/{id}/instructions\x12\xa7\x01\n\x13\x43reateCACertificate\x12\'.arangodb.cloud.crypto.v1.CACertificate\x1a\'.arangodb.cloud.crypto.v1.CACertificate\">\x82\xd3\xe4\x93\x02\x38\"3/api/crypto/v1/projects/{project_id}/cacertificates:\x01*\x12\x94\x01\n\x12\x43loneCACertificate\x12#.arangodb.cloud.common.v1.IDOptions\x1a\'.arangodb.cloud.crypto.v1.CACertificate\"0\x82\xd3\xe4\x93\x02*\"(/api/crypto/v1/cacertificates/{id}/clone\x12\x96\x01\n\x13UpdateCACertificate\x12\'.arangodb.cloud.crypto.v1.CACertificate\x1a\'.arangodb.cloud.crypto.v1.CACertificate\"-\x82\xd3\xe4\x93\x02\'2\"/api/crypto/v1/cacertificates/{id}:\x01*\x12\x87\x01\n\x13\x44\x65leteCACertificate\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x1f.arangodb.cloud.common.v1.Empty\"*\x82\xd3\xe4\x93\x02$*\"/api/crypto/v1/cacertificates/{id}\x12\xab\x01\n\x17SetDefaultCACertificate\x12\'.arangodb.cloud.crypto.v1.CACertificate\x1a\x1f.arangodb.cloud.common.v1.Empty\"F\x82\xd3\xe4\x93\x02@\";/api/crypto/v1/projects/{project_id}/cacertificates/default:\x01*B,Z*github.com/arangodb-managed/apis/crypto/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crypto.v1.crypto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z*github.com/arangodb-managed/apis/crypto/v1'
  _globals['_CRYPTOSERVICE'].methods_by_name['GetAPIVersion']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['GetAPIVersion']._serialized_options = b'\202\323\344\223\002\034\022\032/api/crypto/v1/api-version'
  _globals['_CRYPTOSERVICE'].methods_by_name['ListCACertificates']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['ListCACertificates']._serialized_options = b'\202\323\344\223\0025\0223/api/crypto/v1/projects/{context_id}/cacertificates'
  _globals['_CRYPTOSERVICE'].methods_by_name['ListCACertificatesWithFilter']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['ListCACertificatesWithFilter']._serialized_options = b'\202\323\344\223\002=\"8/api/crypto/v1/projects/{project_id}/cacertificates/list:\001*'
  _globals['_CRYPTOSERVICE'].methods_by_name['GetCACertificate']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['GetCACertificate']._serialized_options = b'\202\323\344\223\002$\022\"/api/crypto/v1/cacertificates/{id}'
  _globals['_CRYPTOSERVICE'].methods_by_name['GetCACertificateInstructions']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['GetCACertificateInstructions']._serialized_options = b'\202\323\344\223\0021\022//api/crypto/v1/cacertificates/{id}/instructions'
  _globals['_CRYPTOSERVICE'].methods_by_name['CreateCACertificate']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['CreateCACertificate']._serialized_options = b'\202\323\344\223\0028\"3/api/crypto/v1/projects/{project_id}/cacertificates:\001*'
  _globals['_CRYPTOSERVICE'].methods_by_name['CloneCACertificate']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['CloneCACertificate']._serialized_options = b'\202\323\344\223\002*\"(/api/crypto/v1/cacertificates/{id}/clone'
  _globals['_CRYPTOSERVICE'].methods_by_name['UpdateCACertificate']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['UpdateCACertificate']._serialized_options = b'\202\323\344\223\002\'2\"/api/crypto/v1/cacertificates/{id}:\001*'
  _globals['_CRYPTOSERVICE'].methods_by_name['DeleteCACertificate']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['DeleteCACertificate']._serialized_options = b'\202\323\344\223\002$*\"/api/crypto/v1/cacertificates/{id}'
  _globals['_CRYPTOSERVICE'].methods_by_name['SetDefaultCACertificate']._loaded_options = None
  _globals['_CRYPTOSERVICE'].methods_by_name['SetDefaultCACertificate']._serialized_options = b'\202\323\344\223\002@\";/api/crypto/v1/projects/{project_id}/cacertificates/default:\001*'
  _globals['_CACERTIFICATE']._serialized_start=172
  _globals['_CACERTIFICATE']._serialized_end=668
  _globals['_CACERTIFICATELIST']._serialized_start=670
  _globals['_CACERTIFICATELIST']._serialized_end=745
  _globals['_LISTCACERTIFICATESREQUEST']._serialized_start=747
  _globals['_LISTCACERTIFICATESREQUEST']._serialized_end=874
  _globals['_CACERTIFICATEINSTRUCTIONS']._serialized_start=877
  _globals['_CACERTIFICATEINSTRUCTIONS']._serialized_end=1087
  _globals['_CACERTIFICATEINSTRUCTIONS_PLATFORMINSTRUCTIONS']._serialized_start=999
  _globals['_CACERTIFICATEINSTRUCTIONS_PLATFORMINSTRUCTIONS']._serialized_end=1087
  _globals['_CRYPTOSERVICE']._serialized_start=1090
  _globals['_CRYPTOSERVICE']._serialized_end=2703
# @@protoc_insertion_point(module_scope)
