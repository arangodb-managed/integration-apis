from common.v1 import common_pb2 as _common_pb2
from iam.v1 import iam_pb2 as _iam_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticationProviders(_message.Message):
    __slots__ = ["enable_github", "enable_google", "enable_microsoft", "enable_username_password"]
    ENABLE_GITHUB_FIELD_NUMBER: _ClassVar[int]
    ENABLE_GOOGLE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MICROSOFT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_USERNAME_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    enable_github: bool
    enable_google: bool
    enable_microsoft: bool
    enable_username_password: bool
    def __init__(self, enable_username_password: bool = ..., enable_google: bool = ..., enable_github: bool = ..., enable_microsoft: bool = ...) -> None: ...

class DataProcessingAddendum(_message.Message):
    __slots__ = ["content", "created_at", "id"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    content: str
    created_at: _timestamp_pb2.Timestamp
    id: str
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DomainRestrictions(_message.Message):
    __slots__ = ["allowed_domains"]
    ALLOWED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    allowed_domains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowed_domains: _Optional[_Iterable[str]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["created_at", "created_by_id", "id", "organization_id", "payload", "reason", "status_only", "subject_id", "subject_url", "type", "url", "volatile"]
    class PayloadEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    STATUS_ONLY_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VOLATILE_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    created_by_id: str
    id: str
    organization_id: str
    payload: _containers.ScalarMap[str, str]
    reason: str
    status_only: bool
    subject_id: str
    subject_url: str
    type: str
    url: str
    volatile: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., subject_id: _Optional[str] = ..., type: _Optional[str] = ..., payload: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., subject_url: _Optional[str] = ..., volatile: bool = ..., created_by_id: _Optional[str] = ..., reason: _Optional[str] = ..., status_only: bool = ...) -> None: ...

class EventList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, items: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class IsMemberOfOrganizationRequest(_message.Message):
    __slots__ = ["organization_id", "user_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class IsMemberOfOrganizationResponse(_message.Message):
    __slots__ = ["member", "owner"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    member: bool
    owner: bool
    def __init__(self, member: bool = ..., owner: bool = ...) -> None: ...

class ListEventOptions(_message.Message):
    __slots__ = ["created_after", "created_before", "options", "sort_descending", "subject_ids", "types"]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SORT_DESCENDING_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    created_after: _timestamp_pb2.Timestamp
    created_before: _timestamp_pb2.Timestamp
    options: _common_pb2.ListOptions
    sort_descending: bool
    subject_ids: _containers.RepeatedScalarFieldContainer[str]
    types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., subject_ids: _Optional[_Iterable[str]] = ..., types: _Optional[_Iterable[str]] = ..., created_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sort_descending: bool = ...) -> None: ...

class ListQuotasRequest(_message.Message):
    __slots__ = ["kinds", "options"]
    KINDS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    kinds: _containers.RepeatedScalarFieldContainer[str]
    options: _common_pb2.ListOptions
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., kinds: _Optional[_Iterable[str]] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ["owner", "user", "user_id"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    owner: bool
    user: _iam_pb2.User
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., owner: bool = ..., user: _Optional[_Union[_iam_pb2.User, _Mapping]] = ...) -> None: ...

class MemberList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, items: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class Organization(_message.Message):
    __slots__ = ["authentication_providers", "created_at", "deleted_at", "description", "email_domain_restrictions", "id", "is_allowed_to_use_custom_images", "is_allowed_to_use_iamproviders", "is_allowed_to_use_scim", "is_deleted", "is_flexible_deployments_enabled", "locked", "name", "requires_prepaid_deployments", "tier", "total_deployments", "url"]
    class TotalDeploymentsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    AUTHENTICATION_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DOMAIN_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_TO_USE_CUSTOM_IMAGES_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_TO_USE_IAMPROVIDERS_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_TO_USE_SCIM_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_FLEXIBLE_DEPLOYMENTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_PREPAID_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    authentication_providers: AuthenticationProviders
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    description: str
    email_domain_restrictions: DomainRestrictions
    id: str
    is_allowed_to_use_custom_images: bool
    is_allowed_to_use_iamproviders: bool
    is_allowed_to_use_scim: bool
    is_deleted: bool
    is_flexible_deployments_enabled: bool
    locked: bool
    name: str
    requires_prepaid_deployments: bool
    tier: Tier
    total_deployments: _containers.ScalarMap[str, int]
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tier: _Optional[_Union[Tier, _Mapping]] = ..., total_deployments: _Optional[_Mapping[str, int]] = ..., is_flexible_deployments_enabled: bool = ..., is_allowed_to_use_custom_images: bool = ..., is_allowed_to_use_iamproviders: bool = ..., locked: bool = ..., requires_prepaid_deployments: bool = ..., authentication_providers: _Optional[_Union[AuthenticationProviders, _Mapping]] = ..., email_domain_restrictions: _Optional[_Union[DomainRestrictions, _Mapping]] = ..., is_allowed_to_use_scim: bool = ...) -> None: ...

class OrganizationInvite(_message.Message):
    __slots__ = ["accepted", "accepted_at", "created_at", "created_by_id", "created_by_name", "email", "id", "organization_id", "organization_name", "rejected", "rejected_at", "url", "user_id"]
    ACCEPTED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    REJECTED_AT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    accepted_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    created_by_id: str
    created_by_name: str
    email: str
    id: str
    organization_id: str
    organization_name: str
    rejected: bool
    rejected_at: _timestamp_pb2.Timestamp
    url: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., email: _Optional[str] = ..., accepted: bool = ..., rejected: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., accepted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., created_by_id: _Optional[str] = ..., organization_name: _Optional[str] = ..., created_by_name: _Optional[str] = ...) -> None: ...

class OrganizationInviteList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[OrganizationInvite]
    def __init__(self, items: _Optional[_Iterable[_Union[OrganizationInvite, _Mapping]]] = ...) -> None: ...

class OrganizationList(_message.Message):
    __slots__ = ["budget", "items"]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    budget: _common_pb2.Budget
    items: _containers.RepeatedCompositeFieldContainer[Organization]
    def __init__(self, items: _Optional[_Iterable[_Union[Organization, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class OrganizationMembersRequest(_message.Message):
    __slots__ = ["members", "organization_id"]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    members: MemberList
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ..., members: _Optional[_Union[MemberList, _Mapping]] = ...) -> None: ...

class Project(_message.Message):
    __slots__ = ["created_at", "deleted_at", "description", "id", "is_deleted", "is_flexible_deployments_enabled", "locked", "name", "organization_id", "url"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_FLEXIBLE_DEPLOYMENTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    description: str
    id: str
    is_deleted: bool
    is_flexible_deployments_enabled: bool
    locked: bool
    name: str
    organization_id: str
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_flexible_deployments_enabled: bool = ..., locked: bool = ...) -> None: ...

class ProjectList(_message.Message):
    __slots__ = ["budget", "items"]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    budget: _common_pb2.Budget
    items: _containers.RepeatedCompositeFieldContainer[Project]
    def __init__(self, items: _Optional[_Iterable[_Union[Project, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class Quota(_message.Message):
    __slots__ = ["description", "kind", "limit"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    description: str
    kind: str
    limit: int
    def __init__(self, kind: _Optional[str] = ..., description: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class QuotaDescription(_message.Message):
    __slots__ = ["description", "for_organizations", "for_projects", "kind"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FOR_ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    FOR_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    description: str
    for_organizations: bool
    for_projects: bool
    kind: str
    def __init__(self, kind: _Optional[str] = ..., description: _Optional[str] = ..., for_organizations: bool = ..., for_projects: bool = ...) -> None: ...

class QuotaDescriptionList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[QuotaDescription]
    def __init__(self, items: _Optional[_Iterable[_Union[QuotaDescription, _Mapping]]] = ...) -> None: ...

class QuotaList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Quota]
    def __init__(self, items: _Optional[_Iterable[_Union[Quota, _Mapping]]] = ...) -> None: ...

class TermsAndConditions(_message.Message):
    __slots__ = ["content", "created_at", "id"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    content: str
    created_at: _timestamp_pb2.Timestamp
    id: str
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Tier(_message.Message):
    __slots__ = ["has_auditlog_destination_cloud", "has_auditlog_destination_https_post", "has_auditlog_feature", "has_backup_uploads", "has_multi_region_backup_uploads", "has_private_endpoints", "has_support_plans", "has_support_severity_critical", "has_support_severity_high", "id", "name", "requires_terms_and_conditions"]
    HAS_AUDITLOG_DESTINATION_CLOUD_FIELD_NUMBER: _ClassVar[int]
    HAS_AUDITLOG_DESTINATION_HTTPS_POST_FIELD_NUMBER: _ClassVar[int]
    HAS_AUDITLOG_FEATURE_FIELD_NUMBER: _ClassVar[int]
    HAS_BACKUP_UPLOADS_FIELD_NUMBER: _ClassVar[int]
    HAS_MULTI_REGION_BACKUP_UPLOADS_FIELD_NUMBER: _ClassVar[int]
    HAS_PRIVATE_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    HAS_SUPPORT_PLANS_FIELD_NUMBER: _ClassVar[int]
    HAS_SUPPORT_SEVERITY_CRITICAL_FIELD_NUMBER: _ClassVar[int]
    HAS_SUPPORT_SEVERITY_HIGH_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_TERMS_AND_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    has_auditlog_destination_cloud: bool
    has_auditlog_destination_https_post: bool
    has_auditlog_feature: bool
    has_backup_uploads: bool
    has_multi_region_backup_uploads: bool
    has_private_endpoints: bool
    has_support_plans: bool
    has_support_severity_critical: bool
    has_support_severity_high: bool
    id: str
    name: str
    requires_terms_and_conditions: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., has_support_plans: bool = ..., has_backup_uploads: bool = ..., requires_terms_and_conditions: bool = ..., has_support_severity_high: bool = ..., has_support_severity_critical: bool = ..., has_auditlog_feature: bool = ..., has_auditlog_destination_cloud: bool = ..., has_auditlog_destination_https_post: bool = ..., has_private_endpoints: bool = ..., has_multi_region_backup_uploads: bool = ...) -> None: ...
