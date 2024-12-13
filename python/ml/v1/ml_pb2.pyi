from common.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MLServicesSizeList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[MLServicesSize]
    def __init__(self, items: _Optional[_Iterable[_Union[MLServicesSize, _Mapping]]] = ...) -> None: ...

class ListMLServicesSizesRequest(_message.Message):
    __slots__ = ("deployment_id",)
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class MLServicesSize(_message.Message):
    __slots__ = ("size_id", "is_default", "cpu", "memory", "gpu")
    SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    size_id: str
    is_default: bool
    cpu: float
    memory: int
    gpu: float
    def __init__(self, size_id: _Optional[str] = ..., is_default: bool = ..., cpu: _Optional[float] = ..., memory: _Optional[int] = ..., gpu: _Optional[float] = ...) -> None: ...

class MLServices(_message.Message):
    __slots__ = ("deployment_id", "enabled", "size", "created_at", "status")
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    enabled: bool
    size: str
    created_at: _timestamp_pb2.Timestamp
    status: Status
    def __init__(self, deployment_id: _Optional[str] = ..., enabled: bool = ..., size: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("phase", "message", "last_updated_at", "services", "hours_used", "hours_allowed", "expires_at", "last_enabled_at")
    PHASE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    HOURS_USED_FIELD_NUMBER: _ClassVar[int]
    HOURS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ENABLED_AT_FIELD_NUMBER: _ClassVar[int]
    phase: str
    message: str
    last_updated_at: _timestamp_pb2.Timestamp
    services: _containers.RepeatedCompositeFieldContainer[ServiceStatus]
    hours_used: float
    hours_allowed: float
    expires_at: _timestamp_pb2.Timestamp
    last_enabled_at: _timestamp_pb2.Timestamp
    def __init__(self, phase: _Optional[str] = ..., message: _Optional[str] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., services: _Optional[_Iterable[_Union[ServiceStatus, _Mapping]]] = ..., hours_used: _Optional[float] = ..., hours_allowed: _Optional[float] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_enabled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ServiceStatus(_message.Message):
    __slots__ = ("type", "available", "failed", "usage", "replicas")
    class Usage(_message.Message):
        __slots__ = ("last_memory_usage", "last_cpu_usage", "last_memory_limit", "last_cpu_limit")
        LAST_MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        last_memory_usage: int
        last_cpu_usage: float
        last_memory_limit: int
        last_cpu_limit: float
        def __init__(self, last_memory_usage: _Optional[int] = ..., last_cpu_usage: _Optional[float] = ..., last_memory_limit: _Optional[int] = ..., last_cpu_limit: _Optional[float] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    type: str
    available: bool
    failed: bool
    usage: ServiceStatus.Usage
    replicas: int
    def __init__(self, type: _Optional[str] = ..., available: bool = ..., failed: bool = ..., usage: _Optional[_Union[ServiceStatus.Usage, _Mapping]] = ..., replicas: _Optional[int] = ...) -> None: ...
