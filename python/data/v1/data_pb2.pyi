from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from github.com.golang.protobuf.ptypes.duration import duration_pb2 as _duration_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RotateDeploymentServerRequest(_message.Message):
    __slots__ = ["deployment_id", "server_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    server_id: str
    def __init__(self, deployment_id: _Optional[str] = ..., server_id: _Optional[str] = ...) -> None: ...

class CreateTestDatabaseResponse(_message.Message):
    __slots__ = ["db_name", "username", "password", "hostname", "port"]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    username: str
    password: str
    hostname: str
    port: str
    def __init__(self, db_name: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., hostname: _Optional[str] = ..., port: _Optional[str] = ...) -> None: ...

class CreateTestDatabaseRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class RebalanceDeploymentShardsRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class Deployment(_message.Message):
    __slots__ = ["id", "url", "name", "description", "project_id", "region_id", "created_at", "deleted_at", "is_deleted", "support_plan_id", "created_by_id", "accepted_terms_and_conditions_id", "locked", "is_paused", "last_paused_at", "last_resumed_at", "prepaid_deployment_id", "disable_foxx_authentication", "prepaid_deployment_starts_at", "prepaid_deployment_ends_at", "is_prepaid_deployment_update_available", "private_endpoint", "version", "replace_version_by", "upgrade_recommendation", "version_is_end_of_life", "certificates", "servers", "ipallowlist_id", "model", "custom_image", "iamprovider_id", "disk_performance_id", "disk_performance_locked", "disk_rate_limit_period", "last_disk_performance_updated_at", "last_disk_size_updated_at", "disk_rate_limit_active", "status", "size", "expiration", "backup_restore", "deployment_recommendations", "is_clone", "clone_backup_id", "notification_settings", "disk_auto_size_settings", "is_scheduled_root_password_rotation_enabled", "last_root_password_rotated_at", "deployment_profile_id", "is_platform_authentication_enabled", "intended_use_case"]
    class CertificateSpec(_message.Message):
        __slots__ = ["ca_certificate_id", "alternate_dns_names"]
        CA_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
        ALTERNATE_DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
        ca_certificate_id: str
        alternate_dns_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, ca_certificate_id: _Optional[str] = ..., alternate_dns_names: _Optional[_Iterable[str]] = ...) -> None: ...
    class ServersSpec(_message.Message):
        __slots__ = ["coordinators", "coordinator_memory_size", "coordinator_args", "dbservers", "dbserver_memory_size", "dbserver_disk_size", "dbserver_args", "minimum_dbservers_count"]
        COORDINATORS_FIELD_NUMBER: _ClassVar[int]
        COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        COORDINATOR_ARGS_FIELD_NUMBER: _ClassVar[int]
        DBSERVERS_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_ARGS_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_DBSERVERS_COUNT_FIELD_NUMBER: _ClassVar[int]
        coordinators: int
        coordinator_memory_size: int
        coordinator_args: _containers.RepeatedScalarFieldContainer[str]
        dbservers: int
        dbserver_memory_size: int
        dbserver_disk_size: int
        dbserver_args: _containers.RepeatedScalarFieldContainer[str]
        minimum_dbservers_count: int
        def __init__(self, coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., coordinator_args: _Optional[_Iterable[str]] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ..., dbserver_args: _Optional[_Iterable[str]] = ..., minimum_dbservers_count: _Optional[int] = ...) -> None: ...
    class ModelSpec(_message.Message):
        __slots__ = ["model", "node_size_id", "node_count", "node_disk_size"]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        model: str
        node_size_id: str
        node_count: int
        node_disk_size: int
        def __init__(self, model: _Optional[str] = ..., node_size_id: _Optional[str] = ..., node_count: _Optional[int] = ..., node_disk_size: _Optional[int] = ...) -> None: ...
    class ServerStatus(_message.Message):
        __slots__ = ["id", "type", "description", "created_at", "ready", "member_of_cluster", "failed", "creating", "ok", "bad", "upgrading", "version", "last_started_at", "rotation_pending", "can_be_deleted", "is_leader", "data_volume_info", "recent_restarts", "last_memory_usage", "last_cpu_usage", "last_memory_limit", "last_cpu_limit"]
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        READY_FIELD_NUMBER: _ClassVar[int]
        MEMBER_OF_CLUSTER_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        CREATING_FIELD_NUMBER: _ClassVar[int]
        OK_FIELD_NUMBER: _ClassVar[int]
        BAD_FIELD_NUMBER: _ClassVar[int]
        UPGRADING_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        LAST_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        ROTATION_PENDING_FIELD_NUMBER: _ClassVar[int]
        CAN_BE_DELETED_FIELD_NUMBER: _ClassVar[int]
        IS_LEADER_FIELD_NUMBER: _ClassVar[int]
        DATA_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
        RECENT_RESTARTS_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: str
        description: str
        created_at: _timestamp_pb2.Timestamp
        ready: bool
        member_of_cluster: bool
        failed: bool
        creating: bool
        ok: bool
        bad: bool
        upgrading: bool
        version: str
        last_started_at: _timestamp_pb2.Timestamp
        rotation_pending: bool
        can_be_deleted: bool
        is_leader: bool
        data_volume_info: DataVolumeInfo
        recent_restarts: int
        last_memory_usage: int
        last_cpu_usage: float
        last_memory_limit: int
        last_cpu_limit: float
        def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ready: bool = ..., member_of_cluster: bool = ..., failed: bool = ..., creating: bool = ..., ok: bool = ..., bad: bool = ..., upgrading: bool = ..., version: _Optional[str] = ..., last_started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rotation_pending: bool = ..., can_be_deleted: bool = ..., is_leader: bool = ..., data_volume_info: _Optional[_Union[DataVolumeInfo, _Mapping]] = ..., recent_restarts: _Optional[int] = ..., last_memory_usage: _Optional[int] = ..., last_cpu_usage: _Optional[float] = ..., last_memory_limit: _Optional[int] = ..., last_cpu_limit: _Optional[float] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["endpoint", "description", "created", "ready", "upgrading", "server_versions", "servers", "bootstrapped_at", "bootstrapped", "endpoint_self_signed", "private_endpoint", "private_endpoint_only", "endpoint_private_endpoint", "endpoint_private_endpoint_self_signed", "backup_restore_status", "total_backup_size_bytes", "backup_upload_in_progress", "is_up_to_date"]
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        READY_FIELD_NUMBER: _ClassVar[int]
        UPGRADING_FIELD_NUMBER: _ClassVar[int]
        SERVER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        SERVERS_FIELD_NUMBER: _ClassVar[int]
        BOOTSTRAPPED_AT_FIELD_NUMBER: _ClassVar[int]
        BOOTSTRAPPED_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_SELF_SIGNED_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_ONLY_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_PRIVATE_ENDPOINT_SELF_SIGNED_FIELD_NUMBER: _ClassVar[int]
        BACKUP_RESTORE_STATUS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        BACKUP_UPLOAD_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        IS_UP_TO_DATE_FIELD_NUMBER: _ClassVar[int]
        endpoint: str
        description: str
        created: bool
        ready: bool
        upgrading: bool
        server_versions: _containers.RepeatedScalarFieldContainer[str]
        servers: _containers.RepeatedCompositeFieldContainer[Deployment.ServerStatus]
        bootstrapped_at: _timestamp_pb2.Timestamp
        bootstrapped: bool
        endpoint_self_signed: str
        private_endpoint: bool
        private_endpoint_only: bool
        endpoint_private_endpoint: str
        endpoint_private_endpoint_self_signed: str
        backup_restore_status: Deployment.BackupRestoreStatus
        total_backup_size_bytes: int
        backup_upload_in_progress: bool
        is_up_to_date: bool
        def __init__(self, endpoint: _Optional[str] = ..., description: _Optional[str] = ..., created: bool = ..., ready: bool = ..., upgrading: bool = ..., server_versions: _Optional[_Iterable[str]] = ..., servers: _Optional[_Iterable[_Union[Deployment.ServerStatus, _Mapping]]] = ..., bootstrapped_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., bootstrapped: bool = ..., endpoint_self_signed: _Optional[str] = ..., private_endpoint: bool = ..., private_endpoint_only: bool = ..., endpoint_private_endpoint: _Optional[str] = ..., endpoint_private_endpoint_self_signed: _Optional[str] = ..., backup_restore_status: _Optional[_Union[Deployment.BackupRestoreStatus, _Mapping]] = ..., total_backup_size_bytes: _Optional[int] = ..., backup_upload_in_progress: bool = ..., is_up_to_date: bool = ...) -> None: ...
    class BackupRestoreStatus(_message.Message):
        __slots__ = ["revision", "last_updated_at", "restoring", "status", "failure_reason"]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        RESTORING_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
        revision: int
        last_updated_at: _timestamp_pb2.Timestamp
        restoring: bool
        status: str
        failure_reason: str
        def __init__(self, revision: _Optional[int] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., restoring: bool = ..., status: _Optional[str] = ..., failure_reason: _Optional[str] = ...) -> None: ...
    class Expiration(_message.Message):
        __slots__ = ["expires_at", "reason", "last_warning_email_send_at", "last_warning_email_send_to"]
        EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        LAST_WARNING_EMAIL_SEND_AT_FIELD_NUMBER: _ClassVar[int]
        LAST_WARNING_EMAIL_SEND_TO_FIELD_NUMBER: _ClassVar[int]
        expires_at: _timestamp_pb2.Timestamp
        reason: str
        last_warning_email_send_at: _timestamp_pb2.Timestamp
        last_warning_email_send_to: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ..., last_warning_email_send_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_warning_email_send_to: _Optional[_Iterable[str]] = ...) -> None: ...
    class BackupRestoreSpec(_message.Message):
        __slots__ = ["revision", "last_updated_at", "restored_by_id", "backup_id"]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        RESTORED_BY_ID_FIELD_NUMBER: _ClassVar[int]
        BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
        revision: int
        last_updated_at: _timestamp_pb2.Timestamp
        restored_by_id: str
        backup_id: str
        def __init__(self, revision: _Optional[int] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., restored_by_id: _Optional[str] = ..., backup_id: _Optional[str] = ...) -> None: ...
    class NotificationSettings(_message.Message):
        __slots__ = ["email_addresses"]
        EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        email_addresses: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, email_addresses: _Optional[_Iterable[str]] = ...) -> None: ...
    class DiskAutoSizeSettings(_message.Message):
        __slots__ = ["maximum_node_disk_size"]
        MAXIMUM_NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        maximum_node_disk_size: int
        def __init__(self, maximum_node_disk_size: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_TERMS_AND_CONDITIONS_ID_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    LAST_PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RESUMED_AT_FIELD_NUMBER: _ClassVar[int]
    PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FOXX_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    PREPAID_DEPLOYMENT_STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    PREPAID_DEPLOYMENT_ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PREPAID_DEPLOYMENT_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REPLACE_VERSION_BY_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_IS_END_OF_LIFE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    IPALLOWLIST_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_IMAGE_FIELD_NUMBER: _ClassVar[int]
    IAMPROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_PERFORMANCE_LOCKED_FIELD_NUMBER: _ClassVar[int]
    DISK_RATE_LIMIT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    LAST_DISK_PERFORMANCE_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_DISK_SIZE_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DISK_RATE_LIMIT_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RESTORE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    IS_CLONE_FIELD_NUMBER: _ClassVar[int]
    CLONE_BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DISK_AUTO_SIZE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IS_SCHEDULED_ROOT_PASSWORD_ROTATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_ROOT_PASSWORD_ROTATED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PLATFORM_AUTHENTICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INTENDED_USE_CASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    project_id: str
    region_id: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    support_plan_id: str
    created_by_id: str
    accepted_terms_and_conditions_id: str
    locked: bool
    is_paused: bool
    last_paused_at: _timestamp_pb2.Timestamp
    last_resumed_at: _timestamp_pb2.Timestamp
    prepaid_deployment_id: str
    disable_foxx_authentication: bool
    prepaid_deployment_starts_at: _timestamp_pb2.Timestamp
    prepaid_deployment_ends_at: _timestamp_pb2.Timestamp
    is_prepaid_deployment_update_available: bool
    private_endpoint: bool
    version: str
    replace_version_by: ReplaceVersionBy
    upgrade_recommendation: UpgradeVersionRecommendation
    version_is_end_of_life: bool
    certificates: Deployment.CertificateSpec
    servers: Deployment.ServersSpec
    ipallowlist_id: str
    model: Deployment.ModelSpec
    custom_image: str
    iamprovider_id: str
    disk_performance_id: str
    disk_performance_locked: bool
    disk_rate_limit_period: _duration_pb2.Duration
    last_disk_performance_updated_at: _timestamp_pb2.Timestamp
    last_disk_size_updated_at: _timestamp_pb2.Timestamp
    disk_rate_limit_active: _duration_pb2.Duration
    status: Deployment.Status
    size: DeploymentSize
    expiration: Deployment.Expiration
    backup_restore: Deployment.BackupRestoreSpec
    deployment_recommendations: _containers.RepeatedCompositeFieldContainer[DeploymentSizeRecommendation]
    is_clone: bool
    clone_backup_id: str
    notification_settings: Deployment.NotificationSettings
    disk_auto_size_settings: Deployment.DiskAutoSizeSettings
    is_scheduled_root_password_rotation_enabled: bool
    last_root_password_rotated_at: _timestamp_pb2.Timestamp
    deployment_profile_id: str
    is_platform_authentication_enabled: bool
    intended_use_case: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., support_plan_id: _Optional[str] = ..., created_by_id: _Optional[str] = ..., accepted_terms_and_conditions_id: _Optional[str] = ..., locked: bool = ..., is_paused: bool = ..., last_paused_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_resumed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., prepaid_deployment_id: _Optional[str] = ..., disable_foxx_authentication: bool = ..., prepaid_deployment_starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., prepaid_deployment_ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_prepaid_deployment_update_available: bool = ..., private_endpoint: bool = ..., version: _Optional[str] = ..., replace_version_by: _Optional[_Union[ReplaceVersionBy, _Mapping]] = ..., upgrade_recommendation: _Optional[_Union[UpgradeVersionRecommendation, _Mapping]] = ..., version_is_end_of_life: bool = ..., certificates: _Optional[_Union[Deployment.CertificateSpec, _Mapping]] = ..., servers: _Optional[_Union[Deployment.ServersSpec, _Mapping]] = ..., ipallowlist_id: _Optional[str] = ..., model: _Optional[_Union[Deployment.ModelSpec, _Mapping]] = ..., custom_image: _Optional[str] = ..., iamprovider_id: _Optional[str] = ..., disk_performance_id: _Optional[str] = ..., disk_performance_locked: bool = ..., disk_rate_limit_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., last_disk_performance_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_disk_size_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., disk_rate_limit_active: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., status: _Optional[_Union[Deployment.Status, _Mapping]] = ..., size: _Optional[_Union[DeploymentSize, _Mapping]] = ..., expiration: _Optional[_Union[Deployment.Expiration, _Mapping]] = ..., backup_restore: _Optional[_Union[Deployment.BackupRestoreSpec, _Mapping]] = ..., deployment_recommendations: _Optional[_Iterable[_Union[DeploymentSizeRecommendation, _Mapping]]] = ..., is_clone: bool = ..., clone_backup_id: _Optional[str] = ..., notification_settings: _Optional[_Union[Deployment.NotificationSettings, _Mapping]] = ..., disk_auto_size_settings: _Optional[_Union[Deployment.DiskAutoSizeSettings, _Mapping]] = ..., is_scheduled_root_password_rotation_enabled: bool = ..., last_root_password_rotated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployment_profile_id: _Optional[str] = ..., is_platform_authentication_enabled: bool = ..., intended_use_case: _Optional[str] = ...) -> None: ...

class NodeSize(_message.Message):
    __slots__ = ["id", "name", "memory_size", "min_disk_size", "max_disk_size", "cpu_size", "disk_sizes"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIN_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    CPU_SIZE_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    memory_size: int
    min_disk_size: int
    max_disk_size: int
    cpu_size: str
    disk_sizes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., memory_size: _Optional[int] = ..., min_disk_size: _Optional[int] = ..., max_disk_size: _Optional[int] = ..., cpu_size: _Optional[str] = ..., disk_sizes: _Optional[_Iterable[int]] = ...) -> None: ...

class NodeSizeList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[NodeSize]
    def __init__(self, items: _Optional[_Iterable[_Union[NodeSize, _Mapping]]] = ...) -> None: ...

class NodeSizesRequest(_message.Message):
    __slots__ = ["project_id", "region_id", "deployment_id", "model", "organization_id", "include_restricted"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region_id: str
    deployment_id: str
    model: str
    organization_id: str
    include_restricted: bool
    def __init__(self, project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., model: _Optional[str] = ..., organization_id: _Optional[str] = ..., include_restricted: bool = ...) -> None: ...

class DeploymentModel(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeploymentModelList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DeploymentModel]
    def __init__(self, items: _Optional[_Iterable[_Union[DeploymentModel, _Mapping]]] = ...) -> None: ...

class ListDeploymentModelsRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class CPUSize(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CPUSizeList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CPUSize]
    def __init__(self, items: _Optional[_Iterable[_Union[CPUSize, _Mapping]]] = ...) -> None: ...

class ListCPUSizesRequest(_message.Message):
    __slots__ = ["project_id", "deployment_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    deployment_id: str
    def __init__(self, project_id: _Optional[str] = ..., deployment_id: _Optional[str] = ...) -> None: ...

class DeploymentCredentialsRequest(_message.Message):
    __slots__ = ["deployment_id", "reason"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    reason: str
    def __init__(self, deployment_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DeploymentCredentials(_message.Message):
    __slots__ = ["username", "password"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class DeploymentList(_message.Message):
    __slots__ = ["items", "budget"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Deployment]
    budget: _common_pb2.Budget
    def __init__(self, items: _Optional[_Iterable[_Union[Deployment, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ["version", "replace_by", "upgrade_recommendation", "is_end_of_life", "release_notes_url"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REPLACE_BY_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    IS_END_OF_LIFE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NOTES_URL_FIELD_NUMBER: _ClassVar[int]
    version: str
    replace_by: ReplaceVersionBy
    upgrade_recommendation: UpgradeVersionRecommendation
    is_end_of_life: bool
    release_notes_url: str
    def __init__(self, version: _Optional[str] = ..., replace_by: _Optional[_Union[ReplaceVersionBy, _Mapping]] = ..., upgrade_recommendation: _Optional[_Union[UpgradeVersionRecommendation, _Mapping]] = ..., is_end_of_life: bool = ..., release_notes_url: _Optional[str] = ...) -> None: ...

class ReplaceVersionBy(_message.Message):
    __slots__ = ["version", "reason", "auto_update_date"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    version: str
    reason: str
    auto_update_date: _timestamp_pb2.Timestamp
    def __init__(self, version: _Optional[str] = ..., reason: _Optional[str] = ..., auto_update_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpgradeVersionRecommendation(_message.Message):
    __slots__ = ["version", "reason"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    version: str
    reason: str
    def __init__(self, version: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class VersionList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Version]
    def __init__(self, items: _Optional[_Iterable[_Union[Version, _Mapping]]] = ...) -> None: ...

class ListVersionsRequest(_message.Message):
    __slots__ = ["options", "organization_id", "current_version"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    organization_id: str
    current_version: str
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., organization_id: _Optional[str] = ..., current_version: _Optional[str] = ...) -> None: ...

class ServersSpecLimitsRequest(_message.Message):
    __slots__ = ["project_id", "region_id", "deployment_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region_id: str
    deployment_id: str
    def __init__(self, project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., deployment_id: _Optional[str] = ...) -> None: ...

class ServersSpecLimits(_message.Message):
    __slots__ = ["coordinators", "coordinator_memory_size", "dbservers", "dbserver_memory_size", "dbserver_disk_size", "node_memory_size", "node_count"]
    class Limits(_message.Message):
        __slots__ = ["min", "max", "allowed_values"]
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
        min: int
        max: int
        allowed_values: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ..., allowed_values: _Optional[_Iterable[int]] = ...) -> None: ...
    COORDINATORS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVERS_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NODE_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    coordinators: ServersSpecLimits.Limits
    coordinator_memory_size: ServersSpecLimits.Limits
    dbservers: ServersSpecLimits.Limits
    dbserver_memory_size: ServersSpecLimits.Limits
    dbserver_disk_size: ServersSpecLimits.Limits
    node_memory_size: ServersSpecLimits.Limits
    node_count: ServersSpecLimits.Limits
    def __init__(self, coordinators: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., coordinator_memory_size: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., dbservers: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., dbserver_memory_size: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., dbserver_disk_size: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., node_memory_size: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., node_count: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ...) -> None: ...

class CalculateDeploymentSizeRequest(_message.Message):
    __slots__ = ["coordinators", "coordinator_memory_size", "dbservers", "dbserver_memory_size", "dbserver_disk_size", "model", "node_size_id", "node_count", "node_disk_size", "region_id"]
    COORDINATORS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVERS_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    coordinators: int
    coordinator_memory_size: int
    dbservers: int
    dbserver_memory_size: int
    dbserver_disk_size: int
    model: str
    node_size_id: str
    node_count: int
    node_disk_size: int
    region_id: str
    def __init__(self, coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ..., model: _Optional[str] = ..., node_size_id: _Optional[str] = ..., node_count: _Optional[int] = ..., node_disk_size: _Optional[int] = ..., region_id: _Optional[str] = ...) -> None: ...

class DeploymentSize(_message.Message):
    __slots__ = ["agents", "agent_memory_size", "agent_disk_size", "total_memory_size", "total_disk_size", "coordinators", "coordinator_memory_size", "dbservers", "dbserver_memory_size", "dbserver_disk_size"]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    AGENT_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    COORDINATORS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVERS_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    agents: int
    agent_memory_size: int
    agent_disk_size: int
    total_memory_size: int
    total_disk_size: int
    coordinators: int
    coordinator_memory_size: int
    dbservers: int
    dbserver_memory_size: int
    dbserver_disk_size: int
    def __init__(self, agents: _Optional[int] = ..., agent_memory_size: _Optional[int] = ..., agent_disk_size: _Optional[int] = ..., total_memory_size: _Optional[int] = ..., total_disk_size: _Optional[int] = ..., coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ...) -> None: ...

class DeploymentSizeRequest(_message.Message):
    __slots__ = ["dataset_size", "usecase", "model", "file_format", "number_of_documents", "number_of_columns", "working_set_percentage", "access_read_percentage", "access_create_percentage", "access_update_percentage", "growth_rate", "replication_factor", "project_id", "region_id"]
    DATASET_SIZE_FIELD_NUMBER: _ClassVar[int]
    USECASE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    WORKING_SET_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_READ_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CREATE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_UPDATE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    GROWTH_RATE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_size: int
    usecase: str
    model: str
    file_format: str
    number_of_documents: int
    number_of_columns: int
    working_set_percentage: float
    access_read_percentage: float
    access_create_percentage: float
    access_update_percentage: float
    growth_rate: float
    replication_factor: int
    project_id: str
    region_id: str
    def __init__(self, dataset_size: _Optional[int] = ..., usecase: _Optional[str] = ..., model: _Optional[str] = ..., file_format: _Optional[str] = ..., number_of_documents: _Optional[int] = ..., number_of_columns: _Optional[int] = ..., working_set_percentage: _Optional[float] = ..., access_read_percentage: _Optional[float] = ..., access_create_percentage: _Optional[float] = ..., access_update_percentage: _Optional[float] = ..., growth_rate: _Optional[float] = ..., replication_factor: _Optional[int] = ..., project_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class DeploymentSizeRecommendation(_message.Message):
    __slots__ = ["request", "created_at", "node_memory_size", "node_disk_size", "node_count", "exceeds_quota", "exceeds_platform"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    NODE_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXCEEDS_QUOTA_FIELD_NUMBER: _ClassVar[int]
    EXCEEDS_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    request: DeploymentSizeRequest
    created_at: _timestamp_pb2.Timestamp
    node_memory_size: int
    node_disk_size: int
    node_count: int
    exceeds_quota: bool
    exceeds_platform: bool
    def __init__(self, request: _Optional[_Union[DeploymentSizeRequest, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., node_memory_size: _Optional[int] = ..., node_disk_size: _Optional[int] = ..., node_count: _Optional[int] = ..., exceeds_quota: bool = ..., exceeds_platform: bool = ...) -> None: ...

class DataVolumeInfo(_message.Message):
    __slots__ = ["total_bytes", "used_bytes", "available_bytes", "total_inodes", "used_inodes", "available_inodes", "measured_at"]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INODES_FIELD_NUMBER: _ClassVar[int]
    USED_INODES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_INODES_FIELD_NUMBER: _ClassVar[int]
    MEASURED_AT_FIELD_NUMBER: _ClassVar[int]
    total_bytes: int
    used_bytes: int
    available_bytes: int
    total_inodes: int
    used_inodes: int
    available_inodes: int
    measured_at: _timestamp_pb2.Timestamp
    def __init__(self, total_bytes: _Optional[int] = ..., used_bytes: _Optional[int] = ..., available_bytes: _Optional[int] = ..., total_inodes: _Optional[int] = ..., used_inodes: _Optional[int] = ..., available_inodes: _Optional[int] = ..., measured_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConnectDriverInstructions(_message.Message):
    __slots__ = ["drivers"]
    class DriverInstructions(_message.Message):
        __slots__ = ["name", "code", "remarks", "driver_url"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        REMARKS_FIELD_NUMBER: _ClassVar[int]
        DRIVER_URL_FIELD_NUMBER: _ClassVar[int]
        name: str
        code: _containers.RepeatedScalarFieldContainer[str]
        remarks: _containers.RepeatedScalarFieldContainer[str]
        driver_url: str
        def __init__(self, name: _Optional[str] = ..., code: _Optional[_Iterable[str]] = ..., remarks: _Optional[_Iterable[str]] = ..., driver_url: _Optional[str] = ...) -> None: ...
    DRIVERS_FIELD_NUMBER: _ClassVar[int]
    drivers: _containers.RepeatedCompositeFieldContainer[ConnectDriverInstructions.DriverInstructions]
    def __init__(self, drivers: _Optional[_Iterable[_Union[ConnectDriverInstructions.DriverInstructions, _Mapping]]] = ...) -> None: ...

class ImportDataInstructions(_message.Message):
    __slots__ = ["import_dump", "arango_import_json", "arango_import_csv", "arango_import_tsv"]
    IMPORT_DUMP_FIELD_NUMBER: _ClassVar[int]
    ARANGO_IMPORT_JSON_FIELD_NUMBER: _ClassVar[int]
    ARANGO_IMPORT_CSV_FIELD_NUMBER: _ClassVar[int]
    ARANGO_IMPORT_TSV_FIELD_NUMBER: _ClassVar[int]
    import_dump: _containers.RepeatedScalarFieldContainer[str]
    arango_import_json: _containers.RepeatedScalarFieldContainer[str]
    arango_import_csv: _containers.RepeatedScalarFieldContainer[str]
    arango_import_tsv: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, import_dump: _Optional[_Iterable[str]] = ..., arango_import_json: _Optional[_Iterable[str]] = ..., arango_import_csv: _Optional[_Iterable[str]] = ..., arango_import_tsv: _Optional[_Iterable[str]] = ...) -> None: ...

class DeploymentPriceRequest(_message.Message):
    __slots__ = ["organization_id", "project_id", "support_plan_id", "cloud_provider_id", "cloud_region_id", "model", "node_size_id", "node_count", "node_disk_size", "coordinators", "coordinator_memory_size", "dbservers", "dbserver_memory_size", "dbserver_disk_size", "disk_performance_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    COORDINATORS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVERS_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    project_id: str
    support_plan_id: str
    cloud_provider_id: str
    cloud_region_id: str
    model: str
    node_size_id: str
    node_count: int
    node_disk_size: int
    coordinators: int
    coordinator_memory_size: int
    dbservers: int
    dbserver_memory_size: int
    dbserver_disk_size: int
    disk_performance_id: str
    def __init__(self, organization_id: _Optional[str] = ..., project_id: _Optional[str] = ..., support_plan_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., cloud_region_id: _Optional[str] = ..., model: _Optional[str] = ..., node_size_id: _Optional[str] = ..., node_count: _Optional[int] = ..., node_disk_size: _Optional[int] = ..., coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ..., disk_performance_id: _Optional[str] = ...) -> None: ...

class DeploymentPrice(_message.Message):
    __slots__ = ["price_per_hour", "network_transfer_prices", "backup_price", "currency_id", "auditlog_price"]
    class NetworkTransferPrice(_message.Message):
        __slots__ = ["ingress_price_per_gb", "egress_price_per_gb", "description"]
        INGRESS_PRICE_PER_GB_FIELD_NUMBER: _ClassVar[int]
        EGRESS_PRICE_PER_GB_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ingress_price_per_gb: float
        egress_price_per_gb: float
        description: str
        def __init__(self, ingress_price_per_gb: _Optional[float] = ..., egress_price_per_gb: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...
    class BackupPrice(_message.Message):
        __slots__ = ["price_per_gb_per_hour"]
        PRICE_PER_GB_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
        price_per_gb_per_hour: float
        def __init__(self, price_per_gb_per_hour: _Optional[float] = ...) -> None: ...
    class AuditLogPrice(_message.Message):
        __slots__ = ["price_per_gb_per_hour", "https_post_invocation_price_per_1000", "https_post_body_size_price_per_gb"]
        PRICE_PER_GB_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
        HTTPS_POST_INVOCATION_PRICE_PER_1000_FIELD_NUMBER: _ClassVar[int]
        HTTPS_POST_BODY_SIZE_PRICE_PER_GB_FIELD_NUMBER: _ClassVar[int]
        price_per_gb_per_hour: float
        https_post_invocation_price_per_1000: float
        https_post_body_size_price_per_gb: float
        def __init__(self, price_per_gb_per_hour: _Optional[float] = ..., https_post_invocation_price_per_1000: _Optional[float] = ..., https_post_body_size_price_per_gb: _Optional[float] = ...) -> None: ...
    PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TRANSFER_PRICES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_PRICE_FIELD_NUMBER: _ClassVar[int]
    price_per_hour: float
    network_transfer_prices: _containers.RepeatedCompositeFieldContainer[DeploymentPrice.NetworkTransferPrice]
    backup_price: DeploymentPrice.BackupPrice
    currency_id: str
    auditlog_price: DeploymentPrice.AuditLogPrice
    def __init__(self, price_per_hour: _Optional[float] = ..., network_transfer_prices: _Optional[_Iterable[_Union[DeploymentPrice.NetworkTransferPrice, _Mapping]]] = ..., backup_price: _Optional[_Union[DeploymentPrice.BackupPrice, _Mapping]] = ..., currency_id: _Optional[str] = ..., auditlog_price: _Optional[_Union[DeploymentPrice.AuditLogPrice, _Mapping]] = ...) -> None: ...

class DeploymentFeatures(_message.Message):
    __slots__ = ["iamprovider", "pause", "ml"]
    IAMPROVIDER_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    ML_FIELD_NUMBER: _ClassVar[int]
    iamprovider: bool
    pause: bool
    ml: bool
    def __init__(self, iamprovider: bool = ..., pause: bool = ..., ml: bool = ...) -> None: ...

class DeploymentFeaturesRequest(_message.Message):
    __slots__ = ["project_id", "region_id", "model", "node_size_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region_id: str
    model: str
    node_size_id: str
    def __init__(self, project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., model: _Optional[str] = ..., node_size_id: _Optional[str] = ...) -> None: ...

class UpdateDeploymentScheduledRootPasswordRotationRequest(_message.Message):
    __slots__ = ["deployment_id", "enabled"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    enabled: bool
    def __init__(self, deployment_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class ListDiskPerformancesRequest(_message.Message):
    __slots__ = ["region_id", "node_size_id", "dbserver_disk_size", "organization_id", "deployment_id"]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    node_size_id: str
    dbserver_disk_size: int
    organization_id: str
    deployment_id: str
    def __init__(self, region_id: _Optional[str] = ..., node_size_id: _Optional[str] = ..., dbserver_disk_size: _Optional[int] = ..., organization_id: _Optional[str] = ..., deployment_id: _Optional[str] = ...) -> None: ...

class GetDiskPerformanceRequest(_message.Message):
    __slots__ = ["disk_performance_id", "region_id"]
    DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    disk_performance_id: str
    region_id: str
    def __init__(self, disk_performance_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class DiskPerformanceList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DiskPerformance]
    def __init__(self, items: _Optional[_Iterable[_Union[DiskPerformance, _Mapping]]] = ...) -> None: ...

class DiskPerformance(_message.Message):
    __slots__ = ["id", "name", "description", "is_default"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    is_default: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_default: bool = ...) -> None: ...

class ListDeploymentsByFilterRequest(_message.Message):
    __slots__ = ["organization_id", "project_id", "region_id", "expires_after", "expires_before", "does_not_expire", "options"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AFTER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DOES_NOT_EXPIRE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    project_id: str
    region_id: str
    expires_after: _timestamp_pb2.Timestamp
    expires_before: _timestamp_pb2.Timestamp
    does_not_expire: bool
    options: _common_pb2.ListOptions
    def __init__(self, organization_id: _Optional[str] = ..., project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., expires_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., does_not_expire: bool = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...
