from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IPAllowlist(_message.Message):
    __slots__ = ["id", "url", "name", "description", "project_id", "cidr_ranges", "created_at", "deleted_at", "is_deleted", "created_by_id", "locked", "warnings", "remote_inspection_allowed"]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CIDR_RANGES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_INSPECTION_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    project_id: str
    cidr_ranges: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    created_by_id: str
    locked: bool
    warnings: _containers.RepeatedScalarFieldContainer[str]
    remote_inspection_allowed: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., project_id: _Optional[str] = ..., cidr_ranges: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., created_by_id: _Optional[str] = ..., locked: bool = ..., warnings: _Optional[_Iterable[str]] = ..., remote_inspection_allowed: bool = ...) -> None: ...

class IPAllowlistList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[IPAllowlist]
    def __init__(self, items: _Optional[_Iterable[_Union[IPAllowlist, _Mapping]]] = ...) -> None: ...

class IAMProvider(_message.Message):
    __slots__ = ["id", "url", "name", "description", "project_id", "type", "created_at", "deleted_at", "is_deleted", "created_by_id", "is_default", "locked", "ldap_settings"]
    class LDAPSettings(_message.Message):
        __slots__ = ["server", "port", "base_distinguished_name", "bind_distinguished_name", "bind_password", "refresh_rate", "tls_ca_certificate_pem", "serialized", "serialize_timeout_sec", "retries", "restart", "referrals", "timeout_sec", "network_timeout_sec", "async_connect", "prefix", "suffix", "search_scope", "search_filter", "search_attribute", "roles_attribute_name", "roles_search", "roles_include", "roles_exclude", "roles_transformation", "super_user_role"]
        SERVER_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        BASE_DISTINGUISHED_NAME_FIELD_NUMBER: _ClassVar[int]
        BIND_DISTINGUISHED_NAME_FIELD_NUMBER: _ClassVar[int]
        BIND_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        REFRESH_RATE_FIELD_NUMBER: _ClassVar[int]
        TLS_CA_CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
        SERIALIZED_FIELD_NUMBER: _ClassVar[int]
        SERIALIZE_TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
        RETRIES_FIELD_NUMBER: _ClassVar[int]
        RESTART_FIELD_NUMBER: _ClassVar[int]
        REFERRALS_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
        NETWORK_TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
        ASYNC_CONNECT_FIELD_NUMBER: _ClassVar[int]
        PREFIX_FIELD_NUMBER: _ClassVar[int]
        SUFFIX_FIELD_NUMBER: _ClassVar[int]
        SEARCH_SCOPE_FIELD_NUMBER: _ClassVar[int]
        SEARCH_FILTER_FIELD_NUMBER: _ClassVar[int]
        SEARCH_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        ROLES_ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
        ROLES_SEARCH_FIELD_NUMBER: _ClassVar[int]
        ROLES_INCLUDE_FIELD_NUMBER: _ClassVar[int]
        ROLES_EXCLUDE_FIELD_NUMBER: _ClassVar[int]
        ROLES_TRANSFORMATION_FIELD_NUMBER: _ClassVar[int]
        SUPER_USER_ROLE_FIELD_NUMBER: _ClassVar[int]
        server: str
        port: int
        base_distinguished_name: str
        bind_distinguished_name: str
        bind_password: str
        refresh_rate: int
        tls_ca_certificate_pem: str
        serialized: bool
        serialize_timeout_sec: int
        retries: int
        restart: bool
        referrals: bool
        timeout_sec: int
        network_timeout_sec: int
        async_connect: bool
        prefix: str
        suffix: str
        search_scope: str
        search_filter: str
        search_attribute: str
        roles_attribute_name: str
        roles_search: str
        roles_include: str
        roles_exclude: str
        roles_transformation: str
        super_user_role: str
        def __init__(self, server: _Optional[str] = ..., port: _Optional[int] = ..., base_distinguished_name: _Optional[str] = ..., bind_distinguished_name: _Optional[str] = ..., bind_password: _Optional[str] = ..., refresh_rate: _Optional[int] = ..., tls_ca_certificate_pem: _Optional[str] = ..., serialized: bool = ..., serialize_timeout_sec: _Optional[int] = ..., retries: _Optional[int] = ..., restart: bool = ..., referrals: bool = ..., timeout_sec: _Optional[int] = ..., network_timeout_sec: _Optional[int] = ..., async_connect: bool = ..., prefix: _Optional[str] = ..., suffix: _Optional[str] = ..., search_scope: _Optional[str] = ..., search_filter: _Optional[str] = ..., search_attribute: _Optional[str] = ..., roles_attribute_name: _Optional[str] = ..., roles_search: _Optional[str] = ..., roles_include: _Optional[str] = ..., roles_exclude: _Optional[str] = ..., roles_transformation: _Optional[str] = ..., super_user_role: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    LDAP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    project_id: str
    type: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    created_by_id: str
    is_default: bool
    locked: bool
    ldap_settings: IAMProvider.LDAPSettings
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., project_id: _Optional[str] = ..., type: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., created_by_id: _Optional[str] = ..., is_default: bool = ..., locked: bool = ..., ldap_settings: _Optional[_Union[IAMProvider.LDAPSettings, _Mapping]] = ...) -> None: ...

class IAMProviderList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[IAMProvider]
    def __init__(self, items: _Optional[_Iterable[_Union[IAMProvider, _Mapping]]] = ...) -> None: ...
