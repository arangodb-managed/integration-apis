# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: resourcemanager/v1/resourcemanager.proto
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
    'resourcemanager/v1/resourcemanager.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from iam.v1 import iam_pb2 as iam_dot_v1_dot_iam__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(resourcemanager/v1/resourcemanager.proto\x12!arangodb.cloud.resourcemanager.v1\x1a\x16\x63ommon/v1/common.proto\x1a\x10iam/v1/iam.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xda\x07\n\x0cOrganization\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\nis_deleted\x18\x05 \x01(\x08\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x04tier\x18\x08 \x01(\x0b\x32\'.arangodb.cloud.resourcemanager.v1.Tier\x12`\n\x11total_deployments\x18\t \x03(\x0b\x32\x45.arangodb.cloud.resourcemanager.v1.Organization.TotalDeploymentsEntry\x12\'\n\x1fis_flexible_deployments_enabled\x18\n \x01(\x08\x12\'\n\x1fis_allowed_to_use_custom_images\x18\x0b \x01(\x08\x12&\n\x1eis_allowed_to_use_iamproviders\x18\x0c \x01(\x08\x12\x0e\n\x06locked\x18\r \x01(\x08\x12$\n\x1crequires_prepaid_deployments\x18\x0e \x01(\x08\x12\\\n\x18\x61uthentication_providers\x18\x0f \x01(\x0b\x32:.arangodb.cloud.resourcemanager.v1.AuthenticationProviders\x12X\n\x19\x65mail_domain_restrictions\x18\x10 \x01(\x0b\x32\x35.arangodb.cloud.resourcemanager.v1.DomainRestrictions\x12\x1e\n\x16is_allowed_to_use_scim\x18\x11 \x01(\x08\x12Y\n\rnotifications\x18\x12 \x03(\x0b\x32\x42.arangodb.cloud.resourcemanager.v1.Organization.NotificationsEntry\x1a\x37\n\x15TotalDeploymentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x65\n\x12NotificationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.arangodb.cloud.resourcemanager.v1.Notification:\x02\x38\x01\"\x84\x01\n\x10OrganizationList\x12>\n\x05items\x18\x01 \x03(\x0b\x32/.arangodb.cloud.resourcemanager.v1.Organization\x12\x30\n\x06\x62udget\x18\x02 \x01(\x0b\x32 .arangodb.cloud.common.v1.Budget\"\x97\x01\n\x17\x41uthenticationProviders\x12 \n\x18\x65nable_username_password\x18\x01 \x01(\x08\x12\x15\n\renable_google\x18\x02 \x01(\x08\x12\x15\n\renable_github\x18\x03 \x01(\x08\x12\x18\n\x10\x65nable_microsoft\x18\x04 \x01(\x08\x12\x12\n\nenable_sso\x18\x05 \x01(\x08\"-\n\x12\x44omainRestrictions\x12\x17\n\x0f\x61llowed_domains\x18\x01 \x03(\t\"\x83\x03\n\x04Tier\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11has_support_plans\x18\x03 \x01(\x08\x12\x1a\n\x12has_backup_uploads\x18\x04 \x01(\x08\x12%\n\x1drequires_terms_and_conditions\x18\x05 \x01(\x08\x12!\n\x19has_support_severity_high\x18\x06 \x01(\x08\x12%\n\x1dhas_support_severity_critical\x18\x07 \x01(\x08\x12\x1c\n\x14has_auditlog_feature\x18\x08 \x01(\x08\x12&\n\x1ehas_auditlog_destination_cloud\x18\t \x01(\x08\x12+\n#has_auditlog_destination_https_post\x18\n \x01(\x08\x12\x1d\n\x15has_private_endpoints\x18\x0b \x01(\x08\x12\'\n\x1fhas_multi_region_backup_uploads\x18\x0c \x01(\x08\"S\n\x06Member\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\x08\x12)\n\x04user\x18\x03 \x01(\x0b\x32\x1b.arangodb.cloud.iam.v1.User\"F\n\nMemberList\x12\x38\n\x05items\x18\x01 \x03(\x0b\x32).arangodb.cloud.resourcemanager.v1.Member\"I\n\x1dIsMemberOfOrganizationRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\"?\n\x1eIsMemberOfOrganizationResponse\x12\x0e\n\x06member\x18\x01 \x01(\x08\x12\r\n\x05owner\x18\x02 \x01(\x08\"u\n\x1aOrganizationMembersRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12>\n\x07members\x18\x02 \x01(\x0b\x32-.arangodb.cloud.resourcemanager.v1.MemberList\"\x8b\x02\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x17\n\x0forganization_id\x18\x05 \x01(\t\x12\x12\n\nis_deleted\x18\x06 \x01(\x08\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x1fis_flexible_deployments_enabled\x18\t \x01(\x08\x12\x0e\n\x06locked\x18\n \x01(\x08\"z\n\x0bProjectList\x12\x39\n\x05items\x18\x01 \x03(\x0b\x32*.arangodb.cloud.resourcemanager.v1.Project\x12\x30\n\x06\x62udget\x18\x02 \x01(\x0b\x32 .arangodb.cloud.common.v1.Budget\"\xfc\x02\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x17\n\x0forganization_id\x18\x03 \x01(\t\x12\x12\n\nsubject_id\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x46\n\x07payload\x18\x06 \x03(\x0b\x32\x35.arangodb.cloud.resourcemanager.v1.Event.PayloadEntry\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bsubject_url\x18\x08 \x01(\t\x12\x10\n\x08volatile\x18\t \x01(\x08\x12\x15\n\rcreated_by_id\x18\n \x01(\t\x12\x0e\n\x06reason\x18\x0b \x01(\t\x12\x13\n\x0bstatus_only\x18\x0c \x01(\x08\x12\x14\n\x0c\x63reated_with\x18\r \x01(\t\x1a.\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"D\n\tEventList\x12\x37\n\x05items\x18\x01 \x03(\x0b\x32(.arangodb.cloud.resourcemanager.v1.Event\"\xee\x01\n\x10ListEventOptions\x12\x36\n\x07options\x18\x01 \x01(\x0b\x32%.arangodb.cloud.common.v1.ListOptions\x12\x13\n\x0bsubject_ids\x18\x02 \x03(\t\x12\r\n\x05types\x18\x03 \x03(\t\x12\x31\n\rcreated_after\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0e\x63reated_before\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0fsort_descending\x18\x06 \x01(\x08\"\xe7\x02\n\x12OrganizationInvite\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x17\n\x0forganization_id\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x05 \x01(\x08\x12\x10\n\x08rejected\x18\x06 \x01(\x08\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x61\x63\x63\x65pted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0brejected_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07user_id\x18\n \x01(\t\x12\x15\n\rcreated_by_id\x18\x0b \x01(\t\x12\x19\n\x11organization_name\x18\x0c \x01(\t\x12\x17\n\x0f\x63reated_by_name\x18\r \x01(\t\"^\n\x16OrganizationInviteList\x12\x44\n\x05items\x18\x01 \x03(\x0b\x32\x35.arangodb.cloud.resourcemanager.v1.OrganizationInvite\"f\n\x10QuotaDescription\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x19\n\x11\x66or_organizations\x18\x03 \x01(\x08\x12\x14\n\x0c\x66or_projects\x18\x04 \x01(\x08\"Z\n\x14QuotaDescriptionList\x12\x42\n\x05items\x18\x01 \x03(\x0b\x32\x33.arangodb.cloud.resourcemanager.v1.QuotaDescription\"9\n\x05Quota\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x03\"D\n\tQuotaList\x12\x37\n\x05items\x18\x01 \x03(\x0b\x32(.arangodb.cloud.resourcemanager.v1.Quota\"Z\n\x11ListQuotasRequest\x12\x36\n\x07options\x18\x01 \x01(\x0b\x32%.arangodb.cloud.common.v1.ListOptions\x12\r\n\x05kinds\x18\x02 \x03(\t\"a\n\x12TermsAndConditions\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"e\n\x16\x44\x61taProcessingAddendum\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xff\x01\n\x0cNotification\x12\x14\n\x0cnotification\x18\x01 \x01(\t\x12I\n\x08severity\x18\x02 \x01(\x0e\x32\x37.arangodb.cloud.resourcemanager.v1.NotificationSeverity\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpires_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*}\n\x14NotificationSeverity\x12\x1e\n\x1aNOTIFICATION_SEVERITY_INFO\x10\x00\x12!\n\x1dNOTIFICATION_SEVERITY_WARNING\x10\x01\x12\"\n\x1eNOTIFICATION_SEVERITY_CRITICAL\x10\x02\x32\xa7+\n\x16ResourceManagerService\x12\x80\x01\n\rGetAPIVersion\x12\x1f.arangodb.cloud.common.v1.Empty\x1a!.arangodb.cloud.common.v1.Version\"+\x82\xd3\xe4\x93\x02%\x12#/api/resourcemanager/v1/api-version\x12\xa3\x01\n\x11ListOrganizations\x12%.arangodb.cloud.common.v1.ListOptions\x1a\x33.arangodb.cloud.resourcemanager.v1.OrganizationList\"2\x82\xd3\xe4\x93\x02,\x12*/api/resourcemanager/v1/self/organizations\x12\x9b\x01\n\x0fGetOrganization\x12#.arangodb.cloud.common.v1.IDOptions\x1a/.arangodb.cloud.resourcemanager.v1.Organization\"2\x82\xd3\xe4\x93\x02,\x12*/api/resourcemanager/v1/organizations/{id}\x12\xa8\x01\n\x12\x43reateOrganization\x12/.arangodb.cloud.resourcemanager.v1.Organization\x1a/.arangodb.cloud.resourcemanager.v1.Organization\"0\x82\xd3\xe4\x93\x02*\"%/api/resourcemanager/v1/organizations:\x01*\x12\xad\x01\n\x12UpdateOrganization\x12/.arangodb.cloud.resourcemanager.v1.Organization\x1a/.arangodb.cloud.resourcemanager.v1.Organization\"5\x82\xd3\xe4\x93\x02/2*/api/resourcemanager/v1/organizations/{id}:\x01*\x12\x8e\x01\n\x12\x44\x65leteOrganization\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x1f.arangodb.cloud.common.v1.Empty\"2\x82\xd3\xe4\x93\x02,**/api/resourcemanager/v1/organizations/{id}\x12\xb3\x01\n\x17ListOrganizationMembers\x12%.arangodb.cloud.common.v1.ListOptions\x1a-.arangodb.cloud.resourcemanager.v1.MemberList\"B\x82\xd3\xe4\x93\x02<\x12:/api/resourcemanager/v1/organizations/{context_id}/members\x12\xc4\x01\n\x16\x41\x64\x64OrganizationMembers\x12=.arangodb.cloud.resourcemanager.v1.OrganizationMembersRequest\x1a\x1f.arangodb.cloud.common.v1.Empty\"J\x82\xd3\xe4\x93\x02\x44\"?/api/resourcemanager/v1/organizations/{organization_id}/members:\x01*\x12\xc7\x01\n\x19UpdateOrganizationMembers\x12=.arangodb.cloud.resourcemanager.v1.OrganizationMembersRequest\x1a\x1f.arangodb.cloud.common.v1.Empty\"J\x82\xd3\xe4\x93\x02\x44\x32?/api/resourcemanager/v1/organizations/{organization_id}/members:\x01*\x12\xc7\x01\n\x19\x44\x65leteOrganizationMembers\x12=.arangodb.cloud.resourcemanager.v1.OrganizationMembersRequest\x1a\x1f.arangodb.cloud.common.v1.Empty\"J\x82\xd3\xe4\x93\x02\x44*?/api/resourcemanager/v1/organizations/{organization_id}/members:\x01*\x12\xf0\x01\n\x16IsMemberOfOrganization\x12@.arangodb.cloud.resourcemanager.v1.IsMemberOfOrganizationRequest\x1a\x41.arangodb.cloud.resourcemanager.v1.IsMemberOfOrganizationResponse\"Q\x82\xd3\xe4\x93\x02K\x12I/api/resourcemanager/v1/organizations/{organization_id}/members/{user_id}\x12\xc7\x01\n\x16ListOrganizationQuotas\x12\x34.arangodb.cloud.resourcemanager.v1.ListQuotasRequest\x1a,.arangodb.cloud.resourcemanager.v1.QuotaList\"I\x82\xd3\xe4\x93\x02\x43\x12\x41/api/resourcemanager/v1/organizations/{options.context_id}/quotas\x12\xaa\x01\n\x0cListProjects\x12%.arangodb.cloud.common.v1.ListOptions\x1a..arangodb.cloud.resourcemanager.v1.ProjectList\"C\x82\xd3\xe4\x93\x02=\x12;/api/resourcemanager/v1/organizations/{context_id}/projects\x12\x8c\x01\n\nGetProject\x12#.arangodb.cloud.common.v1.IDOptions\x1a*.arangodb.cloud.resourcemanager.v1.Project\"-\x82\xd3\xe4\x93\x02\'\x12%/api/resourcemanager/v1/projects/{id}\x12\xb4\x01\n\rCreateProject\x12*.arangodb.cloud.resourcemanager.v1.Project\x1a*.arangodb.cloud.resourcemanager.v1.Project\"K\x82\xd3\xe4\x93\x02\x45\"@/api/resourcemanager/v1/organizations/{organization_id}/projects:\x01*\x12\x99\x01\n\rUpdateProject\x12*.arangodb.cloud.resourcemanager.v1.Project\x1a*.arangodb.cloud.resourcemanager.v1.Project\"0\x82\xd3\xe4\x93\x02*2%/api/resourcemanager/v1/projects/{id}:\x01*\x12\x84\x01\n\rDeleteProject\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x1f.arangodb.cloud.common.v1.Empty\"-\x82\xd3\xe4\x93\x02\'*%/api/resourcemanager/v1/projects/{id}\x12\xbd\x01\n\x11ListProjectQuotas\x12\x34.arangodb.cloud.resourcemanager.v1.ListQuotasRequest\x1a,.arangodb.cloud.resourcemanager.v1.QuotaList\"D\x82\xd3\xe4\x93\x02>\x12</api/resourcemanager/v1/projects/{options.context_id}/quotas\x12\xbd\x01\n\nListEvents\x12\x33.arangodb.cloud.resourcemanager.v1.ListEventOptions\x1a,.arangodb.cloud.resourcemanager.v1.EventList\"L\x82\xd3\xe4\x93\x02\x46\"A/api/resourcemanager/v1/organizations/{options.context_id}/events:\x01*\x12\xcc\x01\n\x17ListOrganizationInvites\x12%.arangodb.cloud.common.v1.ListOptions\x1a\x39.arangodb.cloud.resourcemanager.v1.OrganizationInviteList\"O\x82\xd3\xe4\x93\x02I\x12G/api/resourcemanager/v1/organizations/{context_id}/organization-invites\x12\xb8\x01\n\x19ListMyOrganizationInvites\x12%.arangodb.cloud.common.v1.ListOptions\x1a\x39.arangodb.cloud.resourcemanager.v1.OrganizationInviteList\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/api/resourcemanager/v1/self/organization-invites\x12\xae\x01\n\x15GetOrganizationInvite\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x35.arangodb.cloud.resourcemanager.v1.OrganizationInvite\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/api/resourcemanager/v1/organization-invites/{id}\x12\xe1\x01\n\x18\x43reateOrganizationInvite\x12\x35.arangodb.cloud.resourcemanager.v1.OrganizationInvite\x1a\x35.arangodb.cloud.resourcemanager.v1.OrganizationInvite\"W\x82\xd3\xe4\x93\x02Q\"L/api/resourcemanager/v1/organizations/{organization_id}/organization-invites:\x01*\x12\x9b\x01\n\x18\x44\x65leteOrganizationInvite\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x1f.arangodb.cloud.common.v1.Empty\"9\x82\xd3\xe4\x93\x02\x33*1/api/resourcemanager/v1/organization-invites/{id}\x12\xa2\x01\n\x18\x41\x63\x63\x65ptOrganizationInvite\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x1f.arangodb.cloud.common.v1.Empty\"@\x82\xd3\xe4\x93\x02:\"8/api/resourcemanager/v1/organization-invites/{id}/accept\x12\xa2\x01\n\x18RejectOrganizationInvite\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x1f.arangodb.cloud.common.v1.Empty\"@\x82\xd3\xe4\x93\x02:\"8/api/resourcemanager/v1/organization-invites/{id}/reject\x12\xac\x01\n\x15ListQuotaDescriptions\x12%.arangodb.cloud.common.v1.ListOptions\x1a\x37.arangodb.cloud.resourcemanager.v1.QuotaDescriptionList\"3\x82\xd3\xe4\x93\x02-\x12+/api/resourcemanager/v1/quotas/descriptions\x12\xac\x01\n\x15GetTermsAndConditions\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x35.arangodb.cloud.resourcemanager.v1.TermsAndConditions\"7\x82\xd3\xe4\x93\x02\x31\x12//api/resourcemanager/v1/termsandconditions/{id}\x12\xb6\x01\n\x1cGetCurrentTermsAndConditions\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x35.arangodb.cloud.resourcemanager.v1.TermsAndConditions\":\x82\xd3\xe4\x93\x02\x34\x12\x32/api/resourcemanager/v1/current-termsandconditions\x12\xa5\x01\n\x19GetDataProcessingAddendum\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x39.arangodb.cloud.resourcemanager.v1.DataProcessingAddendum\"(\x82\xd3\xe4\x93\x02\"\x12 /api/resourcemanager/v1/dpa/{id}\x12\xaf\x01\n GetCurrentDataProcessingAddendum\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x39.arangodb.cloud.resourcemanager.v1.DataProcessingAddendum\"+\x82\xd3\xe4\x93\x02%\x12#/api/resourcemanager/v1/current-dpaB5Z3github.com/arangodb-managed/apis/resourcemanager/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'resourcemanager.v1.resourcemanager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/arangodb-managed/apis/resourcemanager/v1'
  _globals['_ORGANIZATION_TOTALDEPLOYMENTSENTRY']._loaded_options = None
  _globals['_ORGANIZATION_TOTALDEPLOYMENTSENTRY']._serialized_options = b'8\001'
  _globals['_ORGANIZATION_NOTIFICATIONSENTRY']._loaded_options = None
  _globals['_ORGANIZATION_NOTIFICATIONSENTRY']._serialized_options = b'8\001'
  _globals['_EVENT_PAYLOADENTRY']._loaded_options = None
  _globals['_EVENT_PAYLOADENTRY']._serialized_options = b'8\001'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetAPIVersion']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetAPIVersion']._serialized_options = b'\202\323\344\223\002%\022#/api/resourcemanager/v1/api-version'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListOrganizations']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListOrganizations']._serialized_options = b'\202\323\344\223\002,\022*/api/resourcemanager/v1/self/organizations'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetOrganization']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetOrganization']._serialized_options = b'\202\323\344\223\002,\022*/api/resourcemanager/v1/organizations/{id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['CreateOrganization']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['CreateOrganization']._serialized_options = b'\202\323\344\223\002*\"%/api/resourcemanager/v1/organizations:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['UpdateOrganization']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['UpdateOrganization']._serialized_options = b'\202\323\344\223\002/2*/api/resourcemanager/v1/organizations/{id}:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['DeleteOrganization']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['DeleteOrganization']._serialized_options = b'\202\323\344\223\002,**/api/resourcemanager/v1/organizations/{id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListOrganizationMembers']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListOrganizationMembers']._serialized_options = b'\202\323\344\223\002<\022:/api/resourcemanager/v1/organizations/{context_id}/members'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['AddOrganizationMembers']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['AddOrganizationMembers']._serialized_options = b'\202\323\344\223\002D\"?/api/resourcemanager/v1/organizations/{organization_id}/members:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['UpdateOrganizationMembers']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['UpdateOrganizationMembers']._serialized_options = b'\202\323\344\223\002D2?/api/resourcemanager/v1/organizations/{organization_id}/members:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['DeleteOrganizationMembers']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['DeleteOrganizationMembers']._serialized_options = b'\202\323\344\223\002D*?/api/resourcemanager/v1/organizations/{organization_id}/members:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['IsMemberOfOrganization']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['IsMemberOfOrganization']._serialized_options = b'\202\323\344\223\002K\022I/api/resourcemanager/v1/organizations/{organization_id}/members/{user_id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListOrganizationQuotas']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListOrganizationQuotas']._serialized_options = b'\202\323\344\223\002C\022A/api/resourcemanager/v1/organizations/{options.context_id}/quotas'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListProjects']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListProjects']._serialized_options = b'\202\323\344\223\002=\022;/api/resourcemanager/v1/organizations/{context_id}/projects'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetProject']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetProject']._serialized_options = b'\202\323\344\223\002\'\022%/api/resourcemanager/v1/projects/{id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['CreateProject']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['CreateProject']._serialized_options = b'\202\323\344\223\002E\"@/api/resourcemanager/v1/organizations/{organization_id}/projects:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['UpdateProject']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['UpdateProject']._serialized_options = b'\202\323\344\223\002*2%/api/resourcemanager/v1/projects/{id}:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['DeleteProject']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['DeleteProject']._serialized_options = b'\202\323\344\223\002\'*%/api/resourcemanager/v1/projects/{id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListProjectQuotas']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListProjectQuotas']._serialized_options = b'\202\323\344\223\002>\022</api/resourcemanager/v1/projects/{options.context_id}/quotas'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListEvents']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListEvents']._serialized_options = b'\202\323\344\223\002F\"A/api/resourcemanager/v1/organizations/{options.context_id}/events:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListOrganizationInvites']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListOrganizationInvites']._serialized_options = b'\202\323\344\223\002I\022G/api/resourcemanager/v1/organizations/{context_id}/organization-invites'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListMyOrganizationInvites']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListMyOrganizationInvites']._serialized_options = b'\202\323\344\223\0023\0221/api/resourcemanager/v1/self/organization-invites'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetOrganizationInvite']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetOrganizationInvite']._serialized_options = b'\202\323\344\223\0023\0221/api/resourcemanager/v1/organization-invites/{id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['CreateOrganizationInvite']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['CreateOrganizationInvite']._serialized_options = b'\202\323\344\223\002Q\"L/api/resourcemanager/v1/organizations/{organization_id}/organization-invites:\001*'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['DeleteOrganizationInvite']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['DeleteOrganizationInvite']._serialized_options = b'\202\323\344\223\0023*1/api/resourcemanager/v1/organization-invites/{id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['AcceptOrganizationInvite']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['AcceptOrganizationInvite']._serialized_options = b'\202\323\344\223\002:\"8/api/resourcemanager/v1/organization-invites/{id}/accept'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['RejectOrganizationInvite']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['RejectOrganizationInvite']._serialized_options = b'\202\323\344\223\002:\"8/api/resourcemanager/v1/organization-invites/{id}/reject'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListQuotaDescriptions']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['ListQuotaDescriptions']._serialized_options = b'\202\323\344\223\002-\022+/api/resourcemanager/v1/quotas/descriptions'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetTermsAndConditions']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetTermsAndConditions']._serialized_options = b'\202\323\344\223\0021\022//api/resourcemanager/v1/termsandconditions/{id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetCurrentTermsAndConditions']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetCurrentTermsAndConditions']._serialized_options = b'\202\323\344\223\0024\0222/api/resourcemanager/v1/current-termsandconditions'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetDataProcessingAddendum']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetDataProcessingAddendum']._serialized_options = b'\202\323\344\223\002\"\022 /api/resourcemanager/v1/dpa/{id}'
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetCurrentDataProcessingAddendum']._loaded_options = None
  _globals['_RESOURCEMANAGERSERVICE'].methods_by_name['GetCurrentDataProcessingAddendum']._serialized_options = b'\202\323\344\223\002%\022#/api/resourcemanager/v1/current-dpa'
  _globals['_NOTIFICATIONSEVERITY']._serialized_start=4738
  _globals['_NOTIFICATIONSEVERITY']._serialized_end=4863
  _globals['_ORGANIZATION']._serialized_start=185
  _globals['_ORGANIZATION']._serialized_end=1171
  _globals['_ORGANIZATION_TOTALDEPLOYMENTSENTRY']._serialized_start=1013
  _globals['_ORGANIZATION_TOTALDEPLOYMENTSENTRY']._serialized_end=1068
  _globals['_ORGANIZATION_NOTIFICATIONSENTRY']._serialized_start=1070
  _globals['_ORGANIZATION_NOTIFICATIONSENTRY']._serialized_end=1171
  _globals['_ORGANIZATIONLIST']._serialized_start=1174
  _globals['_ORGANIZATIONLIST']._serialized_end=1306
  _globals['_AUTHENTICATIONPROVIDERS']._serialized_start=1309
  _globals['_AUTHENTICATIONPROVIDERS']._serialized_end=1460
  _globals['_DOMAINRESTRICTIONS']._serialized_start=1462
  _globals['_DOMAINRESTRICTIONS']._serialized_end=1507
  _globals['_TIER']._serialized_start=1510
  _globals['_TIER']._serialized_end=1897
  _globals['_MEMBER']._serialized_start=1899
  _globals['_MEMBER']._serialized_end=1982
  _globals['_MEMBERLIST']._serialized_start=1984
  _globals['_MEMBERLIST']._serialized_end=2054
  _globals['_ISMEMBEROFORGANIZATIONREQUEST']._serialized_start=2056
  _globals['_ISMEMBEROFORGANIZATIONREQUEST']._serialized_end=2129
  _globals['_ISMEMBEROFORGANIZATIONRESPONSE']._serialized_start=2131
  _globals['_ISMEMBEROFORGANIZATIONRESPONSE']._serialized_end=2194
  _globals['_ORGANIZATIONMEMBERSREQUEST']._serialized_start=2196
  _globals['_ORGANIZATIONMEMBERSREQUEST']._serialized_end=2313
  _globals['_PROJECT']._serialized_start=2316
  _globals['_PROJECT']._serialized_end=2583
  _globals['_PROJECTLIST']._serialized_start=2585
  _globals['_PROJECTLIST']._serialized_end=2707
  _globals['_EVENT']._serialized_start=2710
  _globals['_EVENT']._serialized_end=3090
  _globals['_EVENT_PAYLOADENTRY']._serialized_start=3044
  _globals['_EVENT_PAYLOADENTRY']._serialized_end=3090
  _globals['_EVENTLIST']._serialized_start=3092
  _globals['_EVENTLIST']._serialized_end=3160
  _globals['_LISTEVENTOPTIONS']._serialized_start=3163
  _globals['_LISTEVENTOPTIONS']._serialized_end=3401
  _globals['_ORGANIZATIONINVITE']._serialized_start=3404
  _globals['_ORGANIZATIONINVITE']._serialized_end=3763
  _globals['_ORGANIZATIONINVITELIST']._serialized_start=3765
  _globals['_ORGANIZATIONINVITELIST']._serialized_end=3859
  _globals['_QUOTADESCRIPTION']._serialized_start=3861
  _globals['_QUOTADESCRIPTION']._serialized_end=3963
  _globals['_QUOTADESCRIPTIONLIST']._serialized_start=3965
  _globals['_QUOTADESCRIPTIONLIST']._serialized_end=4055
  _globals['_QUOTA']._serialized_start=4057
  _globals['_QUOTA']._serialized_end=4114
  _globals['_QUOTALIST']._serialized_start=4116
  _globals['_QUOTALIST']._serialized_end=4184
  _globals['_LISTQUOTASREQUEST']._serialized_start=4186
  _globals['_LISTQUOTASREQUEST']._serialized_end=4276
  _globals['_TERMSANDCONDITIONS']._serialized_start=4278
  _globals['_TERMSANDCONDITIONS']._serialized_end=4375
  _globals['_DATAPROCESSINGADDENDUM']._serialized_start=4377
  _globals['_DATAPROCESSINGADDENDUM']._serialized_end=4478
  _globals['_NOTIFICATION']._serialized_start=4481
  _globals['_NOTIFICATION']._serialized_end=4736
  _globals['_RESOURCEMANAGERSERVICE']._serialized_start=4866
  _globals['_RESOURCEMANAGERSERVICE']._serialized_end=10409
# @@protoc_insertion_point(module_scope)
