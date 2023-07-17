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
    __slots__ = ["backup_id", "region_id", "accepted_terms_and_conditions_id", "project_id"]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_TERMS_AND_CONDITIONS_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    region_id: str
    accepted_terms_and_conditions_id: str
    project_id: str
    def __init__(self, backup_id: _Optional[str] = ..., region_id: _Optional[str] = ..., accepted_terms_and_conditions_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeploymentReplication(_message.Message):
    __slots__ = ["deployment_id", "started", "certificate_pem", "tls_keyfile", "master_endpoint", "cancelation_options", "status"]
    class CancelationOptions(_message.Message):
        __slots__ = ["data_consistency_not_required", "make_source_deployment_read_only"]
        DATA_CONSISTENCY_NOT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        MAKE_SOURCE_DEPLOYMENT_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
        data_consistency_not_required: bool
        make_source_deployment_read_only: bool
        def __init__(self, data_consistency_not_required: bool = ..., make_source_deployment_read_only: bool = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["phase", "message", "total_shards", "shards_in_sync", "sync_endpoint", "phase_updated_at"]
        PHASE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SHARDS_FIELD_NUMBER: _ClassVar[int]
        SHARDS_IN_SYNC_FIELD_NUMBER: _ClassVar[int]
        SYNC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        PHASE_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        phase: str
        message: str
        total_shards: int
        shards_in_sync: int
        sync_endpoint: str
        phase_updated_at: _timestamp_pb2.Timestamp
        def __init__(self, phase: _Optional[str] = ..., message: _Optional[str] = ..., total_shards: _Optional[int] = ..., shards_in_sync: _Optional[int] = ..., sync_endpoint: _Optional[str] = ..., phase_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
    TLS_KEYFILE_FIELD_NUMBER: _ClassVar[int]
    MASTER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CANCELATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    started: bool
    certificate_pem: str
    tls_keyfile: str
    master_endpoint: _containers.RepeatedScalarFieldContainer[str]
    cancelation_options: DeploymentReplication.CancelationOptions
    status: DeploymentReplication.Status
    def __init__(self, deployment_id: _Optional[str] = ..., started: bool = ..., certificate_pem: _Optional[str] = ..., tls_keyfile: _Optional[str] = ..., master_endpoint: _Optional[_Iterable[str]] = ..., cancelation_options: _Optional[_Union[DeploymentReplication.CancelationOptions, _Mapping]] = ..., status: _Optional[_Union[DeploymentReplication.Status, _Mapping]] = ...) -> None: ...
