# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: support/v1/support.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18support/v1/support.proto\x12\x19\x61rangodb.cloud.support.v1\x1a\x16\x63ommon/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\"\xd1\x01\n\x0eSupportRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x15\n\remail_address\x18\x04 \x01(\t\x12\x17\n\x0forganization_id\x18\x05 \x01(\t\x12\x12\n\nproject_id\x18\x06 \x01(\t\x12\x15\n\rdeployment_id\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x10\n\x08severity\x18\t \x01(\t\x12\r\n\x05title\x18\n \x01(\t\"\xc0\x01\n\x04Plan\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nis_default\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x16\n\x0eis_unavailable\x18\x05 \x01(\x08\x12\x46\n\x14\x66irst_response_times\x18\x06 \x01(\x0b\x32(.arangodb.cloud.support.v1.ResponseTimes\x12\x15\n\rsupport_hours\x18\x07 \x01(\t\"L\n\rResponseTimes\x12\x10\n\x08\x63ritical\x18\x01 \x01(\x05\x12\x0c\n\x04high\x18\x02 \x01(\x05\x12\x0e\n\x06normal\x18\x03 \x01(\x05\x12\x0b\n\x03low\x18\x04 \x01(\x05\":\n\x08PlanList\x12.\n\x05items\x18\x01 \x03(\x0b\x32\x1f.arangodb.cloud.support.v1.Plan\"r\n\x10ListPlansRequest\x12\x36\n\x07options\x18\x01 \x01(\x0b\x32%.arangodb.cloud.common.v1.ListOptions\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\"$\n\x08\x46\x61qGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"B\n\x0c\x46\x61qGroupList\x12\x32\n\x05items\x18\x01 \x03(\x0b\x32#.arangodb.cloud.support.v1.FaqGroup\"1\n\rFaqGroupEntry\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x0e\n\x06\x61nswer\x18\x02 \x01(\t\"L\n\x11\x46\x61qGroupEntryList\x12\x37\n\x05items\x18\x01 \x03(\x0b\x32(.arangodb.cloud.support.v1.FaqGroupEntry2\xc2\x06\n\x0eSupportService\x12x\n\rGetAPIVersion\x12\x1f.arangodb.cloud.common.v1.Empty\x1a!.arangodb.cloud.common.v1.Version\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/api/support/v1/api-version\x12|\n\tListPlans\x12+.arangodb.cloud.support.v1.ListPlansRequest\x1a#.arangodb.cloud.support.v1.PlanList\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/api/support/v1/plans\x12s\n\x07GetPlan\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x1f.arangodb.cloud.support.v1.Plan\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/support/v1/plans/{id}\x12\x82\x01\n\rListFaqGroups\x12%.arangodb.cloud.common.v1.ListOptions\x1a\'.arangodb.cloud.support.v1.FaqGroupList\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/api/support/v1/faqgroups\x12\xa2\x01\n\x13ListFaqGroupEntries\x12%.arangodb.cloud.common.v1.ListOptions\x1a,.arangodb.cloud.support.v1.FaqGroupEntryList\"6\x82\xd3\xe4\x93\x02\x30\x12./api/support/v1/faqgroups/{context_id}/entries\x12\x98\x01\n\x14\x43reateSupportRequest\x12).arangodb.cloud.support.v1.SupportRequest\x1a).arangodb.cloud.support.v1.SupportRequest\"*\x82\xd3\xe4\x93\x02$\"\x1f/api/support/v1/supportrequests:\x01*B-Z+github.com/arangodb-managed/apis/support/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'support.v1.support_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/arangodb-managed/apis/support/v1'
  _SUPPORTSERVICE.methods_by_name['GetAPIVersion']._options = None
  _SUPPORTSERVICE.methods_by_name['GetAPIVersion']._serialized_options = b'\202\323\344\223\002\035\022\033/api/support/v1/api-version'
  _SUPPORTSERVICE.methods_by_name['ListPlans']._options = None
  _SUPPORTSERVICE.methods_by_name['ListPlans']._serialized_options = b'\202\323\344\223\002\027\022\025/api/support/v1/plans'
  _SUPPORTSERVICE.methods_by_name['GetPlan']._options = None
  _SUPPORTSERVICE.methods_by_name['GetPlan']._serialized_options = b'\202\323\344\223\002\034\022\032/api/support/v1/plans/{id}'
  _SUPPORTSERVICE.methods_by_name['ListFaqGroups']._options = None
  _SUPPORTSERVICE.methods_by_name['ListFaqGroups']._serialized_options = b'\202\323\344\223\002\033\022\031/api/support/v1/faqgroups'
  _SUPPORTSERVICE.methods_by_name['ListFaqGroupEntries']._options = None
  _SUPPORTSERVICE.methods_by_name['ListFaqGroupEntries']._serialized_options = b'\202\323\344\223\0020\022./api/support/v1/faqgroups/{context_id}/entries'
  _SUPPORTSERVICE.methods_by_name['CreateSupportRequest']._options = None
  _SUPPORTSERVICE.methods_by_name['CreateSupportRequest']._serialized_options = b'\202\323\344\223\002$\"\037/api/support/v1/supportrequests:\001*'
  _SUPPORTREQUEST._serialized_start=110
  _SUPPORTREQUEST._serialized_end=319
  _PLAN._serialized_start=322
  _PLAN._serialized_end=514
  _RESPONSETIMES._serialized_start=516
  _RESPONSETIMES._serialized_end=592
  _PLANLIST._serialized_start=594
  _PLANLIST._serialized_end=652
  _LISTPLANSREQUEST._serialized_start=654
  _LISTPLANSREQUEST._serialized_end=768
  _FAQGROUP._serialized_start=770
  _FAQGROUP._serialized_end=806
  _FAQGROUPLIST._serialized_start=808
  _FAQGROUPLIST._serialized_end=874
  _FAQGROUPENTRY._serialized_start=876
  _FAQGROUPENTRY._serialized_end=925
  _FAQGROUPENTRYLIST._serialized_start=927
  _FAQGROUPENTRYLIST._serialized_end=1003
  _SUPPORTSERVICE._serialized_start=1006
  _SUPPORTSERVICE._serialized_end=1840
# @@protoc_insertion_point(module_scope)