from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DEFAULT_PROFILE_FIELD_NUMBER: _ClassVar[int]
DESCRIPTOR: _descriptor.FileDescriptor
PROFILE_FIELD_NUMBER: _ClassVar[int]
default_profile: _descriptor.FieldDescriptor
profile: _descriptor.FieldDescriptor

class MethodProfile(_message.Message):
    __slots__ = ["retryable", "timeout"]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    retryable: bool
    timeout: int
    def __init__(self, timeout: _Optional[int] = ..., retryable: bool = ...) -> None: ...

class ServiceProfile(_message.Message):
    __slots__ = ["timeout"]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    timeout: int
    def __init__(self, timeout: _Optional[int] = ...) -> None: ...
