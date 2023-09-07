from common.v1 import common_pb2 as _common_pb2
from data.v1 import data_pb2 as _data_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepaidDeployment(_message.Message):
    __slots__ = ["id", "url", "name", "description", "organization_id", "region_id", "created_at", "deleted_at", "is_deleted", "starts_at", "ends_at", "is_active", "support_plan_id", "model", "addons", "disk_performance_id", "status"]
    class Status(_message.Message):
        __slots__ = ["deployment_id", "attached_at", "detached_at", "deployment_url", "last_warning_email_send_at"]
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ATTACHED_AT_FIELD_NUMBER: _ClassVar[int]
        DETACHED_AT_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_URL_FIELD_NUMBER: _ClassVar[int]
        LAST_WARNING_EMAIL_SEND_AT_FIELD_NUMBER: _ClassVar[int]
        deployment_id: str
        attached_at: _timestamp_pb2.Timestamp
        detached_at: _timestamp_pb2.Timestamp
        deployment_url: str
        last_warning_email_send_at: _timestamp_pb2.Timestamp
        def __init__(self, deployment_id: _Optional[str] = ..., attached_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., detached_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployment_url: _Optional[str] = ..., last_warning_email_send_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ADDONS_FIELD_NUMBER: _ClassVar[int]
    DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    organization_id: str
    region_id: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    is_active: bool
    support_plan_id: str
    model: _data_pb2.Deployment.ModelSpec
    addons: _containers.RepeatedScalarFieldContainer[str]
    disk_performance_id: str
    status: PrepaidDeployment.Status
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., region_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_active: bool = ..., support_plan_id: _Optional[str] = ..., model: _Optional[_Union[_data_pb2.Deployment.ModelSpec, _Mapping]] = ..., addons: _Optional[_Iterable[str]] = ..., disk_performance_id: _Optional[str] = ..., status: _Optional[_Union[PrepaidDeployment.Status, _Mapping]] = ...) -> None: ...

class PrepaidDeploymentList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PrepaidDeployment]
    def __init__(self, items: _Optional[_Iterable[_Union[PrepaidDeployment, _Mapping]]] = ...) -> None: ...

class ListPrepaidDeploymentsRequest(_message.Message):
    __slots__ = ["organization_id", "options"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    options: _common_pb2.ListOptions
    def __init__(self, organization_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class UpdateDeploymentRequest(_message.Message):
    __slots__ = ["prepaid_deployment_id"]
    PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    prepaid_deployment_id: str
    def __init__(self, prepaid_deployment_id: _Optional[str] = ...) -> None: ...

class CloneFromBackupRequest(_message.Message):
    __slots__ = ["prepaid_deployment_id", "backup_id"]
    PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    prepaid_deployment_id: str
    backup_id: str
    def __init__(self, prepaid_deployment_id: _Optional[str] = ..., backup_id: _Optional[str] = ...) -> None: ...

class CreateDeploymentRequest(_message.Message):
    __slots__ = ["prepaid_deployment_id", "project_id", "ipallowlist_id", "version", "certificates", "accepted_terms_and_conditions_id", "is_platform_authentication_enabled"]
    class CertificateSpec(_message.Message):
        __slots__ = ["ca_certificate_id", "alternate_dns_names"]
        CA_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
        ALTERNATE_DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
        ca_certificate_id: str
        alternate_dns_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, ca_certificate_id: _Optional[str] = ..., alternate_dns_names: _Optional[_Iterable[str]] = ...) -> None: ...
    PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    IPALLOWLIST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_TERMS_AND_CONDITIONS_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PLATFORM_AUTHENTICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    prepaid_deployment_id: str
    project_id: str
    ipallowlist_id: str
    version: str
    certificates: CreateDeploymentRequest.CertificateSpec
    accepted_terms_and_conditions_id: str
    is_platform_authentication_enabled: bool
    def __init__(self, prepaid_deployment_id: _Optional[str] = ..., project_id: _Optional[str] = ..., ipallowlist_id: _Optional[str] = ..., version: _Optional[str] = ..., certificates: _Optional[_Union[CreateDeploymentRequest.CertificateSpec, _Mapping]] = ..., accepted_terms_and_conditions_id: _Optional[str] = ..., is_platform_authentication_enabled: bool = ...) -> None: ...
