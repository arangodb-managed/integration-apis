from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from github.com.golang.protobuf.ptypes.duration import duration_pb2 as _duration_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class CalculateDeploymentSizeRequest(_message.Message):
    __slots__ = ["coordinator_memory_size", "coordinators", "dbserver_disk_size", "dbserver_memory_size", "dbservers", "model", "node_count", "node_disk_size", "node_size_id", "region_id"]
    COORDINATORS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVERS_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    coordinator_memory_size: int
    coordinators: int
    dbserver_disk_size: int
    dbserver_memory_size: int
    dbservers: int
    model: str
    node_count: int
    node_disk_size: int
    node_size_id: str
    region_id: str
    def __init__(self, coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ..., model: _Optional[str] = ..., node_size_id: _Optional[str] = ..., node_count: _Optional[int] = ..., node_disk_size: _Optional[int] = ..., region_id: _Optional[str] = ...) -> None: ...

class ConnectDriverInstructions(_message.Message):
    __slots__ = ["drivers"]
    class DriverInstructions(_message.Message):
        __slots__ = ["code", "driver_url", "name", "remarks"]
        CODE_FIELD_NUMBER: _ClassVar[int]
        DRIVER_URL_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        REMARKS_FIELD_NUMBER: _ClassVar[int]
        code: _containers.RepeatedScalarFieldContainer[str]
        driver_url: str
        name: str
        remarks: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., code: _Optional[_Iterable[str]] = ..., remarks: _Optional[_Iterable[str]] = ..., driver_url: _Optional[str] = ...) -> None: ...
    DRIVERS_FIELD_NUMBER: _ClassVar[int]
    drivers: _containers.RepeatedCompositeFieldContainer[ConnectDriverInstructions.DriverInstructions]
    def __init__(self, drivers: _Optional[_Iterable[_Union[ConnectDriverInstructions.DriverInstructions, _Mapping]]] = ...) -> None: ...

class CreateTestDatabaseRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class CreateTestDatabaseResponse(_message.Message):
    __slots__ = ["db_name", "hostname", "password", "port", "username"]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    hostname: str
    password: str
    port: str
    username: str
    def __init__(self, db_name: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., hostname: _Optional[str] = ..., port: _Optional[str] = ...) -> None: ...

class DataVolumeInfo(_message.Message):
    __slots__ = ["available_bytes", "available_inodes", "measured_at", "total_bytes", "total_inodes", "used_bytes", "used_inodes"]
    AVAILABLE_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_INODES_FIELD_NUMBER: _ClassVar[int]
    MEASURED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INODES_FIELD_NUMBER: _ClassVar[int]
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_INODES_FIELD_NUMBER: _ClassVar[int]
    available_bytes: int
    available_inodes: int
    measured_at: _timestamp_pb2.Timestamp
    total_bytes: int
    total_inodes: int
    used_bytes: int
    used_inodes: int
    def __init__(self, total_bytes: _Optional[int] = ..., used_bytes: _Optional[int] = ..., available_bytes: _Optional[int] = ..., total_inodes: _Optional[int] = ..., used_inodes: _Optional[int] = ..., available_inodes: _Optional[int] = ..., measured_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Deployment(_message.Message):
    __slots__ = ["accepted_terms_and_conditions_id", "backup_restore", "certificates", "clone_backup_id", "created_at", "created_by_id", "custom_image", "deleted_at", "deployment_profile_id", "deployment_recommendations", "description", "disable_foxx_authentication", "disk_auto_size_settings", "disk_performance_id", "disk_performance_locked", "disk_rate_limit_active", "disk_rate_limit_period", "expiration", "iamprovider_id", "id", "ipallowlist_id", "is_clone", "is_deleted", "is_paused", "is_prepaid_deployment_update_available", "is_scheduled_root_password_rotation_enabled", "last_disk_performance_updated_at", "last_disk_size_updated_at", "last_paused_at", "last_resumed_at", "last_root_password_rotated_at", "locked", "model", "name", "notification_settings", "prepaid_deployment_ends_at", "prepaid_deployment_id", "prepaid_deployment_starts_at", "private_endpoint", "project_id", "region_id", "replace_version_by", "servers", "size", "status", "support_plan_id", "upgrade_recommendation", "url", "version", "version_is_end_of_life"]
    class BackupRestoreSpec(_message.Message):
        __slots__ = ["backup_id", "last_updated_at", "revision"]
        BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        backup_id: str
        last_updated_at: _timestamp_pb2.Timestamp
        revision: int
        def __init__(self, revision: _Optional[int] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backup_id: _Optional[str] = ...) -> None: ...
    class BackupRestoreStatus(_message.Message):
        __slots__ = ["failure_reason", "restoring", "revision", "status"]
        FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
        RESTORING_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        failure_reason: str
        restoring: bool
        revision: int
        status: str
        def __init__(self, revision: _Optional[int] = ..., restoring: bool = ..., status: _Optional[str] = ..., failure_reason: _Optional[str] = ...) -> None: ...
    class CertificateSpec(_message.Message):
        __slots__ = ["alternate_dns_names", "ca_certificate_id"]
        ALTERNATE_DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
        CA_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
        alternate_dns_names: _containers.RepeatedScalarFieldContainer[str]
        ca_certificate_id: str
        def __init__(self, ca_certificate_id: _Optional[str] = ..., alternate_dns_names: _Optional[_Iterable[str]] = ...) -> None: ...
    class DiskAutoSizeSettings(_message.Message):
        __slots__ = ["maximum_node_disk_size"]
        MAXIMUM_NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        maximum_node_disk_size: int
        def __init__(self, maximum_node_disk_size: _Optional[int] = ...) -> None: ...
    class Expiration(_message.Message):
        __slots__ = ["expires_at", "last_warning_email_send_at", "last_warning_email_send_to", "reason"]
        EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
        LAST_WARNING_EMAIL_SEND_AT_FIELD_NUMBER: _ClassVar[int]
        LAST_WARNING_EMAIL_SEND_TO_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        expires_at: _timestamp_pb2.Timestamp
        last_warning_email_send_at: _timestamp_pb2.Timestamp
        last_warning_email_send_to: _containers.RepeatedScalarFieldContainer[str]
        reason: str
        def __init__(self, expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ..., last_warning_email_send_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_warning_email_send_to: _Optional[_Iterable[str]] = ...) -> None: ...
    class ModelSpec(_message.Message):
        __slots__ = ["model", "node_count", "node_disk_size", "node_size_id"]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
        model: str
        node_count: int
        node_disk_size: int
        node_size_id: str
        def __init__(self, model: _Optional[str] = ..., node_size_id: _Optional[str] = ..., node_count: _Optional[int] = ..., node_disk_size: _Optional[int] = ...) -> None: ...
    class NotificationSettings(_message.Message):
        __slots__ = ["email_addresses"]
        EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        email_addresses: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, email_addresses: _Optional[_Iterable[str]] = ...) -> None: ...
    class ServerStatus(_message.Message):
        __slots__ = ["bad", "can_be_deleted", "created_at", "creating", "data_volume_info", "description", "failed", "id", "is_leader", "last_cpu_limit", "last_cpu_usage", "last_memory_limit", "last_memory_usage", "last_started_at", "member_of_cluster", "ok", "ready", "recent_restarts", "rotation_pending", "type", "upgrading", "version"]
        BAD_FIELD_NUMBER: _ClassVar[int]
        CAN_BE_DELETED_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        CREATING_FIELD_NUMBER: _ClassVar[int]
        DATA_VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_LEADER_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        LAST_CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        LAST_MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        MEMBER_OF_CLUSTER_FIELD_NUMBER: _ClassVar[int]
        OK_FIELD_NUMBER: _ClassVar[int]
        READY_FIELD_NUMBER: _ClassVar[int]
        RECENT_RESTARTS_FIELD_NUMBER: _ClassVar[int]
        ROTATION_PENDING_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UPGRADING_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        bad: bool
        can_be_deleted: bool
        created_at: _timestamp_pb2.Timestamp
        creating: bool
        data_volume_info: DataVolumeInfo
        description: str
        failed: bool
        id: str
        is_leader: bool
        last_cpu_limit: float
        last_cpu_usage: float
        last_memory_limit: int
        last_memory_usage: int
        last_started_at: _timestamp_pb2.Timestamp
        member_of_cluster: bool
        ok: bool
        ready: bool
        recent_restarts: int
        rotation_pending: bool
        type: str
        upgrading: bool
        version: str
        def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ready: bool = ..., member_of_cluster: bool = ..., failed: bool = ..., creating: bool = ..., ok: bool = ..., bad: bool = ..., upgrading: bool = ..., version: _Optional[str] = ..., last_started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rotation_pending: bool = ..., can_be_deleted: bool = ..., is_leader: bool = ..., data_volume_info: _Optional[_Union[DataVolumeInfo, _Mapping]] = ..., recent_restarts: _Optional[int] = ..., last_memory_usage: _Optional[int] = ..., last_cpu_usage: _Optional[float] = ..., last_memory_limit: _Optional[int] = ..., last_cpu_limit: _Optional[float] = ...) -> None: ...
    class ServersSpec(_message.Message):
        __slots__ = ["coordinator_args", "coordinator_memory_size", "coordinators", "dbserver_args", "dbserver_disk_size", "dbserver_memory_size", "dbservers", "minimum_dbservers_count"]
        COORDINATORS_FIELD_NUMBER: _ClassVar[int]
        COORDINATOR_ARGS_FIELD_NUMBER: _ClassVar[int]
        COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        DBSERVERS_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_ARGS_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_DBSERVERS_COUNT_FIELD_NUMBER: _ClassVar[int]
        coordinator_args: _containers.RepeatedScalarFieldContainer[str]
        coordinator_memory_size: int
        coordinators: int
        dbserver_args: _containers.RepeatedScalarFieldContainer[str]
        dbserver_disk_size: int
        dbserver_memory_size: int
        dbservers: int
        minimum_dbservers_count: int
        def __init__(self, coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., coordinator_args: _Optional[_Iterable[str]] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ..., dbserver_args: _Optional[_Iterable[str]] = ..., minimum_dbservers_count: _Optional[int] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["backup_restore_status", "backup_upload_in_progress", "bootstrapped", "bootstrapped_at", "created", "description", "endpoint", "endpoint_private_endpoint", "endpoint_private_endpoint_self_signed", "endpoint_self_signed", "is_up_to_date", "private_endpoint", "private_endpoint_only", "ready", "server_versions", "servers", "total_backup_size_bytes", "upgrading"]
        BACKUP_RESTORE_STATUS_FIELD_NUMBER: _ClassVar[int]
        BACKUP_UPLOAD_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        BOOTSTRAPPED_AT_FIELD_NUMBER: _ClassVar[int]
        BOOTSTRAPPED_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_PRIVATE_ENDPOINT_SELF_SIGNED_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_SELF_SIGNED_FIELD_NUMBER: _ClassVar[int]
        IS_UP_TO_DATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_ONLY_FIELD_NUMBER: _ClassVar[int]
        READY_FIELD_NUMBER: _ClassVar[int]
        SERVERS_FIELD_NUMBER: _ClassVar[int]
        SERVER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        UPGRADING_FIELD_NUMBER: _ClassVar[int]
        backup_restore_status: Deployment.BackupRestoreStatus
        backup_upload_in_progress: bool
        bootstrapped: bool
        bootstrapped_at: _timestamp_pb2.Timestamp
        created: bool
        description: str
        endpoint: str
        endpoint_private_endpoint: str
        endpoint_private_endpoint_self_signed: str
        endpoint_self_signed: str
        is_up_to_date: bool
        private_endpoint: bool
        private_endpoint_only: bool
        ready: bool
        server_versions: _containers.RepeatedScalarFieldContainer[str]
        servers: _containers.RepeatedCompositeFieldContainer[Deployment.ServerStatus]
        total_backup_size_bytes: int
        upgrading: bool
        def __init__(self, endpoint: _Optional[str] = ..., description: _Optional[str] = ..., created: bool = ..., ready: bool = ..., upgrading: bool = ..., server_versions: _Optional[_Iterable[str]] = ..., servers: _Optional[_Iterable[_Union[Deployment.ServerStatus, _Mapping]]] = ..., bootstrapped_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., bootstrapped: bool = ..., endpoint_self_signed: _Optional[str] = ..., private_endpoint: bool = ..., private_endpoint_only: bool = ..., endpoint_private_endpoint: _Optional[str] = ..., endpoint_private_endpoint_self_signed: _Optional[str] = ..., backup_restore_status: _Optional[_Union[Deployment.BackupRestoreStatus, _Mapping]] = ..., total_backup_size_bytes: _Optional[int] = ..., backup_upload_in_progress: bool = ..., is_up_to_date: bool = ...) -> None: ...
    ACCEPTED_TERMS_AND_CONDITIONS_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RESTORE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    CLONE_BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_IMAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FOXX_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    DISK_AUTO_SIZE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_PERFORMANCE_LOCKED_FIELD_NUMBER: _ClassVar[int]
    DISK_RATE_LIMIT_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DISK_RATE_LIMIT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    IAMPROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IPALLOWLIST_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CLONE_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    IS_PREPAID_DEPLOYMENT_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_SCHEDULED_ROOT_PASSWORD_ROTATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_DISK_PERFORMANCE_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_DISK_SIZE_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RESUMED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ROOT_PASSWORD_ROTATED_AT_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PREPAID_DEPLOYMENT_ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    PREPAID_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PREPAID_DEPLOYMENT_STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLACE_VERSION_BY_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_IS_END_OF_LIFE_FIELD_NUMBER: _ClassVar[int]
    accepted_terms_and_conditions_id: str
    backup_restore: Deployment.BackupRestoreSpec
    certificates: Deployment.CertificateSpec
    clone_backup_id: str
    created_at: _timestamp_pb2.Timestamp
    created_by_id: str
    custom_image: str
    deleted_at: _timestamp_pb2.Timestamp
    deployment_profile_id: str
    deployment_recommendations: _containers.RepeatedCompositeFieldContainer[DeploymentSizeRecommendation]
    description: str
    disable_foxx_authentication: bool
    disk_auto_size_settings: Deployment.DiskAutoSizeSettings
    disk_performance_id: str
    disk_performance_locked: bool
    disk_rate_limit_active: _duration_pb2.Duration
    disk_rate_limit_period: _duration_pb2.Duration
    expiration: Deployment.Expiration
    iamprovider_id: str
    id: str
    ipallowlist_id: str
    is_clone: bool
    is_deleted: bool
    is_paused: bool
    is_prepaid_deployment_update_available: bool
    is_scheduled_root_password_rotation_enabled: bool
    last_disk_performance_updated_at: _timestamp_pb2.Timestamp
    last_disk_size_updated_at: _timestamp_pb2.Timestamp
    last_paused_at: _timestamp_pb2.Timestamp
    last_resumed_at: _timestamp_pb2.Timestamp
    last_root_password_rotated_at: _timestamp_pb2.Timestamp
    locked: bool
    model: Deployment.ModelSpec
    name: str
    notification_settings: Deployment.NotificationSettings
    prepaid_deployment_ends_at: _timestamp_pb2.Timestamp
    prepaid_deployment_id: str
    prepaid_deployment_starts_at: _timestamp_pb2.Timestamp
    private_endpoint: bool
    project_id: str
    region_id: str
    replace_version_by: ReplaceVersionBy
    servers: Deployment.ServersSpec
    size: DeploymentSize
    status: Deployment.Status
    support_plan_id: str
    upgrade_recommendation: UpgradeVersionRecommendation
    url: str
    version: str
    version_is_end_of_life: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., support_plan_id: _Optional[str] = ..., created_by_id: _Optional[str] = ..., accepted_terms_and_conditions_id: _Optional[str] = ..., locked: bool = ..., is_paused: bool = ..., last_paused_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_resumed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., prepaid_deployment_id: _Optional[str] = ..., disable_foxx_authentication: bool = ..., prepaid_deployment_starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., prepaid_deployment_ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_prepaid_deployment_update_available: bool = ..., private_endpoint: bool = ..., version: _Optional[str] = ..., replace_version_by: _Optional[_Union[ReplaceVersionBy, _Mapping]] = ..., upgrade_recommendation: _Optional[_Union[UpgradeVersionRecommendation, _Mapping]] = ..., version_is_end_of_life: bool = ..., certificates: _Optional[_Union[Deployment.CertificateSpec, _Mapping]] = ..., servers: _Optional[_Union[Deployment.ServersSpec, _Mapping]] = ..., ipallowlist_id: _Optional[str] = ..., model: _Optional[_Union[Deployment.ModelSpec, _Mapping]] = ..., custom_image: _Optional[str] = ..., iamprovider_id: _Optional[str] = ..., disk_performance_id: _Optional[str] = ..., disk_performance_locked: bool = ..., disk_rate_limit_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., last_disk_performance_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_disk_size_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., disk_rate_limit_active: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., status: _Optional[_Union[Deployment.Status, _Mapping]] = ..., size: _Optional[_Union[DeploymentSize, _Mapping]] = ..., expiration: _Optional[_Union[Deployment.Expiration, _Mapping]] = ..., backup_restore: _Optional[_Union[Deployment.BackupRestoreSpec, _Mapping]] = ..., deployment_recommendations: _Optional[_Iterable[_Union[DeploymentSizeRecommendation, _Mapping]]] = ..., is_clone: bool = ..., clone_backup_id: _Optional[str] = ..., notification_settings: _Optional[_Union[Deployment.NotificationSettings, _Mapping]] = ..., disk_auto_size_settings: _Optional[_Union[Deployment.DiskAutoSizeSettings, _Mapping]] = ..., is_scheduled_root_password_rotation_enabled: bool = ..., last_root_password_rotated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployment_profile_id: _Optional[str] = ...) -> None: ...

class DeploymentCredentials(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class DeploymentCredentialsRequest(_message.Message):
    __slots__ = ["deployment_id", "reason"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    reason: str
    def __init__(self, deployment_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DeploymentFeatures(_message.Message):
    __slots__ = ["iamprovider"]
    IAMPROVIDER_FIELD_NUMBER: _ClassVar[int]
    iamprovider: bool
    def __init__(self, iamprovider: bool = ...) -> None: ...

class DeploymentFeaturesRequest(_message.Message):
    __slots__ = ["model", "node_size_id", "project_id", "region_id"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    model: str
    node_size_id: str
    project_id: str
    region_id: str
    def __init__(self, project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., model: _Optional[str] = ..., node_size_id: _Optional[str] = ...) -> None: ...

class DeploymentList(_message.Message):
    __slots__ = ["budget", "items"]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    budget: _common_pb2.Budget
    items: _containers.RepeatedCompositeFieldContainer[Deployment]
    def __init__(self, items: _Optional[_Iterable[_Union[Deployment, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

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

class DeploymentPrice(_message.Message):
    __slots__ = ["auditlog_price", "backup_price", "currency_id", "network_transfer_prices", "price_per_hour"]
    class AuditLogPrice(_message.Message):
        __slots__ = ["https_post_body_size_price_per_gb", "https_post_invocation_price_per_1000", "price_per_gb_per_hour"]
        HTTPS_POST_BODY_SIZE_PRICE_PER_GB_FIELD_NUMBER: _ClassVar[int]
        HTTPS_POST_INVOCATION_PRICE_PER_1000_FIELD_NUMBER: _ClassVar[int]
        PRICE_PER_GB_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
        https_post_body_size_price_per_gb: float
        https_post_invocation_price_per_1000: float
        price_per_gb_per_hour: float
        def __init__(self, price_per_gb_per_hour: _Optional[float] = ..., https_post_invocation_price_per_1000: _Optional[float] = ..., https_post_body_size_price_per_gb: _Optional[float] = ...) -> None: ...
    class BackupPrice(_message.Message):
        __slots__ = ["price_per_gb_per_hour"]
        PRICE_PER_GB_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
        price_per_gb_per_hour: float
        def __init__(self, price_per_gb_per_hour: _Optional[float] = ...) -> None: ...
    class NetworkTransferPrice(_message.Message):
        __slots__ = ["description", "egress_price_per_gb", "ingress_price_per_gb"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        EGRESS_PRICE_PER_GB_FIELD_NUMBER: _ClassVar[int]
        INGRESS_PRICE_PER_GB_FIELD_NUMBER: _ClassVar[int]
        description: str
        egress_price_per_gb: float
        ingress_price_per_gb: float
        def __init__(self, ingress_price_per_gb: _Optional[float] = ..., egress_price_per_gb: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...
    AUDITLOG_PRICE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TRANSFER_PRICES_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    auditlog_price: DeploymentPrice.AuditLogPrice
    backup_price: DeploymentPrice.BackupPrice
    currency_id: str
    network_transfer_prices: _containers.RepeatedCompositeFieldContainer[DeploymentPrice.NetworkTransferPrice]
    price_per_hour: float
    def __init__(self, price_per_hour: _Optional[float] = ..., network_transfer_prices: _Optional[_Iterable[_Union[DeploymentPrice.NetworkTransferPrice, _Mapping]]] = ..., backup_price: _Optional[_Union[DeploymentPrice.BackupPrice, _Mapping]] = ..., currency_id: _Optional[str] = ..., auditlog_price: _Optional[_Union[DeploymentPrice.AuditLogPrice, _Mapping]] = ...) -> None: ...

class DeploymentPriceRequest(_message.Message):
    __slots__ = ["cloud_provider_id", "cloud_region_id", "coordinator_memory_size", "coordinators", "dbserver_disk_size", "dbserver_memory_size", "dbservers", "disk_performance_id", "model", "node_count", "node_disk_size", "node_size_id", "organization_id", "project_id", "support_plan_id"]
    CLOUD_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    COORDINATORS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVERS_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_provider_id: str
    cloud_region_id: str
    coordinator_memory_size: int
    coordinators: int
    dbserver_disk_size: int
    dbserver_memory_size: int
    dbservers: int
    disk_performance_id: str
    model: str
    node_count: int
    node_disk_size: int
    node_size_id: str
    organization_id: str
    project_id: str
    support_plan_id: str
    def __init__(self, organization_id: _Optional[str] = ..., project_id: _Optional[str] = ..., support_plan_id: _Optional[str] = ..., cloud_provider_id: _Optional[str] = ..., cloud_region_id: _Optional[str] = ..., model: _Optional[str] = ..., node_size_id: _Optional[str] = ..., node_count: _Optional[int] = ..., node_disk_size: _Optional[int] = ..., coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ..., disk_performance_id: _Optional[str] = ...) -> None: ...

class DeploymentSize(_message.Message):
    __slots__ = ["agent_disk_size", "agent_memory_size", "agents", "coordinator_memory_size", "coordinators", "dbserver_disk_size", "dbserver_memory_size", "dbservers", "total_disk_size", "total_memory_size"]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    AGENT_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    COORDINATORS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVERS_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    agent_disk_size: int
    agent_memory_size: int
    agents: int
    coordinator_memory_size: int
    coordinators: int
    dbserver_disk_size: int
    dbserver_memory_size: int
    dbservers: int
    total_disk_size: int
    total_memory_size: int
    def __init__(self, agents: _Optional[int] = ..., agent_memory_size: _Optional[int] = ..., agent_disk_size: _Optional[int] = ..., total_memory_size: _Optional[int] = ..., total_disk_size: _Optional[int] = ..., coordinators: _Optional[int] = ..., coordinator_memory_size: _Optional[int] = ..., dbservers: _Optional[int] = ..., dbserver_memory_size: _Optional[int] = ..., dbserver_disk_size: _Optional[int] = ...) -> None: ...

class DeploymentSizeRecommendation(_message.Message):
    __slots__ = ["created_at", "exceeds_platform", "exceeds_quota", "node_count", "node_disk_size", "node_memory_size", "request"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXCEEDS_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    EXCEEDS_QUOTA_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NODE_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    exceeds_platform: bool
    exceeds_quota: bool
    node_count: int
    node_disk_size: int
    node_memory_size: int
    request: DeploymentSizeRequest
    def __init__(self, request: _Optional[_Union[DeploymentSizeRequest, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., node_memory_size: _Optional[int] = ..., node_disk_size: _Optional[int] = ..., node_count: _Optional[int] = ..., exceeds_quota: bool = ..., exceeds_platform: bool = ...) -> None: ...

class DeploymentSizeRequest(_message.Message):
    __slots__ = ["access_create_percentage", "access_read_percentage", "access_update_percentage", "dataset_size", "file_format", "growth_rate", "model", "number_of_columns", "number_of_documents", "project_id", "region_id", "replication_factor", "usecase", "working_set_percentage"]
    ACCESS_CREATE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_READ_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_UPDATE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    DATASET_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    GROWTH_RATE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    USECASE_FIELD_NUMBER: _ClassVar[int]
    WORKING_SET_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    access_create_percentage: float
    access_read_percentage: float
    access_update_percentage: float
    dataset_size: int
    file_format: str
    growth_rate: float
    model: str
    number_of_columns: int
    number_of_documents: int
    project_id: str
    region_id: str
    replication_factor: int
    usecase: str
    working_set_percentage: float
    def __init__(self, dataset_size: _Optional[int] = ..., usecase: _Optional[str] = ..., model: _Optional[str] = ..., file_format: _Optional[str] = ..., number_of_documents: _Optional[int] = ..., number_of_columns: _Optional[int] = ..., working_set_percentage: _Optional[float] = ..., access_read_percentage: _Optional[float] = ..., access_create_percentage: _Optional[float] = ..., access_update_percentage: _Optional[float] = ..., growth_rate: _Optional[float] = ..., replication_factor: _Optional[int] = ..., project_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class DiskPerformance(_message.Message):
    __slots__ = ["description", "id", "is_default", "name"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    is_default: bool
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_default: bool = ...) -> None: ...

class DiskPerformanceList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DiskPerformance]
    def __init__(self, items: _Optional[_Iterable[_Union[DiskPerformance, _Mapping]]] = ...) -> None: ...

class GetDiskPerformanceRequest(_message.Message):
    __slots__ = ["disk_performance_id", "region_id"]
    DISK_PERFORMANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    disk_performance_id: str
    region_id: str
    def __init__(self, disk_performance_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class ImportDataInstructions(_message.Message):
    __slots__ = ["arango_import_csv", "arango_import_json", "arango_import_tsv", "import_dump"]
    ARANGO_IMPORT_CSV_FIELD_NUMBER: _ClassVar[int]
    ARANGO_IMPORT_JSON_FIELD_NUMBER: _ClassVar[int]
    ARANGO_IMPORT_TSV_FIELD_NUMBER: _ClassVar[int]
    IMPORT_DUMP_FIELD_NUMBER: _ClassVar[int]
    arango_import_csv: _containers.RepeatedScalarFieldContainer[str]
    arango_import_json: _containers.RepeatedScalarFieldContainer[str]
    arango_import_tsv: _containers.RepeatedScalarFieldContainer[str]
    import_dump: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, import_dump: _Optional[_Iterable[str]] = ..., arango_import_json: _Optional[_Iterable[str]] = ..., arango_import_csv: _Optional[_Iterable[str]] = ..., arango_import_tsv: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCPUSizesRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class ListDeploymentModelsRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class ListDeploymentsByFilterRequest(_message.Message):
    __slots__ = ["does_not_expire", "expires_after", "expires_before", "options", "organization_id", "project_id", "region_id"]
    DOES_NOT_EXPIRE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AFTER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_BEFORE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    does_not_expire: bool
    expires_after: _timestamp_pb2.Timestamp
    expires_before: _timestamp_pb2.Timestamp
    options: _common_pb2.ListOptions
    organization_id: str
    project_id: str
    region_id: str
    def __init__(self, organization_id: _Optional[str] = ..., project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., expires_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., does_not_expire: bool = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class ListDiskPerformancesRequest(_message.Message):
    __slots__ = ["dbserver_disk_size", "deployment_id", "node_size_id", "region_id"]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_SIZE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    dbserver_disk_size: int
    deployment_id: str
    node_size_id: str
    region_id: str
    def __init__(self, region_id: _Optional[str] = ..., node_size_id: _Optional[str] = ..., dbserver_disk_size: _Optional[int] = ..., deployment_id: _Optional[str] = ...) -> None: ...

class ListVersionsRequest(_message.Message):
    __slots__ = ["current_version", "options", "organization_id"]
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    current_version: str
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., organization_id: _Optional[str] = ..., current_version: _Optional[str] = ...) -> None: ...

class NodeSize(_message.Message):
    __slots__ = ["cpu_size", "disk_sizes", "id", "max_disk_size", "memory_size", "min_disk_size", "name"]
    CPU_SIZE_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIN_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    cpu_size: str
    disk_sizes: _containers.RepeatedScalarFieldContainer[int]
    id: str
    max_disk_size: int
    memory_size: int
    min_disk_size: int
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., memory_size: _Optional[int] = ..., min_disk_size: _Optional[int] = ..., max_disk_size: _Optional[int] = ..., cpu_size: _Optional[str] = ..., disk_sizes: _Optional[_Iterable[int]] = ...) -> None: ...

class NodeSizeList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[NodeSize]
    def __init__(self, items: _Optional[_Iterable[_Union[NodeSize, _Mapping]]] = ...) -> None: ...

class NodeSizesRequest(_message.Message):
    __slots__ = ["deployment_id", "model", "organization_id", "project_id", "region_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    model: str
    organization_id: str
    project_id: str
    region_id: str
    def __init__(self, project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., model: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class RebalanceDeploymentShardsRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class ReplaceVersionBy(_message.Message):
    __slots__ = ["auto_update_date", "reason", "version"]
    AUTO_UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    auto_update_date: _timestamp_pb2.Timestamp
    reason: str
    version: str
    def __init__(self, version: _Optional[str] = ..., reason: _Optional[str] = ..., auto_update_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RotateDeploymentServerRequest(_message.Message):
    __slots__ = ["deployment_id", "server_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    server_id: str
    def __init__(self, deployment_id: _Optional[str] = ..., server_id: _Optional[str] = ...) -> None: ...

class ServersSpecLimits(_message.Message):
    __slots__ = ["coordinator_memory_size", "coordinators", "dbserver_disk_size", "dbserver_memory_size", "dbservers", "node_count", "node_memory_size"]
    class Limits(_message.Message):
        __slots__ = ["allowed_values", "max", "min"]
        ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        allowed_values: _containers.RepeatedScalarFieldContainer[int]
        max: int
        min: int
        def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ..., allowed_values: _Optional[_Iterable[int]] = ...) -> None: ...
    COORDINATORS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVERS_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    DBSERVER_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    coordinator_memory_size: ServersSpecLimits.Limits
    coordinators: ServersSpecLimits.Limits
    dbserver_disk_size: ServersSpecLimits.Limits
    dbserver_memory_size: ServersSpecLimits.Limits
    dbservers: ServersSpecLimits.Limits
    node_count: ServersSpecLimits.Limits
    node_memory_size: ServersSpecLimits.Limits
    def __init__(self, coordinators: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., coordinator_memory_size: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., dbservers: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., dbserver_memory_size: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., dbserver_disk_size: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., node_memory_size: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ..., node_count: _Optional[_Union[ServersSpecLimits.Limits, _Mapping]] = ...) -> None: ...

class ServersSpecLimitsRequest(_message.Message):
    __slots__ = ["deployment_id", "project_id", "region_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    project_id: str
    region_id: str
    def __init__(self, project_id: _Optional[str] = ..., region_id: _Optional[str] = ..., deployment_id: _Optional[str] = ...) -> None: ...

class UpdateDeploymentScheduledRootPasswordRotationRequest(_message.Message):
    __slots__ = ["deployment_id", "enabled"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    enabled: bool
    def __init__(self, deployment_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class UpgradeVersionRecommendation(_message.Message):
    __slots__ = ["reason", "version"]
    REASON_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    reason: str
    version: str
    def __init__(self, version: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ["is_end_of_life", "replace_by", "upgrade_recommendation", "version"]
    IS_END_OF_LIFE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_BY_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    is_end_of_life: bool
    replace_by: ReplaceVersionBy
    upgrade_recommendation: UpgradeVersionRecommendation
    version: str
    def __init__(self, version: _Optional[str] = ..., replace_by: _Optional[_Union[ReplaceVersionBy, _Mapping]] = ..., upgrade_recommendation: _Optional[_Union[UpgradeVersionRecommendation, _Mapping]] = ..., is_end_of_life: bool = ...) -> None: ...

class VersionList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Version]
    def __init__(self, items: _Optional[_Iterable[_Union[Version, _Mapping]]] = ...) -> None: ...
