from common.v1 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Token(_message.Message):
    __slots__ = ("id", "url", "name", "description", "deployment_id", "lifetime", "created_at", "deleted_at", "expires_at", "token", "is_deleted", "is_expired", "will_expire_soon", "is_revoked")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    WILL_EXPIRE_SOON_FIELD_NUMBER: _ClassVar[int]
    IS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    deployment_id: str
    lifetime: _duration_pb2.Duration
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    token: str
    is_deleted: bool
    is_expired: bool
    will_expire_soon: bool
    is_revoked: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., deployment_id: _Optional[str] = ..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., token: _Optional[str] = ..., is_deleted: bool = ..., is_expired: bool = ..., will_expire_soon: bool = ..., is_revoked: bool = ...) -> None: ...

class TokenList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Token]
    def __init__(self, items: _Optional[_Iterable[_Union[Token, _Mapping]]] = ...) -> None: ...

class ListTokensRequest(_message.Message):
    __slots__ = ("options", "deployment_id", "exclude_revoked", "exclude_expired", "exclude_deleted")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_REVOKED_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    deployment_id: str
    exclude_revoked: bool
    exclude_expired: bool
    exclude_deleted: bool
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., deployment_id: _Optional[str] = ..., exclude_revoked: bool = ..., exclude_expired: bool = ..., exclude_deleted: bool = ...) -> None: ...

class GetMetricsEndpointRequest(_message.Message):
    __slots__ = ("deployment_id",)
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class MetricsEndpoint(_message.Message):
    __slots__ = ("endpoint", "endpoint_self_signed", "endpoint_default")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_SELF_SIGNED_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    endpoint_self_signed: str
    endpoint_default: str
    def __init__(self, endpoint: _Optional[str] = ..., endpoint_self_signed: _Optional[str] = ..., endpoint_default: _Optional[str] = ...) -> None: ...
