from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentProfile(_message.Message):
    __slots__ = ["created_at", "description", "id", "name", "organization_id", "url"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    description: str
    id: str
    name: str
    organization_id: str
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeploymentProfileList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DeploymentProfile]
    def __init__(self, items: _Optional[_Iterable[_Union[DeploymentProfile, _Mapping]]] = ...) -> None: ...

class ListDeploymentProfilesRequest(_message.Message):
    __slots__ = ["options", "organization_id"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...
