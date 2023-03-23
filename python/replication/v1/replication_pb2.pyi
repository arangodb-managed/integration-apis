from common.v1 import common_pb2 as _common_pb2
from data.v1 import data_pb2 as _data_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloneDeploymentFromBackupRequest(_message.Message):
    __slots__ = ["accepted_terms_and_conditions_id", "backup_id", "project_id", "region_id"]
    ACCEPTED_TERMS_AND_CONDITIONS_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    accepted_terms_and_conditions_id: str
    backup_id: str
    project_id: str
    region_id: str
    def __init__(self, backup_id: _Optional[str] = ..., region_id: _Optional[str] = ..., accepted_terms_and_conditions_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeploymentReplication(_message.Message):
    __slots__ = ["cancelation_options", "certificate_pem", "deployment_id", "master_endpoint", "started", "status", "tls_keyfile"]
    class CancelationOptions(_message.Message):
        __slots__ = ["data_consistency_not_required", "make_source_deployment_read_only"]
        DATA_CONSISTENCY_NOT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        MAKE_SOURCE_DEPLOYMENT_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
        data_consistency_not_required: bool
        make_source_deployment_read_only: bool
        def __init__(self, data_consistency_not_required: bool = ..., make_source_deployment_read_only: bool = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["message", "phase", "phase_updated_at", "shards_in_sync", "sync_endpoint", "total_shards"]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PHASE_FIELD_NUMBER: _ClassVar[int]
        PHASE_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        SHARDS_IN_SYNC_FIELD_NUMBER: _ClassVar[int]
        SYNC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SHARDS_FIELD_NUMBER: _ClassVar[int]
        message: str
        phase: str
        phase_updated_at: _timestamp_pb2.Timestamp
        shards_in_sync: int
        sync_endpoint: str
        total_shards: int
        def __init__(self, phase: _Optional[str] = ..., message: _Optional[str] = ..., total_shards: _Optional[int] = ..., shards_in_sync: _Optional[int] = ..., sync_endpoint: _Optional[str] = ..., phase_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    CANCELATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TLS_KEYFILE_FIELD_NUMBER: _ClassVar[int]
    cancelation_options: DeploymentReplication.CancelationOptions
    certificate_pem: str
    deployment_id: str
    master_endpoint: _containers.RepeatedScalarFieldContainer[str]
    started: bool
    status: DeploymentReplication.Status
    tls_keyfile: str
    def __init__(self, deployment_id: _Optional[str] = ..., started: bool = ..., certificate_pem: _Optional[str] = ..., tls_keyfile: _Optional[str] = ..., master_endpoint: _Optional[_Iterable[str]] = ..., cancelation_options: _Optional[_Union[DeploymentReplication.CancelationOptions, _Mapping]] = ..., status: _Optional[_Union[DeploymentReplication.Status, _Mapping]] = ...) -> None: ...
