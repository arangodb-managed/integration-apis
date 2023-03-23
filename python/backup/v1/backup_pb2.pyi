from data.v1 import data_pb2 as _data_pb2
from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from github.com.golang.protobuf.ptypes.duration import duration_pb2 as _duration_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Backup(_message.Message):
    __slots__ = ["auto_deleted_at", "backup_policy_id", "created_at", "deleted_at", "deployment_id", "deployment_info", "description", "download", "id", "is_deleted", "name", "region_id", "source_backup_id", "status", "upload", "upload_updated_at", "url"]
    class DeploymentInfo(_message.Message):
        __slots__ = ["model", "servers", "version"]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        SERVERS_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        model: _data_pb2.Deployment.ModelSpec
        servers: _data_pb2.Deployment.ServersSpec
        version: str
        def __init__(self, version: _Optional[str] = ..., servers: _Optional[_Union[_data_pb2.Deployment.ServersSpec, _Mapping]] = ..., model: _Optional[_Union[_data_pb2.Deployment.ModelSpec, _Mapping]] = ...) -> None: ...
    class DownloadSpec(_message.Message):
        __slots__ = ["last_updated_at", "revision"]
        LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        last_updated_at: _timestamp_pb2.Timestamp
        revision: int
        def __init__(self, revision: _Optional[int] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class DownloadStatus(_message.Message):
        __slots__ = ["downloaded", "downloaded_at", "revision"]
        DOWNLOADED_AT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        downloaded: bool
        downloaded_at: _timestamp_pb2.Timestamp
        revision: int
        def __init__(self, revision: _Optional[int] = ..., downloaded: bool = ..., downloaded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["available", "created_at", "dbservers", "download_status", "is_failed", "message", "progress", "size_bytes", "state", "upload_only", "upload_status", "version"]
        AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        DBSERVERS_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
        IS_FAILED_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ONLY_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        available: bool
        created_at: _timestamp_pb2.Timestamp
        dbservers: int
        download_status: Backup.DownloadStatus
        is_failed: bool
        message: str
        progress: str
        size_bytes: int
        state: str
        upload_only: bool
        upload_status: Backup.UploadStatus
        version: str
        def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[str] = ..., state: _Optional[str] = ..., is_failed: bool = ..., message: _Optional[str] = ..., progress: _Optional[str] = ..., size_bytes: _Optional[int] = ..., available: bool = ..., dbservers: _Optional[int] = ..., upload_only: bool = ..., upload_status: _Optional[_Union[Backup.UploadStatus, _Mapping]] = ..., download_status: _Optional[_Union[Backup.DownloadStatus, _Mapping]] = ...) -> None: ...
    class UploadStatus(_message.Message):
        __slots__ = ["size_bytes", "uploaded", "uploaded_at"]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        UPLOADED_AT_FIELD_NUMBER: _ClassVar[int]
        UPLOADED_FIELD_NUMBER: _ClassVar[int]
        size_bytes: int
        uploaded: bool
        uploaded_at: _timestamp_pb2.Timestamp
        def __init__(self, uploaded: bool = ..., uploaded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., size_bytes: _Optional[int] = ...) -> None: ...
    AUTO_DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    auto_deleted_at: _timestamp_pb2.Timestamp
    backup_policy_id: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    deployment_id: str
    deployment_info: Backup.DeploymentInfo
    description: str
    download: Backup.DownloadSpec
    id: str
    is_deleted: bool
    name: str
    region_id: str
    source_backup_id: str
    status: Backup.Status
    upload: bool
    upload_updated_at: _timestamp_pb2.Timestamp
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., deployment_id: _Optional[str] = ..., backup_policy_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., auto_deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployment_info: _Optional[_Union[Backup.DeploymentInfo, _Mapping]] = ..., upload: bool = ..., upload_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., download: _Optional[_Union[Backup.DownloadSpec, _Mapping]] = ..., status: _Optional[_Union[Backup.Status, _Mapping]] = ..., region_id: _Optional[str] = ..., source_backup_id: _Optional[str] = ...) -> None: ...

class BackupList(_message.Message):
    __slots__ = ["budget", "items"]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    budget: _common_pb2.Budget
    items: _containers.RepeatedCompositeFieldContainer[Backup]
    def __init__(self, items: _Optional[_Iterable[_Union[Backup, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class BackupPolicy(_message.Message):
    __slots__ = ["additional_region_ids", "created_at", "deleted_at", "deployment_id", "description", "email_notification", "id", "is_deleted", "is_paused", "locked", "name", "retention_period", "schedule", "status", "upload", "url"]
    class DailySchedule(_message.Message):
        __slots__ = ["friday", "monday", "saturday", "schedule_at", "sunday", "thursday", "tuesday", "wednesday"]
        FRIDAY_FIELD_NUMBER: _ClassVar[int]
        MONDAY_FIELD_NUMBER: _ClassVar[int]
        SATURDAY_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_AT_FIELD_NUMBER: _ClassVar[int]
        SUNDAY_FIELD_NUMBER: _ClassVar[int]
        THURSDAY_FIELD_NUMBER: _ClassVar[int]
        TUESDAY_FIELD_NUMBER: _ClassVar[int]
        WEDNESDAY_FIELD_NUMBER: _ClassVar[int]
        friday: bool
        monday: bool
        saturday: bool
        schedule_at: TimeOfDay
        sunday: bool
        thursday: bool
        tuesday: bool
        wednesday: bool
        def __init__(self, monday: bool = ..., tuesday: bool = ..., wednesday: bool = ..., thursday: bool = ..., friday: bool = ..., saturday: bool = ..., sunday: bool = ..., schedule_at: _Optional[_Union[TimeOfDay, _Mapping]] = ...) -> None: ...
    class HourlySchedule(_message.Message):
        __slots__ = ["minutes_offset", "schedule_every_interval_hours"]
        MINUTES_OFFSET_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_EVERY_INTERVAL_HOURS_FIELD_NUMBER: _ClassVar[int]
        minutes_offset: int
        schedule_every_interval_hours: int
        def __init__(self, schedule_every_interval_hours: _Optional[int] = ..., minutes_offset: _Optional[int] = ...) -> None: ...
    class MonthlySchedule(_message.Message):
        __slots__ = ["day_of_month", "schedule_at"]
        DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_AT_FIELD_NUMBER: _ClassVar[int]
        day_of_month: int
        schedule_at: TimeOfDay
        def __init__(self, day_of_month: _Optional[int] = ..., schedule_at: _Optional[_Union[TimeOfDay, _Mapping]] = ...) -> None: ...
    class Schedule(_message.Message):
        __slots__ = ["daily_schedule", "hourly_schedule", "monthly_schedule", "schedule_type"]
        DAILY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        HOURLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
        daily_schedule: BackupPolicy.DailySchedule
        hourly_schedule: BackupPolicy.HourlySchedule
        monthly_schedule: BackupPolicy.MonthlySchedule
        schedule_type: str
        def __init__(self, schedule_type: _Optional[str] = ..., hourly_schedule: _Optional[_Union[BackupPolicy.HourlySchedule, _Mapping]] = ..., daily_schedule: _Optional[_Union[BackupPolicy.DailySchedule, _Mapping]] = ..., monthly_schedule: _Optional[_Union[BackupPolicy.MonthlySchedule, _Mapping]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["message", "next_backup"]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NEXT_BACKUP_FIELD_NUMBER: _ClassVar[int]
        message: str
        next_backup: _timestamp_pb2.Timestamp
        def __init__(self, next_backup: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...
    ADDITIONAL_REGION_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    additional_region_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    deployment_id: str
    description: str
    email_notification: str
    id: str
    is_deleted: bool
    is_paused: bool
    locked: bool
    name: str
    retention_period: _duration_pb2.Duration
    schedule: BackupPolicy.Schedule
    status: BackupPolicy.Status
    upload: bool
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., deployment_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., is_paused: bool = ..., schedule: _Optional[_Union[BackupPolicy.Schedule, _Mapping]] = ..., upload: bool = ..., retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., email_notification: _Optional[str] = ..., locked: bool = ..., status: _Optional[_Union[BackupPolicy.Status, _Mapping]] = ..., additional_region_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BackupPolicyList(_message.Message):
    __slots__ = ["budget", "items"]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    budget: _common_pb2.Budget
    items: _containers.RepeatedCompositeFieldContainer[BackupPolicy]
    def __init__(self, items: _Optional[_Iterable[_Union[BackupPolicy, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class CopyBackupRequest(_message.Message):
    __slots__ = ["region_id", "source_backup_id"]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    source_backup_id: str
    def __init__(self, source_backup_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class ListBackupPoliciesRequest(_message.Message):
    __slots__ = ["deployment_id", "include_deleted", "options"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    include_deleted: bool
    options: _common_pb2.ListOptions
    def __init__(self, deployment_id: _Optional[str] = ..., include_deleted: bool = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class ListBackupsRequest(_message.Message):
    __slots__ = ["deployment_id", "good_only", "options", "sort_by_created", "sort_descending", "to"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    GOOD_ONLY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_CREATED_FIELD_NUMBER: _ClassVar[int]
    SORT_DESCENDING_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    good_only: bool
    options: _common_pb2.ListOptions
    sort_by_created: bool
    sort_descending: bool
    to: _timestamp_pb2.Timestamp
    def __init__(self, deployment_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., good_only: bool = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., sort_by_created: bool = ..., sort_descending: bool = ..., **kwargs) -> None: ...

class TimeOfDay(_message.Message):
    __slots__ = ["hours", "minutes", "time_zone"]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    hours: int
    minutes: int
    time_zone: str
    def __init__(self, hours: _Optional[int] = ..., minutes: _Optional[int] = ..., time_zone: _Optional[str] = ...) -> None: ...
