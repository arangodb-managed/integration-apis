from common.v1 import common_pb2 as _common_pb2
from iam.v1 import iam_pb2 as _iam_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_SEVERITY_INFO: _ClassVar[NotificationSeverity]
    NOTIFICATION_SEVERITY_WARNING: _ClassVar[NotificationSeverity]
    NOTIFICATION_SEVERITY_CRITICAL: _ClassVar[NotificationSeverity]
NOTIFICATION_SEVERITY_INFO: NotificationSeverity
NOTIFICATION_SEVERITY_WARNING: NotificationSeverity
NOTIFICATION_SEVERITY_CRITICAL: NotificationSeverity

class Organization(_message.Message):
    __slots__ = ("id", "url", "name", "description", "is_deleted", "created_at", "deleted_at", "tier", "total_deployments", "is_flexible_deployments_enabled", "is_allowed_to_use_custom_images", "is_allowed_to_use_iamproviders", "locked", "requires_prepaid_deployments", "authentication_providers", "email_domain_restrictions", "is_allowed_to_use_scim", "notifications")
    class TotalDeploymentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class NotificationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Notification
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Notification, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    IS_FLEXIBLE_DEPLOYMENTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_TO_USE_CUSTOM_IMAGES_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_TO_USE_IAMPROVIDERS_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_PREPAID_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DOMAIN_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_TO_USE_SCIM_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    tier: Tier
    total_deployments: _containers.ScalarMap[str, int]
    is_flexible_deployments_enabled: bool
    is_allowed_to_use_custom_images: bool
    is_allowed_to_use_iamproviders: bool
    locked: bool
    requires_prepaid_deployments: bool
    authentication_providers: AuthenticationProviders
    email_domain_restrictions: DomainRestrictions
    is_allowed_to_use_scim: bool
    notifications: _containers.MessageMap[str, Notification]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tier: _Optional[_Union[Tier, _Mapping]] = ..., total_deployments: _Optional[_Mapping[str, int]] = ..., is_flexible_deployments_enabled: bool = ..., is_allowed_to_use_custom_images: bool = ..., is_allowed_to_use_iamproviders: bool = ..., locked: bool = ..., requires_prepaid_deployments: bool = ..., authentication_providers: _Optional[_Union[AuthenticationProviders, _Mapping]] = ..., email_domain_restrictions: _Optional[_Union[DomainRestrictions, _Mapping]] = ..., is_allowed_to_use_scim: bool = ..., notifications: _Optional[_Mapping[str, Notification]] = ...) -> None: ...

class OrganizationList(_message.Message):
    __slots__ = ("items", "budget")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Organization]
    budget: _common_pb2.Budget
    def __init__(self, items: _Optional[_Iterable[_Union[Organization, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class AuthenticationProviders(_message.Message):
    __slots__ = ("enable_username_password", "enable_google", "enable_github", "enable_microsoft", "enable_sso")
    ENABLE_USERNAME_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_GOOGLE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_GITHUB_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MICROSOFT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SSO_FIELD_NUMBER: _ClassVar[int]
    enable_username_password: bool
    enable_google: bool
    enable_github: bool
    enable_microsoft: bool
    enable_sso: bool
    def __init__(self, enable_username_password: bool = ..., enable_google: bool = ..., enable_github: bool = ..., enable_microsoft: bool = ..., enable_sso: bool = ...) -> None: ...

class DomainRestrictions(_message.Message):
    __slots__ = ("allowed_domains",)
    ALLOWED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    allowed_domains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowed_domains: _Optional[_Iterable[str]] = ...) -> None: ...

class Tier(_message.Message):
    __slots__ = ("id", "name", "has_support_plans", "has_backup_uploads", "requires_terms_and_conditions", "has_support_severity_high", "has_support_severity_critical", "has_auditlog_feature", "has_auditlog_destination_cloud", "has_auditlog_destination_https_post", "has_private_endpoints", "has_multi_region_backup_uploads")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HAS_SUPPORT_PLANS_FIELD_NUMBER: _ClassVar[int]
    HAS_BACKUP_UPLOADS_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_TERMS_AND_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_SUPPORT_SEVERITY_HIGH_FIELD_NUMBER: _ClassVar[int]
    HAS_SUPPORT_SEVERITY_CRITICAL_FIELD_NUMBER: _ClassVar[int]
    HAS_AUDITLOG_FEATURE_FIELD_NUMBER: _ClassVar[int]
    HAS_AUDITLOG_DESTINATION_CLOUD_FIELD_NUMBER: _ClassVar[int]
    HAS_AUDITLOG_DESTINATION_HTTPS_POST_FIELD_NUMBER: _ClassVar[int]
    HAS_PRIVATE_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    HAS_MULTI_REGION_BACKUP_UPLOADS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    has_support_plans: bool
    has_backup_uploads: bool
    requires_terms_and_conditions: bool
    has_support_severity_high: bool
    has_support_severity_critical: bool
    has_auditlog_feature: bool
    has_auditlog_destination_cloud: bool
    has_auditlog_destination_https_post: bool
    has_private_endpoints: bool
    has_multi_region_backup_uploads: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., has_support_plans: bool = ..., has_backup_uploads: bool = ..., requires_terms_and_conditions: bool = ..., has_support_severity_high: bool = ..., has_support_severity_critical: bool = ..., has_auditlog_feature: bool = ..., has_auditlog_destination_cloud: bool = ..., has_auditlog_destination_https_post: bool = ..., has_private_endpoints: bool = ..., has_multi_region_backup_uploads: bool = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ("user_id", "owner", "user")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    owner: bool
    user: _iam_pb2.User
    def __init__(self, user_id: _Optional[str] = ..., owner: bool = ..., user: _Optional[_Union[_iam_pb2.User, _Mapping]] = ...) -> None: ...

class MemberList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, items: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class IsMemberOfOrganizationRequest(_message.Message):
    __slots__ = ("user_id", "organization_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    organization_id: str
    def __init__(self, user_id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class IsMemberOfOrganizationResponse(_message.Message):
    __slots__ = ("member", "owner")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    member: bool
    owner: bool
    def __init__(self, member: bool = ..., owner: bool = ...) -> None: ...

class OrganizationMembersRequest(_message.Message):
    __slots__ = ("organization_id", "members")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    members: MemberList
    def __init__(self, organization_id: _Optional[str] = ..., members: _Optional[_Union[MemberList, _Mapping]] = ...) -> None: ...

class Project(_message.Message):
    __slots__ = ("id", "url", "name", "description", "organization_id", "is_deleted", "created_at", "deleted_at", "is_flexible_deployments_enabled", "locked")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_FLEXIBLE_DEPLOYMENTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    organization_id: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_flexible_deployments_enabled: bool
    locked: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_flexible_deployments_enabled: bool = ..., locked: bool = ...) -> None: ...

class ProjectList(_message.Message):
    __slots__ = ("items", "budget")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Project]
    budget: _common_pb2.Budget
    def __init__(self, items: _Optional[_Iterable[_Union[Project, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("id", "url", "organization_id", "subject_id", "type", "payload", "created_at", "subject_url", "volatile", "created_by_id", "reason", "status_only", "created_with")
    class PayloadEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_URL_FIELD_NUMBER: _ClassVar[int]
    VOLATILE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    STATUS_ONLY_FIELD_NUMBER: _ClassVar[int]
    CREATED_WITH_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    organization_id: str
    subject_id: str
    type: str
    payload: _containers.ScalarMap[str, str]
    created_at: _timestamp_pb2.Timestamp
    subject_url: str
    volatile: bool
    created_by_id: str
    reason: str
    status_only: bool
    created_with: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., subject_id: _Optional[str] = ..., type: _Optional[str] = ..., payload: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., subject_url: _Optional[str] = ..., volatile: bool = ..., created_by_id: _Optional[str] = ..., reason: _Optional[str] = ..., status_only: bool = ..., created_with: _Optional[str] = ...) -> None: ...

class EventList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, items: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class ListEventOptions(_message.Message):
    __slots__ = ("options", "subject_ids", "types", "created_after", "created_before", "sort_descending")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    SORT_DESCENDING_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    subject_ids: _containers.RepeatedScalarFieldContainer[str]
    types: _containers.RepeatedScalarFieldContainer[str]
    created_after: _timestamp_pb2.Timestamp
    created_before: _timestamp_pb2.Timestamp
    sort_descending: bool
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., subject_ids: _Optional[_Iterable[str]] = ..., types: _Optional[_Iterable[str]] = ..., created_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sort_descending: bool = ...) -> None: ...

class OrganizationInvite(_message.Message):
    __slots__ = ("id", "url", "organization_id", "email", "accepted", "rejected", "created_at", "accepted_at", "rejected_at", "user_id", "created_by_id", "organization_name", "created_by_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_AT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    organization_id: str
    email: str
    accepted: bool
    rejected: bool
    created_at: _timestamp_pb2.Timestamp
    accepted_at: _timestamp_pb2.Timestamp
    rejected_at: _timestamp_pb2.Timestamp
    user_id: str
    created_by_id: str
    organization_name: str
    created_by_name: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., email: _Optional[str] = ..., accepted: bool = ..., rejected: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., accepted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., created_by_id: _Optional[str] = ..., organization_name: _Optional[str] = ..., created_by_name: _Optional[str] = ...) -> None: ...

class OrganizationInviteList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[OrganizationInvite]
    def __init__(self, items: _Optional[_Iterable[_Union[OrganizationInvite, _Mapping]]] = ...) -> None: ...

class QuotaDescription(_message.Message):
    __slots__ = ("kind", "description", "for_organizations", "for_projects")
    KIND_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FOR_ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    FOR_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    description: str
    for_organizations: bool
    for_projects: bool
    def __init__(self, kind: _Optional[str] = ..., description: _Optional[str] = ..., for_organizations: bool = ..., for_projects: bool = ...) -> None: ...

class QuotaDescriptionList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[QuotaDescription]
    def __init__(self, items: _Optional[_Iterable[_Union[QuotaDescription, _Mapping]]] = ...) -> None: ...

class Quota(_message.Message):
    __slots__ = ("kind", "description", "limit")
    KIND_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    kind: str
    description: str
    limit: int
    def __init__(self, kind: _Optional[str] = ..., description: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class QuotaList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Quota]
    def __init__(self, items: _Optional[_Iterable[_Union[Quota, _Mapping]]] = ...) -> None: ...

class ListQuotasRequest(_message.Message):
    __slots__ = ("options", "kinds")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    KINDS_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    kinds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., kinds: _Optional[_Iterable[str]] = ...) -> None: ...

class TermsAndConditions(_message.Message):
    __slots__ = ("id", "content", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DataProcessingAddendum(_message.Message):
    __slots__ = ("id", "content", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Notification(_message.Message):
    __slots__ = ("notification", "severity", "created_at", "updated_at", "expires_at")
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    notification: str
    severity: NotificationSeverity
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, notification: _Optional[str] = ..., severity: _Optional[_Union[NotificationSeverity, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
