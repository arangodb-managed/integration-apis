from common.v1 import common_pb2 as _common_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Provider(_message.Message):
    __slots__ = ["id", "name", "prerelease"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRERELEASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    prerelease: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., prerelease: bool = ...) -> None: ...

class ProviderList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Provider]
    def __init__(self, items: _Optional[_Iterable[_Union[Provider, _Mapping]]] = ...) -> None: ...

class ListProvidersRequest(_message.Message):
    __slots__ = ["options", "organization_id"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class Region(_message.Message):
    __slots__ = ["id", "provider_id", "location", "available", "low_stock", "out_of_stock", "prerelease"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    LOW_STOCK_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_STOCK_FIELD_NUMBER: _ClassVar[int]
    PRERELEASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    provider_id: str
    location: str
    available: bool
    low_stock: bool
    out_of_stock: bool
    prerelease: bool
    def __init__(self, id: _Optional[str] = ..., provider_id: _Optional[str] = ..., location: _Optional[str] = ..., available: bool = ..., low_stock: bool = ..., out_of_stock: bool = ..., prerelease: bool = ...) -> None: ...

class RegionList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Region]
    def __init__(self, items: _Optional[_Iterable[_Union[Region, _Mapping]]] = ...) -> None: ...

class ListRegionsRequest(_message.Message):
    __slots__ = ["options", "provider_id", "organization_id"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    provider_id: str
    organization_id: str
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., provider_id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...
