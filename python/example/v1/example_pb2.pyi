from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExampleDataset(_message.Message):
    __slots__ = ["id", "url", "name", "description", "guide", "created_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GUIDE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    guide: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., guide: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExampleDatasetInstallation(_message.Message):
    __slots__ = ["id", "url", "deployment_id", "exampledataset_id", "created_at", "deleted_at", "is_deleted", "status"]
    class Status(_message.Message):
        __slots__ = ["database_name", "state", "is_failed", "is_available", "user_name", "demo_url"]
        DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        IS_FAILED_FIELD_NUMBER: _ClassVar[int]
        IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        DEMO_URL_FIELD_NUMBER: _ClassVar[int]
        database_name: str
        state: str
        is_failed: bool
        is_available: bool
        user_name: str
        demo_url: str
        def __init__(self, database_name: _Optional[str] = ..., state: _Optional[str] = ..., is_failed: bool = ..., is_available: bool = ..., user_name: _Optional[str] = ..., demo_url: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXAMPLEDATASET_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    deployment_id: str
    exampledataset_id: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    status: ExampleDatasetInstallation.Status
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., deployment_id: _Optional[str] = ..., exampledataset_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., status: _Optional[_Union[ExampleDatasetInstallation.Status, _Mapping]] = ...) -> None: ...

class ListExampleDatasetsRequest(_message.Message):
    __slots__ = ["options", "organization_id"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class ExampleDatasetList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ExampleDataset]
    def __init__(self, items: _Optional[_Iterable[_Union[ExampleDataset, _Mapping]]] = ...) -> None: ...

class ExampleDatasetInstallationList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ExampleDatasetInstallation]
    def __init__(self, items: _Optional[_Iterable[_Union[ExampleDatasetInstallation, _Mapping]]] = ...) -> None: ...

class ListExampleDatasetInstallationsRequest(_message.Message):
    __slots__ = ["deployment_id", "options"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    options: _common_pb2.ListOptions
    def __init__(self, deployment_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...
