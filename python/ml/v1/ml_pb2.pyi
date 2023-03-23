from common.v1 import common_pb2 as _common_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MLServices(_message.Message):
    __slots__ = ["deployment_id", "enabled"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    enabled: bool
    def __init__(self, deployment_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...
