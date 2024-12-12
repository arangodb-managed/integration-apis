from common.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDeploymentMetricsRequest(_message.Message):
    __slots__ = ("deployment_id", "start_at", "end_at", "server_type", "metric_type")
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    SERVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    start_at: _timestamp_pb2.Timestamp
    end_at: _timestamp_pb2.Timestamp
    server_type: str
    metric_type: str
    def __init__(self, deployment_id: _Optional[str] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., server_type: _Optional[str] = ..., metric_type: _Optional[str] = ...) -> None: ...

class DeploymentMetrics(_message.Message):
    __slots__ = ("metrics",)
    class Sample(_message.Message):
        __slots__ = ("timestamp", "value")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        value: float
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...
    class Timeseries(_message.Message):
        __slots__ = ("server_id", "samples")
        SERVER_ID_FIELD_NUMBER: _ClassVar[int]
        SAMPLES_FIELD_NUMBER: _ClassVar[int]
        server_id: str
        samples: _containers.RepeatedCompositeFieldContainer[DeploymentMetrics.Sample]
        def __init__(self, server_id: _Optional[str] = ..., samples: _Optional[_Iterable[_Union[DeploymentMetrics.Sample, _Mapping]]] = ...) -> None: ...
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[DeploymentMetrics.Timeseries]
    def __init__(self, metrics: _Optional[_Iterable[_Union[DeploymentMetrics.Timeseries, _Mapping]]] = ...) -> None: ...

class GetDeploymentLogsRequest(_message.Message):
    __slots__ = ("deployment_id", "role", "format", "server_id", "start_at", "end_at", "limit")
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    role: str
    format: str
    server_id: str
    start_at: _timestamp_pb2.Timestamp
    end_at: _timestamp_pb2.Timestamp
    limit: int
    def __init__(self, deployment_id: _Optional[str] = ..., role: _Optional[str] = ..., format: _Optional[str] = ..., server_id: _Optional[str] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class DeploymentLogsChunk(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...
