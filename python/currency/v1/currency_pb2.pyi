from common.v1 import common_pb2 as _common_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Currency(_message.Message):
    __slots__ = ("id", "name", "sign", "iso4217_code")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIGN_FIELD_NUMBER: _ClassVar[int]
    ISO4217_CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    sign: str
    iso4217_code: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., sign: _Optional[str] = ..., iso4217_code: _Optional[str] = ...) -> None: ...

class CurrencyList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Currency]
    def __init__(self, items: _Optional[_Iterable[_Union[Currency, _Mapping]]] = ...) -> None: ...

class GetDefaultCurrencyRequest(_message.Message):
    __slots__ = ("organization_id",)
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ...) -> None: ...
