from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UsageItem(_message.Message):
    __slots__ = ["id", "url", "kind", "resource", "starts_at", "ends_at", "has_ended", "tier_id", "invoice_id", "deployment_size", "network_transfer_size", "backup_storage_size", "auditlog_size", "auditlog_storage_size", "notebook_size"]
    class Resource(_message.Message):
        __slots__ = ["id", "url", "kind", "description", "organization_id", "organization_name", "project_id", "project_name", "deployment_id", "deployment_name", "deployment_member_name", "cloud_provider_id", "cloud_region_id", "support_plan_id", "deployment_model", "prepaid_deployment_id", "prepaid_deployment_starts_at", "prepaid_deployment_ends_at"]
        ID_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        KIND_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_NAME_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
        CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
        CLOUD_REGION_ID_FIELD_NUMBER: _ClassVar[int]
        SUPPORT_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_MODEL_FIELD_NUMBER: _ClassVar[int]
        PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        PREPAID_DEPLOYMENT_STARTS_AT_FIELD_NUMBER: _ClassVar[int]
        PREPAID_DEPLOYMENT_ENDS_AT_FIELD_NUMBER: _ClassVar[int]
        id: str
        url: str
        kind: str
        description: str
        organization_id: str
        organization_name: str
        project_id: str
        project_name: str
        deployment_id: str
        deployment_name: str
        deployment_member_name: str
        cloud_provider_id: str
        cloud_region_id: str
        support_plan_id: str
        deployment_model: str
        prepaid_deployment_id: str
        prepaid_deployment_starts_at: _timestamp_pb2.Timestamp
        prepaid_deployment_ends_at: _timestamp_pb2.Timestamp
        def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., kind: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., organization_name: _Optional[str] = ..., project_id: _Optional[str] = ..., project_name: _Optional[str] = ..., deployment_id: _Optional[str] = ..., deployment_name: _Optional[str] = ..., deployment_member_name: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., cloud_region_id: _Optional[str] = ..., support_plan_id: _Optional[str] = ..., deployment_model: _Optional[str] = ..., prepaid_deployment_id: _Optional[str] = ..., prepaid_deployment_starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., prepaid_deployment_ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class DeploymentSize(_message.Message):
        __slots__ = ["coordinators", "coordinator_memory_size", "dbservers", "dbserver_memory_size", "dbserver_disk_size", "agents", "agent_memory_size", "agent_disk_size", "node_size_id", "disk_performance_id", "addon_ids", "is_paused"]
        COORDINATORS_FIELD_NUMBER: _ClassVar[int]
        COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        DBSERVERS_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        AGENTS_FIELD_NUMBER: _ClassVar[int]
        AGENT_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        AGENT_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
        ADDON_IDS_FIELD_NUMBER: _ClassVar[int]
        IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
        coordinators: int
        coordinator_memory_size: int
        dbservers: int
        dbserver_memory_size: int
        dbserver_disk_size: int
        agents: int
        agent_memory_size: int
        agent_disk_size: int
        node_size_id: str
        disk_performance_id: str
        addon_ids: _containers.RepeatedScalarFieldContainer[str]
        is_paused: bool
        def __init__(self, coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ..., agents: _Optional[int] = ..., agent_memory_size: _Optional[int] = ..., agent_disk_size: _Optional[int] = ..., node_size_id: _Optional[str] = ..., disk_performance_id: _Optional[str] = ..., addon_ids: _Optional[_Iterable[str]] = ..., is_paused: bool = ...) -> None: ...
    class NetworkTransferSize(_message.Message):
        __slots__ = ["destination", "total_transfer_ingress_size", "total_transfer_egress_size"]
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TRANSFER_INGRESS_SIZE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TRANSFER_EGRESS_SIZE_FIELD_NUMBER: _ClassVar[int]
        destination: str
        total_transfer_ingress_size: int
        total_transfer_egress_size: int
        def __init__(self, destination: _Optional[str] = ..., total_transfer_ingress_size: _Optional[int] = ..., total_transfer_egress_size: _Optional[int] = ...) -> None: ...
    class BackupStorageSize(_message.Message):
        __slots__ = ["cloud_storage_size"]
        CLOUD_STORAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        cloud_storage_size: int
        def __init__(self, cloud_storage_size: _Optional[int] = ...) -> None: ...
    class AuditLogSize(_message.Message):
        __slots__ = ["destination_type", "event_count", "event_size", "https_post_count"]
        DESTINATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        EVENT_SIZE_FIELD_NUMBER: _ClassVar[int]
        HTTPS_POST_COUNT_FIELD_NUMBER: _ClassVar[int]
        destination_type: str
        event_count: int
        event_size: int
        https_post_count: int
        def __init__(self, destination_type: _Optional[str] = ..., event_count: _Optional[int] = ..., event_size: _Optional[int] = ..., https_post_count: _Optional[int] = ...) -> None: ...
    class AuditLogStorageSize(_message.Message):
        __slots__ = ["cloud_storage_size"]
        CLOUD_STORAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        cloud_storage_size: int
        def __init__(self, cloud_storage_size: _Optional[int] = ...) -> None: ...
    class NotebookSize(_message.Message):
        __slots__ = ["cpu_size", "memory_size", "disk_size", "is_paused", "notebook_model_id"]
        CPU_SIZE_FIELD_NUMBER: _ClassVar[int]
        MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
        NOTEBOOK_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        cpu_size: float
        memory_size: int
        disk_size: int
        is_paused: bool
        notebook_model_id: str
        def __init__(self, cpu_size: _Optional[float] = ..., memory_size: _Optional[int] = ..., disk_size: _Optional[int] = ..., is_paused: bool = ..., notebook_model_id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    HAS_ENDED_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TRANSFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_STORAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_SIZE_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_STORAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_SIZE_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    kind: str
    resource: UsageItem.Resource
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    has_ended: bool
    tier_id: str
    invoice_id: str
    deployment_size: UsageItem.DeploymentSize
    network_transfer_size: UsageItem.NetworkTransferSize
    backup_storage_size: UsageItem.BackupStorageSize
    auditlog_size: UsageItem.AuditLogSize
    auditlog_storage_size: UsageItem.AuditLogStorageSize
    notebook_size: UsageItem.NotebookSize
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., kind: _Optional[str] = ..., resource: _Optional[_Union[UsageItem.Resource, _Mapping]] = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., has_ended: bool = ..., tier_id: _Optional[str] = ..., invoice_id: _Optional[str] = ..., deployment_size: _Optional[_Union[UsageItem.DeploymentSize, _Mapping]] = ..., network_transfer_size: _Optional[_Union[UsageItem.NetworkTransferSize, _Mapping]] = ..., backup_storage_size: _Optional[_Union[UsageItem.BackupStorageSize, _Mapping]] = ..., auditlog_size: _Optional[_Union[UsageItem.AuditLogSize, _Mapping]] = ..., auditlog_storage_size: _Optional[_Union[UsageItem.AuditLogStorageSize, _Mapping]] = ..., notebook_size: _Optional[_Union[UsageItem.NotebookSize, _Mapping]] = ...) -> None: ...

class UsageItemList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[UsageItem]
    def __init__(self, items: _Optional[_Iterable[_Union[UsageItem, _Mapping]]] = ...) -> None: ...

class ListUsageItemsRequest(_message.Message):
    __slots__ = ["organization_id", "to", "sort_descending", "kind", "options", "resource_url", "resource_kind", "project_id", "deployment_id", "node_size_id", "region_id", "has_no_invoice_id", "has_invoice_id", "invoice_id", "not_start_before"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    SORT_DESCENDING_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_NO_INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    NOT_START_BEFORE_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    to: _timestamp_pb2.Timestamp
    sort_descending: bool
    kind: str
    options: _common_pb2.ListOptions
    resource_url: str
    resource_kind: str
    project_id: str
    deployment_id: str
    node_size_id: str
    region_id: str
    has_no_invoice_id: bool
    has_invoice_id: bool
    invoice_id: str
    not_start_before: _timestamp_pb2.Timestamp
    def __init__(self, organization_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sort_descending: bool = ..., kind: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., resource_url: _Optional[str] = ..., resource_kind: _Optional[str] = ..., project_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., node_size_id: _Optional[str] = ..., region_id: _Optional[str] = ..., has_no_invoice_id: bool = ..., has_invoice_id: bool = ..., invoice_id: _Optional[str] = ..., not_start_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...
