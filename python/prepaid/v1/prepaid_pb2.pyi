from common.v1 import common_pb2 as _common_pb2
from data.v1 import data_pb2 as _data_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloneFromBackupRequest(_message.Message):
    __slots__ = ["backup_id", "prepaid_deployment_id"]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    prepaid_deployment_id: str
    def __init__(self, prepaid_deployment_id: _Optional[str] = ..., backup_id: _Optional[str] = ...) -> None: ...

class CreateDeploymentRequest(_message.Message):
    __slots__ = ["accepted_terms_and_conditions_id", "certificates", "ipallowlist_id", "prepaid_deployment_id", "project_id", "version"]
    class CertificateSpec(_message.Message):
        __slots__ = ["alternate_dns_names", "ca_certificate_id"]
        ALTERNATE_DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
        CA_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
        alternate_dns_names: _containers.RepeatedScalarFieldContainer[str]
        ca_certificate_id: str
        def __init__(self, ca_certificate_id: _Optional[str] = ..., alternate_dns_names: _Optional[_Iterable[str]] = ...) -> None: ...
    ACCEPTED_TERMS_AND_CONDITIONS_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    IPALLOWLIST_ID_FIELD_NUMBER: _ClassVar[int]
    PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    accepted_terms_and_conditions_id: str
    certificates: CreateDeploymentRequest.CertificateSpec
    ipallowlist_id: str
    prepaid_deployment_id: str
    project_id: str
    version: str
    def __init__(self, prepaid_deployment_id: _Optional[str] = ..., project_id: _Optional[str] = ..., ipallowlist_id: _Optional[str] = ..., version: _Optional[str] = ..., certificates: _Optional[_Union[CreateDeploymentRequest.CertificateSpec, _Mapping]] = ..., accepted_terms_and_conditions_id: _Optional[str] = ...) -> None: ...

class ListPrepaidDeploymentsRequest(_message.Message):
    __slots__ = ["options", "organization_id"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class PrepaidDeployment(_message.Message):
    __slots__ = ["addons", "created_at", "deleted_at", "description", "disk_performance_id", "ends_at", "id", "is_active", "is_deleted", "model", "name", "organization_id", "region_id", "starts_at", "status", "support_plan_id", "url"]
    class Status(_message.Message):
        __slots__ = ["attached_at", "deployment_id", "deployment_url", "detached_at", "last_warning_email_send_at"]
        ATTACHED_AT_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_URL_FIELD_NUMBER: _ClassVar[int]
        DETACHED_AT_FIELD_NUMBER: _ClassVar[int]
        LAST_WARNING_EMAIL_SEND_AT_FIELD_NUMBER: _ClassVar[int]
        attached_at: _timestamp_pb2.Timestamp
        deployment_id: str
        deployment_url: str
        detached_at: _timestamp_pb2.Timestamp
        last_warning_email_send_at: _timestamp_pb2.Timestamp
        def __init__(self, deployment_id: _Optional[str] = ..., attached_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., detached_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployment_url: _Optional[str] = ..., last_warning_email_send_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ADDONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    addons: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    description: str
    disk_performance_id: str
    ends_at: _timestamp_pb2.Timestamp
    id: str
    is_active: bool
    is_deleted: bool
    model: _data_pb2.Deployment.ModelSpec
    name: str
    organization_id: str
    region_id: str
    starts_at: _timestamp_pb2.Timestamp
    status: PrepaidDeployment.Status
    support_plan_id: str
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., region_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_active: bool = ..., support_plan_id: _Optional[str] = ..., model: _Optional[_Union[_data_pb2.Deployment.ModelSpec, _Mapping]] = ..., addons: _Optional[_Iterable[str]] = ..., disk_performance_id: _Optional[str] = ..., status: _Optional[_Union[PrepaidDeployment.Status, _Mapping]] = ...) -> None: ...

class PrepaidDeploymentList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PrepaidDeployment]
    def __init__(self, items: _Optional[_Iterable[_Union[PrepaidDeployment, _Mapping]]] = ...) -> None: ...

class UpdateDeploymentRequest(_message.Message):
    __slots__ = ["prepaid_deployment_id"]
    PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    prepaid_deployment_id: str
    def __init__(self, prepaid_deployment_id: _Optional[str] = ...) -> None: ...
