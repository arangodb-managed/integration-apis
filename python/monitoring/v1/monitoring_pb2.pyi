from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentLogsChunk(_message.Message):
    __slots__ = ["chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class GetDeploymentLogsRequest(_message.Message):
    __slots__ = ["deployment_id", "end_at", "format", "limit", "role", "server_id", "start_at"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    end_at: _timestamp_pb2.Timestamp
    format: str
    limit: int
    role: str
    server_id: str
    start_at: _timestamp_pb2.Timestamp
    def __init__(self, deployment_id: _Optional[str] = ..., role: _Optional[str] = ..., format: _Optional[str] = ..., server_id: _Optional[str] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...
