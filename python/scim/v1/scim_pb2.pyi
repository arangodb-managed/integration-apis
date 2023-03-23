from common.v1 import common_pb2 as _common_pb2
from iam.v1 import iam_pb2 as _iam_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListUserResponse(_message.Message):
    __slots__ = ["Resources", "count", "schemas", "startIndex", "totalResult"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    Resources: _containers.RepeatedCompositeFieldContainer[User]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    STARTINDEX_FIELD_NUMBER: _ClassVar[int]
    TOTALRESULT_FIELD_NUMBER: _ClassVar[int]
    count: int
    schemas: _containers.RepeatedScalarFieldContainer[str]
    startIndex: int
    totalResult: int
    def __init__(self, schemas: _Optional[_Iterable[str]] = ..., totalResult: _Optional[int] = ..., startIndex: _Optional[int] = ..., count: _Optional[int] = ..., Resources: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ["count", "filter", "startIndex"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    STARTINDEX_FIELD_NUMBER: _ClassVar[int]
    count: int
    filter: str
    startIndex: int
    def __init__(self, startIndex: _Optional[int] = ..., count: _Optional[int] = ..., filter: _Optional[str] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["created", "lastModified", "resourceType"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIED_FIELD_NUMBER: _ClassVar[int]
    RESOURCETYPE_FIELD_NUMBER: _ClassVar[int]
    created: _timestamp_pb2.Timestamp
    lastModified: _timestamp_pb2.Timestamp
    resourceType: str
    def __init__(self, resourceType: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lastModified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["active", "displayName", "emails", "externalId", "id", "locale", "meta", "name", "nickName", "photos", "schemas", "userName"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    EXTERNALID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    active: bool
    displayName: str
    emails: _containers.RepeatedCompositeFieldContainer[UserResource]
    externalId: str
    id: str
    locale: str
    meta: Metadata
    name: UserName
    nickName: str
    photos: _containers.RepeatedCompositeFieldContainer[UserResource]
    schemas: _containers.RepeatedScalarFieldContainer[str]
    userName: str
    def __init__(self, schemas: _Optional[_Iterable[str]] = ..., id: _Optional[str] = ..., displayName: _Optional[str] = ..., nickName: _Optional[str] = ..., locale: _Optional[str] = ..., name: _Optional[_Union[UserName, _Mapping]] = ..., emails: _Optional[_Iterable[_Union[UserResource, _Mapping]]] = ..., photos: _Optional[_Iterable[_Union[UserResource, _Mapping]]] = ..., meta: _Optional[_Union[Metadata, _Mapping]] = ..., externalId: _Optional[str] = ..., active: bool = ..., userName: _Optional[str] = ...) -> None: ...

class UserName(_message.Message):
    __slots__ = ["familyName", "formatted", "givenName"]
    FAMILYNAME_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_FIELD_NUMBER: _ClassVar[int]
    GIVENNAME_FIELD_NUMBER: _ClassVar[int]
    familyName: str
    formatted: str
    givenName: str
    def __init__(self, formatted: _Optional[str] = ..., givenName: _Optional[str] = ..., familyName: _Optional[str] = ...) -> None: ...

class UserResource(_message.Message):
    __slots__ = ["primary", "type", "value"]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    primary: bool
    type: str
    value: str
    def __init__(self, value: _Optional[str] = ..., primary: bool = ..., type: _Optional[str] = ...) -> None: ...
