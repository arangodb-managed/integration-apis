from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from github.com.golang.protobuf.ptypes.duration import duration_pb2 as _duration_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["id", "email", "name", "given_name", "family_name", "created_at", "additional_emails", "mobile_phone", "mobile_phone_verified", "company_name", "dashboard_access_denied", "dashboard_access_denied_reason", "apikey_id", "slack_name", "last_login_at", "last_ip", "mobile_phone_needs_verification", "has_educational_status", "educational_role", "experience", "other_dbs"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_EMAILS_FIELD_NUMBER: _ClassVar[int]
    MOBILE_PHONE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ACCESS_DENIED_REASON_FIELD_NUMBER: _ClassVar[int]
    APIKEY_ID_FIELD_NUMBER: _ClassVar[int]
    SLACK_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_IP_FIELD_NUMBER: _ClassVar[int]
    MOBILE_PHONE_NEEDS_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    HAS_EDUCATIONAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    EDUCATIONAL_ROLE_FIELD_NUMBER: _ClassVar[int]
    EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    OTHER_DBS_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    name: str
    given_name: str
    family_name: str
    created_at: _timestamp_pb2.Timestamp
    additional_emails: _containers.RepeatedScalarFieldContainer[str]
    mobile_phone: str
    mobile_phone_verified: bool
    company_name: str
    dashboard_access_denied: bool
    dashboard_access_denied_reason: str
    apikey_id: str
    slack_name: str
    last_login_at: _timestamp_pb2.Timestamp
    last_ip: str
    mobile_phone_needs_verification: bool
    has_educational_status: bool
    educational_role: str
    experience: str
    other_dbs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., given_name: _Optional[str] = ..., family_name: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., additional_emails: _Optional[_Iterable[str]] = ..., mobile_phone: _Optional[str] = ..., mobile_phone_verified: bool = ..., company_name: _Optional[str] = ..., dashboard_access_denied: bool = ..., dashboard_access_denied_reason: _Optional[str] = ..., apikey_id: _Optional[str] = ..., slack_name: _Optional[str] = ..., last_login_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_ip: _Optional[str] = ..., mobile_phone_needs_verification: bool = ..., has_educational_status: bool = ..., educational_role: _Optional[str] = ..., experience: _Optional[str] = ..., other_dbs: _Optional[_Iterable[str]] = ...) -> None: ...

class VerifyUserMobilePhoneRequest(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ["id", "organization_id", "name", "description", "created_at", "deleted_at", "is_deleted", "url", "is_virtual", "is_default"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    IS_VIRTUAL_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    url: str
    is_virtual: bool
    is_default: bool
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., url: _Optional[str] = ..., is_virtual: bool = ..., is_default: bool = ...) -> None: ...

class GroupList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(self, items: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...) -> None: ...

class IsMemberOfGroupRequest(_message.Message):
    __slots__ = ["user_id", "group_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    group_id: str
    def __init__(self, user_id: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...

class GroupMemberList(_message.Message):
    __slots__ = ["items", "users"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[str]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, items: _Optional[_Iterable[str]] = ..., users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class GroupMembersRequest(_message.Message):
    __slots__ = ["group_id", "user_ids"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetMultipleEffectivePermissionsRequest(_message.Message):
    __slots__ = ["urls"]
    URLS_FIELD_NUMBER: _ClassVar[int]
    urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, urls: _Optional[_Iterable[str]] = ...) -> None: ...

class MultiplePermissionLists(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PermissionList]
    def __init__(self, items: _Optional[_Iterable[_Union[PermissionList, _Mapping]]] = ...) -> None: ...

class PermissionList(_message.Message):
    __slots__ = ["items", "url"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[str]
    url: str
    def __init__(self, items: _Optional[_Iterable[str]] = ..., url: _Optional[str] = ...) -> None: ...

class HasPermissionsRequest(_message.Message):
    __slots__ = ["url", "permissions"]
    URL_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    url: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, url: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ["id", "organization_id", "name", "description", "permissions", "is_predefined", "created_at", "deleted_at", "is_deleted", "url"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    IS_PREDEFINED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    is_predefined: bool
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    url: str
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ..., is_predefined: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., url: _Optional[str] = ...) -> None: ...

class RoleList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Role]
    def __init__(self, items: _Optional[_Iterable[_Union[Role, _Mapping]]] = ...) -> None: ...

class RoleBinding(_message.Message):
    __slots__ = ["id", "member_id", "role_id", "delete_not_allowed"]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_NOT_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    id: str
    member_id: str
    role_id: str
    delete_not_allowed: bool
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., role_id: _Optional[str] = ..., delete_not_allowed: bool = ...) -> None: ...

class GetPolicyByFilterRequest(_message.Message):
    __slots__ = ["resource_url", "options", "member_id", "role_id"]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_url: str
    options: _common_pb2.ListOptions
    member_id: str
    role_id: str
    def __init__(self, resource_url: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., member_id: _Optional[str] = ..., role_id: _Optional[str] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ["resource_url", "bindings"]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    resource_url: str
    bindings: _containers.RepeatedCompositeFieldContainer[RoleBinding]
    def __init__(self, resource_url: _Optional[str] = ..., bindings: _Optional[_Iterable[_Union[RoleBinding, _Mapping]]] = ...) -> None: ...

class RoleBindingsRequest(_message.Message):
    __slots__ = ["resource_url", "bindings"]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    resource_url: str
    bindings: _containers.RepeatedCompositeFieldContainer[RoleBinding]
    def __init__(self, resource_url: _Optional[str] = ..., bindings: _Optional[_Iterable[_Union[RoleBinding, _Mapping]]] = ...) -> None: ...

class APIKey(_message.Message):
    __slots__ = ["id", "url", "user_id", "organization_id", "is_readonly", "created_at", "expires_at", "is_expired", "revoked_at", "is_revoked"]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    user_id: str
    organization_id: str
    is_readonly: bool
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    is_expired: bool
    revoked_at: _timestamp_pb2.Timestamp
    is_revoked: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., user_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., is_readonly: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_expired: bool = ..., revoked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_revoked: bool = ...) -> None: ...

class APIKeyList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[APIKey]
    def __init__(self, items: _Optional[_Iterable[_Union[APIKey, _Mapping]]] = ...) -> None: ...

class CreateAPIKeyRequest(_message.Message):
    __slots__ = ["organization_id", "readonly", "time_to_live"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    readonly: bool
    time_to_live: _duration_pb2.Duration
    def __init__(self, organization_id: _Optional[str] = ..., readonly: bool = ..., time_to_live: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class APIKeySecret(_message.Message):
    __slots__ = ["id", "secret"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    id: str
    secret: str
    def __init__(self, id: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class AuthenticateAPIKeyRequest(_message.Message):
    __slots__ = ["id", "secret", "time_to_live"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    secret: str
    time_to_live: _duration_pb2.Duration
    def __init__(self, id: _Optional[str] = ..., secret: _Optional[str] = ..., time_to_live: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class AuthenticateAPIKeyResponse(_message.Message):
    __slots__ = ["token", "time_to_live"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_FIELD_NUMBER: _ClassVar[int]
    token: str
    time_to_live: _duration_pb2.Duration
    def __init__(self, token: _Optional[str] = ..., time_to_live: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class RenewAPIKeyTokenRequest(_message.Message):
    __slots__ = ["token", "time_to_live"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_FIELD_NUMBER: _ClassVar[int]
    token: str
    time_to_live: _duration_pb2.Duration
    def __init__(self, token: _Optional[str] = ..., time_to_live: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class RenewAPIKeyTokenResponse(_message.Message):
    __slots__ = ["time_to_live"]
    TIME_TO_LIVE_FIELD_NUMBER: _ClassVar[int]
    time_to_live: _duration_pb2.Duration
    def __init__(self, time_to_live: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class RevokeAPIKeyTokenRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
