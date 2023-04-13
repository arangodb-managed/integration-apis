from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListUsageItemsRequest(_message.Message):
    __slots__ = ["deployment_id", "has_invoice_id", "has_no_invoice_id", "invoice_id", "kind", "node_size_id", "not_start_before", "options", "organization_id", "project_id", "region_id", "resource_kind", "resource_url", "sort_descending", "to"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    HAS_INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_NO_INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    NOT_START_BEFORE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    SORT_DESCENDING_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    has_invoice_id: bool
    has_no_invoice_id: bool
    invoice_id: str
    kind: str
    node_size_id: str
    not_start_before: _timestamp_pb2.Timestamp
    options: _common_pb2.ListOptions
    organization_id: str
    project_id: str
    region_id: str
    resource_kind: str
    resource_url: str
    sort_descending: bool
    to: _timestamp_pb2.Timestamp
    def __init__(self, organization_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sort_descending: bool = ..., kind: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., resource_url: _Optional[str] = ..., resource_kind: _Optional[str] = ..., project_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., node_size_id: _Optional[str] = ..., region_id: _Optional[str] = ..., has_no_invoice_id: bool = ..., has_invoice_id: bool = ..., invoice_id: _Optional[str] = ..., not_start_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class UsageItem(_message.Message):
    __slots__ = ["auditlog_size", "auditlog_storage_size", "backup_storage_size", "deployment_size", "ends_at", "has_ended", "id", "invoice_id", "kind", "network_transfer_size", "notebook_size", "resource", "starts_at", "tier_id", "url"]
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
    class BackupStorageSize(_message.Message):
        __slots__ = ["cloud_storage_size"]
        CLOUD_STORAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        cloud_storage_size: int
        def __init__(self, cloud_storage_size: _Optional[int] = ...) -> None: ...
    class DeploymentSize(_message.Message):
        __slots__ = ["addon_ids", "agent_disk_size", "agent_memory_size", "agents", "coordinator_memory_size", "coordinators", "dbserver_disk_size", "dbserver_memory_size", "dbservers", "disk_performance_id", "is_paused", "node_size_id"]
        ADDON_IDS_FIELD_NUMBER: _ClassVar[int]
        AGENTS_FIELD_NUMBER: _ClassVar[int]
        AGENT_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        AGENT_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        COORDINATORS_FIELD_NUMBER: _ClassVar[int]
        COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        DBSERVERS_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
        IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
        NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
        addon_ids: _containers.RepeatedScalarFieldContainer[str]
        agent_disk_size: int
        agent_memory_size: int
        agents: int
        coordinator_memory_size: int
        coordinators: int
        dbserver_disk_size: int
        dbserver_memory_size: int
        dbservers: int
        disk_performance_id: str
        is_paused: bool
        node_size_id: str
        def __init__(self, coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ..., agents: _Optional[int] = ..., agent_memory_size: _Optional[int] = ..., agent_disk_size: _Optional[int] = ..., node_size_id: _Optional[str] = ..., disk_performance_id: _Optional[str] = ..., addon_ids: _Optional[_Iterable[str]] = ..., is_paused: bool = ...) -> None: ...
    class NetworkTransferSize(_message.Message):
        __slots__ = ["destination", "total_transfer_egress_size", "total_transfer_ingress_size"]
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TRANSFER_EGRESS_SIZE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TRANSFER_INGRESS_SIZE_FIELD_NUMBER: _ClassVar[int]
        destination: str
        total_transfer_egress_size: int
        total_transfer_ingress_size: int
        def __init__(self, destination: _Optional[str] = ..., total_transfer_ingress_size: _Optional[int] = ..., total_transfer_egress_size: _Optional[int] = ...) -> None: ...
    class NotebookSize(_message.Message):
        __slots__ = ["cpu_size", "disk_size", "is_paused", "memory_size", "notebook_model_id"]
        CPU_SIZE_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
        MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        NOTEBOOK_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        cpu_size: float
        disk_size: int
        is_paused: bool
        memory_size: int
        notebook_model_id: str
        def __init__(self, cpu_size: _Optional[float] = ..., memory_size: _Optional[int] = ..., disk_size: _Optional[int] = ..., is_paused: bool = ..., notebook_model_id: _Optional[str] = ...) -> None: ...
    class Resource(_message.Message):
        __slots__ = ["cloud_provider_id", "cloud_region_id", "deployment_id", "deployment_member_name", "deployment_model", "deployment_name", "description", "id", "kind", "organization_id", "organization_name", "prepaid_deployment_ends_at", "prepaid_deployment_id", "prepaid_deployment_starts_at", "project_id", "project_name", "support_plan_id", "url"]
        CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
        CLOUD_REGION_ID_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_MODEL_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        KIND_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
        PREPAID_DEPLOYMENT_ENDS_AT_FIELD_NUMBER: _ClassVar[int]
        PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        PREPAID_DEPLOYMENT_STARTS_AT_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        SUPPORT_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        cloud_provider_id: str
        cloud_region_id: str
        deployment_id: str
        deployment_member_name: str
        deployment_model: str
        deployment_name: str
        description: str
        id: str
        kind: str
        organization_id: str
        organization_name: str
        prepaid_deployment_ends_at: _timestamp_pb2.Timestamp
        prepaid_deployment_id: str
        prepaid_deployment_starts_at: _timestamp_pb2.Timestamp
        project_id: str
        project_name: str
        support_plan_id: str
        url: str
        def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., kind: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., organization_name: _Optional[str] = ..., project_id: _Optional[str] = ..., project_name: _Optional[str] = ..., deployment_id: _Optional[str] = ..., deployment_name: _Optional[str] = ..., deployment_member_name: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., cloud_region_id: _Optional[str] = ..., support_plan_id: _Optional[str] = ..., deployment_model: _Optional[str] = ..., prepaid_deployment_id: _Optional[str] = ..., prepaid_deployment_starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., prepaid_deployment_ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    AUDITLOG_SIZE_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_STORAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_STORAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    HAS_ENDED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TRANSFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    auditlog_size: UsageItem.AuditLogSize
    auditlog_storage_size: UsageItem.AuditLogStorageSize
    backup_storage_size: UsageItem.BackupStorageSize
    deployment_size: UsageItem.DeploymentSize
    ends_at: _timestamp_pb2.Timestamp
    has_ended: bool
    id: str
    invoice_id: str
    kind: str
    network_transfer_size: UsageItem.NetworkTransferSize
    notebook_size: UsageItem.NotebookSize
    resource: UsageItem.Resource
    starts_at: _timestamp_pb2.Timestamp
    tier_id: str
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., kind: _Optional[str] = ..., resource: _Optional[_Union[UsageItem.Resource, _Mapping]] = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., has_ended: bool = ..., tier_id: _Optional[str] = ..., invoice_id: _Optional[str] = ..., deployment_size: _Optional[_Union[UsageItem.DeploymentSize, _Mapping]] = ..., network_transfer_size: _Optional[_Union[UsageItem.NetworkTransferSize, _Mapping]] = ..., backup_storage_size: _Optional[_Union[UsageItem.BackupStorageSize, _Mapping]] = ..., auditlog_size: _Optional[_Union[UsageItem.AuditLogSize, _Mapping]] = ..., auditlog_storage_size: _Optional[_Union[UsageItem.AuditLogStorageSize, _Mapping]] = ..., notebook_size: _Optional[_Union[UsageItem.NotebookSize, _Mapping]] = ...) -> None: ...

class UsageItemList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[UsageItem]
    def __init__(self, items: _Optional[_Iterable[_Union[UsageItem, _Mapping]]] = ...) -> None: ...
