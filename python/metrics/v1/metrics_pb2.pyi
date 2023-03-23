from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.duration import duration_pb2 as _duration_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMetricsEndpointRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class ListTokensRequest(_message.Message):
    __slots__ = ["deployment_id", "exclude_deleted", "exclude_expired", "exclude_revoked", "options"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_REVOKED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    exclude_deleted: bool
    exclude_expired: bool
    exclude_revoked: bool
    options: _common_pb2.ListOptions
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., deployment_id: _Optional[str] = ..., exclude_revoked: bool = ..., exclude_expired: bool = ..., exclude_deleted: bool = ...) -> None: ...

class MetricsEndpoint(_message.Message):
    __slots__ = ["endpoint"]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    def __init__(self, endpoint: _Optional[str] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ["created_at", "deleted_at", "deployment_id", "description", "expires_at", "id", "is_deleted", "is_expired", "is_revoked", "lifetime", "name", "token", "url", "will_expire_soon"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    IS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    WILL_EXPIRE_SOON_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    deployment_id: str
    description: str
    expires_at: _timestamp_pb2.Timestamp
    id: str
    is_deleted: bool
    is_expired: bool
    is_revoked: bool
    lifetime: _duration_pb2.Duration
    name: str
    token: str
    url: str
    will_expire_soon: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., deployment_id: _Optional[str] = ..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., token: _Optional[str] = ..., is_deleted: bool = ..., is_expired: bool = ..., will_expire_soon: bool = ..., is_revoked: bool = ...) -> None: ...

class TokenList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Token]
    def __init__(self, items: _Optional[_Iterable[_Union[Token, _Mapping]]] = ...) -> None: ...
