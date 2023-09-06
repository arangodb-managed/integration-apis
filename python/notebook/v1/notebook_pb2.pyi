from common.v1 import common_pb2 as _common_pb2
from data.v1 import data_pb2 as _data_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotebookList(_message.Message):
    __slots__ = ["items", "budget"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Notebook]
    budget: _common_pb2.Budget
    def __init__(self, items: _Optional[_Iterable[_Union[Notebook, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class ListNotebooksRequest(_message.Message):
    __slots__ = ["deployment_id", "options"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    options: _common_pb2.ListOptions
    def __init__(self, deployment_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class Notebook(_message.Message):
    __slots__ = ["id", "deployment_id", "url", "name", "description", "is_paused", "last_paused_at", "last_resumed_at", "created_by_id", "created_at", "model", "is_deleted", "deleted_at", "ml_enabled", "status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    LAST_PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RESUMED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    ML_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    deployment_id: str
    url: str
    name: str
    description: str
    is_paused: bool
    last_paused_at: _timestamp_pb2.Timestamp
    last_resumed_at: _timestamp_pb2.Timestamp
    created_by_id: str
    created_at: _timestamp_pb2.Timestamp
    model: ModelSpec
    is_deleted: bool
    deleted_at: _timestamp_pb2.Timestamp
    ml_enabled: bool
    status: Status
    def __init__(self, id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_paused: bool = ..., last_paused_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_resumed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., model: _Optional[_Union[ModelSpec, _Mapping]] = ..., is_deleted: bool = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ml_enabled: bool = ..., status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ModelSpec(_message.Message):
    __slots__ = ["notebook_model_id", "disk_size"]
    NOTEBOOK_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    notebook_model_id: str
    disk_size: int
    def __init__(self, notebook_model_id: _Optional[str] = ..., disk_size: _Optional[int] = ...) -> None: ...

class NotebookModel(_message.Message):
    __slots__ = ["id", "name", "cpu", "memory", "max_disk_size", "min_disk_size", "gpu"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIN_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    GPU_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    cpu: float
    memory: int
    max_disk_size: int
    min_disk_size: int
    gpu: float
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., cpu: _Optional[float] = ..., memory: _Optional[int] = ..., max_disk_size: _Optional[int] = ..., min_disk_size: _Optional[int] = ..., gpu: _Optional[float] = ...) -> None: ...

class NotebookModelList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[NotebookModel]
    def __init__(self, items: _Optional[_Iterable[_Union[NotebookModel, _Mapping]]] = ...) -> None: ...

class ListNotebookModelsRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["phase", "message", "last_updated_at", "endpoint", "last_active_at", "usage"]
    class Usage(_message.Message):
        __slots__ = ["data_volume_info", "last_memory_usage", "last_cpu_usage", "last_memory_limit", "last_cpu_limit", "last_gpu_usage", "last_gpu_limit"]
        DATA_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        LAST_GPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_GPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        data_volume_info: _data_pb2.DataVolumeInfo
        last_memory_usage: int
        last_cpu_usage: float
        last_memory_limit: int
        last_cpu_limit: float
        last_gpu_usage: float
        last_gpu_limit: float
        def __init__(self, data_volume_info: _Optional[_Union[_data_pb2.DataVolumeInfo, _Mapping]] = ..., last_memory_usage: _Optional[int] = ..., last_cpu_usage: _Optional[float] = ..., last_memory_limit: _Optional[int] = ..., last_cpu_limit: _Optional[float] = ..., last_gpu_usage: _Optional[float] = ..., last_gpu_limit: _Optional[float] = ...) -> None: ...
    PHASE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    phase: str
    message: str
    last_updated_at: _timestamp_pb2.Timestamp
    endpoint: str
    last_active_at: _timestamp_pb2.Timestamp
    usage: Status.Usage
    def __init__(self, phase: _Optional[str] = ..., message: _Optional[str] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endpoint: _Optional[str] = ..., last_active_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., usage: _Optional[_Union[Status.Usage, _Mapping]] = ...) -> None: ...
