from common.v1 import common_pb2 as _common_pb2
from data.v1 import data_pb2 as _data_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListNotebookModelsRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class ListNotebooksRequest(_message.Message):
    __slots__ = ["deployment_id", "options"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    options: _common_pb2.ListOptions
    def __init__(self, deployment_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class ModelSpec(_message.Message):
    __slots__ = ["disk_size", "notebook_model_id"]
    DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    disk_size: int
    notebook_model_id: str
    def __init__(self, notebook_model_id: _Optional[str] = ..., disk_size: _Optional[int] = ...) -> None: ...

class Notebook(_message.Message):
    __slots__ = ["created_at", "created_by_id", "deleted_at", "deployment_id", "description", "id", "is_deleted", "is_paused", "last_paused_at", "last_resumed_at", "model", "name", "status", "url"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    LAST_PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RESUMED_AT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    created_by_id: str
    deleted_at: _timestamp_pb2.Timestamp
    deployment_id: str
    description: str
    id: str
    is_deleted: bool
    is_paused: bool
    last_paused_at: _timestamp_pb2.Timestamp
    last_resumed_at: _timestamp_pb2.Timestamp
    model: ModelSpec
    name: str
    status: Status
    url: str
    def __init__(self, id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_paused: bool = ..., last_paused_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_resumed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., model: _Optional[_Union[ModelSpec, _Mapping]] = ..., is_deleted: bool = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class NotebookList(_message.Message):
    __slots__ = ["budget", "items"]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    budget: _common_pb2.Budget
    items: _containers.RepeatedCompositeFieldContainer[Notebook]
    def __init__(self, items: _Optional[_Iterable[_Union[Notebook, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class NotebookModel(_message.Message):
    __slots__ = ["cpu", "id", "max_disk_size", "memory", "min_disk_size", "name"]
    CPU_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    MIN_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    cpu: float
    id: str
    max_disk_size: int
    memory: int
    min_disk_size: int
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., cpu: _Optional[float] = ..., memory: _Optional[int] = ..., max_disk_size: _Optional[int] = ..., min_disk_size: _Optional[int] = ...) -> None: ...

class NotebookModelList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[NotebookModel]
    def __init__(self, items: _Optional[_Iterable[_Union[NotebookModel, _Mapping]]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["endpoint", "last_updated_at", "message", "phase", "usage"]
    class Usage(_message.Message):
        __slots__ = ["data_volume_info", "last_cpu_limit", "last_cpu_usage", "last_memory_limit", "last_memory_usage"]
        DATA_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        data_volume_info: _data_pb2.DataVolumeInfo
        last_cpu_limit: float
        last_cpu_usage: float
        last_memory_limit: int
        last_memory_usage: int
        def __init__(self, data_volume_info: _Optional[_Union[_data_pb2.DataVolumeInfo, _Mapping]] = ..., last_memory_usage: _Optional[int] = ..., last_cpu_usage: _Optional[float] = ..., last_memory_limit: _Optional[int] = ..., last_cpu_limit: _Optional[float] = ...) -> None: ...
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    last_updated_at: _timestamp_pb2.Timestamp
    message: str
    phase: str
    usage: Status.Usage
    def __init__(self, phase: _Optional[str] = ..., message: _Optional[str] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endpoint: _Optional[str] = ..., usage: _Optional[_Union[Status.Usage, _Mapping]] = ...) -> None: ...
