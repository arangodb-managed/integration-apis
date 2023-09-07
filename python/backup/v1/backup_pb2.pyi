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

class BackupPolicy(_message.Message):
    __slots__ = ["id", "url", "name", "description", "deployment_id", "created_at", "deleted_at", "is_deleted", "is_paused", "schedule", "upload", "retention_period", "email_notification", "locked", "status", "additional_region_ids"]
    class Schedule(_message.Message):
        __slots__ = ["schedule_type", "hourly_schedule", "daily_schedule", "monthly_schedule"]
        SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
        HOURLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        DAILY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        schedule_type: str
        hourly_schedule: BackupPolicy.HourlySchedule
        daily_schedule: BackupPolicy.DailySchedule
        monthly_schedule: BackupPolicy.MonthlySchedule
        def __init__(self, schedule_type: _Optional[str] = ..., hourly_schedule: _Optional[_Union[BackupPolicy.HourlySchedule, _Mapping]] = ..., daily_schedule: _Optional[_Union[BackupPolicy.DailySchedule, _Mapping]] = ..., monthly_schedule: _Optional[_Union[BackupPolicy.MonthlySchedule, _Mapping]] = ...) -> None: ...
    class HourlySchedule(_message.Message):
        __slots__ = ["schedule_every_interval_hours", "minutes_offset"]
        SCHEDULE_EVERY_INTERVAL_HOURS_FIELD_NUMBER: _ClassVar[int]
        MINUTES_OFFSET_FIELD_NUMBER: _ClassVar[int]
        schedule_every_interval_hours: int
        minutes_offset: int
        def __init__(self, schedule_every_interval_hours: _Optional[int] = ..., minutes_offset: _Optional[int] = ...) -> None: ...
    class DailySchedule(_message.Message):
        __slots__ = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "schedule_at"]
        MONDAY_FIELD_NUMBER: _ClassVar[int]
        TUESDAY_FIELD_NUMBER: _ClassVar[int]
        WEDNESDAY_FIELD_NUMBER: _ClassVar[int]
        THURSDAY_FIELD_NUMBER: _ClassVar[int]
        FRIDAY_FIELD_NUMBER: _ClassVar[int]
        SATURDAY_FIELD_NUMBER: _ClassVar[int]
        SUNDAY_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_AT_FIELD_NUMBER: _ClassVar[int]
        monday: bool
        tuesday: bool
        wednesday: bool
        thursday: bool
        friday: bool
        saturday: bool
        sunday: bool
        schedule_at: TimeOfDay
        def __init__(self, monday: bool = ..., tuesday: bool = ..., wednesday: bool = ..., thursday: bool = ..., friday: bool = ..., saturday: bool = ..., sunday: bool = ..., schedule_at: _Optional[_Union[TimeOfDay, _Mapping]] = ...) -> None: ...
    class MonthlySchedule(_message.Message):
        __slots__ = ["day_of_month", "schedule_at"]
        DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_AT_FIELD_NUMBER: _ClassVar[int]
        day_of_month: int
        schedule_at: TimeOfDay
        def __init__(self, day_of_month: _Optional[int] = ..., schedule_at: _Optional[_Union[TimeOfDay, _Mapping]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["next_backup", "message"]
        NEXT_BACKUP_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        next_backup: _timestamp_pb2.Timestamp
        message: str
        def __init__(self, next_backup: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_REGION_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    deployment_id: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    is_paused: bool
    schedule: BackupPolicy.Schedule
    upload: bool
    retention_period: _duration_pb2.Duration
    email_notification: str
    locked: bool
    status: BackupPolicy.Status
    additional_region_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., deployment_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., is_paused: bool = ..., schedule: _Optional[_Union[BackupPolicy.Schedule, _Mapping]] = ..., upload: bool = ..., retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., email_notification: _Optional[str] = ..., locked: bool = ..., status: _Optional[_Union[BackupPolicy.Status, _Mapping]] = ..., additional_region_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TimeOfDay(_message.Message):
    __slots__ = ["hours", "minutes", "time_zone"]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    hours: int
    minutes: int
    time_zone: str
    def __init__(self, hours: _Optional[int] = ..., minutes: _Optional[int] = ..., time_zone: _Optional[str] = ...) -> None: ...

class BackupPolicyList(_message.Message):
    __slots__ = ["items", "budget"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[BackupPolicy]
    budget: _common_pb2.Budget
    def __init__(self, items: _Optional[_Iterable[_Union[BackupPolicy, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class ListBackupPoliciesRequest(_message.Message):
    __slots__ = ["deployment_id", "include_deleted", "options"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    include_deleted: bool
    options: _common_pb2.ListOptions
    def __init__(self, deployment_id: _Optional[str] = ..., include_deleted: bool = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class Backup(_message.Message):
    __slots__ = ["id", "url", "name", "description", "deployment_id", "backup_policy_id", "created_at", "deleted_at", "is_deleted", "auto_deleted_at", "deployment_info", "upload", "upload_updated_at", "download", "created_by_id", "status", "region_id", "source_backup_id"]
    class DeploymentInfo(_message.Message):
        __slots__ = ["version", "servers", "model"]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        SERVERS_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        version: str
        servers: _data_pb2.Deployment.ServersSpec
        model: _data_pb2.Deployment.ModelSpec
        def __init__(self, version: _Optional[str] = ..., servers: _Optional[_Union[_data_pb2.Deployment.ServersSpec, _Mapping]] = ..., model: _Optional[_Union[_data_pb2.Deployment.ModelSpec, _Mapping]] = ...) -> None: ...
    class DownloadSpec(_message.Message):
        __slots__ = ["revision", "last_updated_at"]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        revision: int
        last_updated_at: _timestamp_pb2.Timestamp
        def __init__(self, revision: _Optional[int] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["created_at", "version", "state", "is_failed", "message", "progress", "size_bytes", "available", "dbservers", "upload_only", "upload_status", "download_status"]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        IS_FAILED_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DBSERVERS_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ONLY_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
        created_at: _timestamp_pb2.Timestamp
        version: str
        state: str
        is_failed: bool
        message: str
        progress: str
        size_bytes: int
        available: bool
        dbservers: int
        upload_only: bool
        upload_status: Backup.UploadStatus
        download_status: Backup.DownloadStatus
        def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[str] = ..., state: _Optional[str] = ..., is_failed: bool = ..., message: _Optional[str] = ..., progress: _Optional[str] = ..., size_bytes: _Optional[int] = ..., available: bool = ..., dbservers: _Optional[int] = ..., upload_only: bool = ..., upload_status: _Optional[_Union[Backup.UploadStatus, _Mapping]] = ..., download_status: _Optional[_Union[Backup.DownloadStatus, _Mapping]] = ...) -> None: ...
    class UploadStatus(_message.Message):
        __slots__ = ["uploaded", "uploaded_at", "size_bytes"]
        UPLOADED_FIELD_NUMBER: _ClassVar[int]
        UPLOADED_AT_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        uploaded: bool
        uploaded_at: _timestamp_pb2.Timestamp
        size_bytes: int
        def __init__(self, uploaded: bool = ..., uploaded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., size_bytes: _Optional[int] = ...) -> None: ...
    class DownloadStatus(_message.Message):
        __slots__ = ["revision", "downloaded", "downloaded_at"]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADED_AT_FIELD_NUMBER: _ClassVar[int]
        revision: int
        downloaded: bool
        downloaded_at: _timestamp_pb2.Timestamp
        def __init__(self, revision: _Optional[int] = ..., downloaded: bool = ..., downloaded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    deployment_id: str
    backup_policy_id: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    auto_deleted_at: _timestamp_pb2.Timestamp
    deployment_info: Backup.DeploymentInfo
    upload: bool
    upload_updated_at: _timestamp_pb2.Timestamp
    download: Backup.DownloadSpec
    created_by_id: str
    status: Backup.Status
    region_id: str
    source_backup_id: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., deployment_id: _Optional[str] = ..., backup_policy_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., auto_deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployment_info: _Optional[_Union[Backup.DeploymentInfo, _Mapping]] = ..., upload: bool = ..., upload_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., download: _Optional[_Union[Backup.DownloadSpec, _Mapping]] = ..., created_by_id: _Optional[str] = ..., status: _Optional[_Union[Backup.Status, _Mapping]] = ..., region_id: _Optional[str] = ..., source_backup_id: _Optional[str] = ...) -> None: ...

class BackupList(_message.Message):
    __slots__ = ["items", "budget"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Backup]
    budget: _common_pb2.Budget
    def __init__(self, items: _Optional[_Iterable[_Union[Backup, _Mapping]]] = ..., budget: _Optional[_Union[_common_pb2.Budget, _Mapping]] = ...) -> None: ...

class ListBackupsRequest(_message.Message):
    __slots__ = ["deployment_id", "to", "good_only", "options", "sort_by_created", "sort_descending"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    GOOD_ONLY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_CREATED_FIELD_NUMBER: _ClassVar[int]
    SORT_DESCENDING_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    to: _timestamp_pb2.Timestamp
    good_only: bool
    options: _common_pb2.ListOptions
    sort_by_created: bool
    sort_descending: bool
    def __init__(self, deployment_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., good_only: bool = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., sort_by_created: bool = ..., sort_descending: bool = ..., **kwargs) -> None: ...

class CopyBackupRequest(_message.Message):
    __slots__ = ["source_backup_id", "region_id"]
    SOURCE_BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    source_backup_id: str
    region_id: str
    def __init__(self, source_backup_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...
