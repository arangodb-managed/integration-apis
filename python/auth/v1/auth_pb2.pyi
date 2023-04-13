from common.v1 import common_pb2 as _common_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizeRequest(_message.Message):
    __slots__ = ["callback_url", "resource_id", "resource_type"]
    CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    callback_url: str
    resource_id: str
    resource_type: str
    def __init__(self, resource_id: _Optional[str] = ..., resource_type: _Optional[str] = ..., callback_url: _Optional[str] = ...) -> None: ...
