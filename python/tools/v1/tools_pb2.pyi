from google.api import annotations_pb2 as _annotations_pb2
from common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToolsVersion(_message.Message):
    __slots__ = ("latest_version", "download_url", "is_compatible")
    LATEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    IS_COMPATIBLE_FIELD_NUMBER: _ClassVar[int]
    latest_version: str
    download_url: str
    is_compatible: bool
    def __init__(self, latest_version: _Optional[str] = ..., download_url: _Optional[str] = ..., is_compatible: bool = ...) -> None: ...

class GetLatestVersionRequest(_message.Message):
    __slots__ = ("name", "expected_api_versions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_API_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    expected_api_versions: _containers.RepeatedCompositeFieldContainer[APIVersionPair]
    def __init__(self, name: _Optional[str] = ..., expected_api_versions: _Optional[_Iterable[_Union[APIVersionPair, _Mapping]]] = ...) -> None: ...

class APIVersionPair(_message.Message):
    __slots__ = ("api_id", "version")
    API_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    api_id: str
    version: _common_pb2.Version
    def __init__(self, api_id: _Optional[str] = ..., version: _Optional[_Union[_common_pb2.Version, _Mapping]] = ...) -> None: ...
