from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from github.com.golang.protobuf.ptypes.duration import duration_pb2 as _duration_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditLog(_message.Message):
    __slots__ = ["id", "url", "name", "description", "created_at", "deleted_at", "is_deleted", "created_by_id", "organization_id", "is_default", "destinations"]
    class HttpsPostSettings(_message.Message):
        __slots__ = ["url", "trusted_server_ca_pem", "client_certificate_pem", "client_key_pem", "headers", "retry_period"]
        URL_FIELD_NUMBER: _ClassVar[int]
        TRUSTED_SERVER_CA_PEM_FIELD_NUMBER: _ClassVar[int]
        CLIENT_CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
        CLIENT_KEY_PEM_FIELD_NUMBER: _ClassVar[int]
        HEADERS_FIELD_NUMBER: _ClassVar[int]
        RETRY_PERIOD_FIELD_NUMBER: _ClassVar[int]
        url: str
        trusted_server_ca_pem: str
        client_certificate_pem: str
        client_key_pem: str
        headers: _containers.RepeatedCompositeFieldContainer[AuditLog.Header]
        retry_period: _duration_pb2.Duration
        def __init__(self, url: _Optional[str] = ..., trusted_server_ca_pem: _Optional[str] = ..., client_certificate_pem: _Optional[str] = ..., client_key_pem: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[AuditLog.Header, _Mapping]]] = ..., retry_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DestinationStatus(_message.Message):
        __slots__ = ["deployment_id", "has_errors", "error_details", "counters_since_midnight", "counters_yesterday", "updated_at", "deployment_name"]
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
        ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        COUNTERS_SINCE_MIDNIGHT_FIELD_NUMBER: _ClassVar[int]
        COUNTERS_YESTERDAY_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_NAME_FIELD_NUMBER: _ClassVar[int]
        deployment_id: str
        has_errors: bool
        error_details: str
        counters_since_midnight: AuditLog.DestinationCounters
        counters_yesterday: AuditLog.DestinationCounters
        updated_at: _timestamp_pb2.Timestamp
        deployment_name: str
        def __init__(self, deployment_id: _Optional[str] = ..., has_errors: bool = ..., error_details: _Optional[str] = ..., counters_since_midnight: _Optional[_Union[AuditLog.DestinationCounters, _Mapping]] = ..., counters_yesterday: _Optional[_Union[AuditLog.DestinationCounters, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployment_name: _Optional[str] = ...) -> None: ...
    class DestinationCounters(_message.Message):
        __slots__ = ["events", "events_excluded", "events_undeliverable", "bytes_succeeded", "bytes_failed", "https_posts_succeeded", "https_posts_failed"]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        EVENTS_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
        EVENTS_UNDELIVERABLE_FIELD_NUMBER: _ClassVar[int]
        BYTES_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
        BYTES_FAILED_FIELD_NUMBER: _ClassVar[int]
        HTTPS_POSTS_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
        HTTPS_POSTS_FAILED_FIELD_NUMBER: _ClassVar[int]
        events: int
        events_excluded: int
        events_undeliverable: int
        bytes_succeeded: int
        bytes_failed: int
        https_posts_succeeded: int
        https_posts_failed: int
        def __init__(self, events: _Optional[int] = ..., events_excluded: _Optional[int] = ..., events_undeliverable: _Optional[int] = ..., bytes_succeeded: _Optional[int] = ..., bytes_failed: _Optional[int] = ..., https_posts_succeeded: _Optional[int] = ..., https_posts_failed: _Optional[int] = ...) -> None: ...
    class Destination(_message.Message):
        __slots__ = ["type", "excluded_topics", "http_post", "Statuses", "id"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_TOPICS_FIELD_NUMBER: _ClassVar[int]
        HTTP_POST_FIELD_NUMBER: _ClassVar[int]
        STATUSES_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        type: str
        excluded_topics: _containers.RepeatedScalarFieldContainer[str]
        http_post: AuditLog.HttpsPostSettings
        Statuses: _containers.RepeatedCompositeFieldContainer[AuditLog.DestinationStatus]
        id: str
        def __init__(self, type: _Optional[str] = ..., excluded_topics: _Optional[_Iterable[str]] = ..., http_post: _Optional[_Union[AuditLog.HttpsPostSettings, _Mapping]] = ..., Statuses: _Optional[_Iterable[_Union[AuditLog.DestinationStatus, _Mapping]]] = ..., id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    created_by_id: str
    organization_id: str
    is_default: bool
    destinations: _containers.RepeatedCompositeFieldContainer[AuditLog.Destination]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., created_by_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., is_default: bool = ..., destinations: _Optional[_Iterable[_Union[AuditLog.Destination, _Mapping]]] = ...) -> None: ...

class AuditLogList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AuditLog]
    def __init__(self, items: _Optional[_Iterable[_Union[AuditLog, _Mapping]]] = ...) -> None: ...

class ListAuditLogsRequest(_message.Message):
    __slots__ = ["organization_id", "include_deleted", "options"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    include_deleted: bool
    options: _common_pb2.ListOptions
    def __init__(self, organization_id: _Optional[str] = ..., include_deleted: bool = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class AuditLogArchive(_message.Message):
    __slots__ = ["id", "url", "created_at", "deleted_at", "is_deleted", "auditlog_id", "deployment_id", "size_in_bytes", "size_in_bytes_changed_at", "project_id", "deployment_name", "project_name", "can_delete"]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_CHANGED_AT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_DELETE_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    auditlog_id: str
    deployment_id: str
    size_in_bytes: int
    size_in_bytes_changed_at: _timestamp_pb2.Timestamp
    project_id: str
    deployment_name: str
    project_name: str
    can_delete: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., auditlog_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., size_in_bytes: _Optional[int] = ..., size_in_bytes_changed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., project_id: _Optional[str] = ..., deployment_name: _Optional[str] = ..., project_name: _Optional[str] = ..., can_delete: bool = ...) -> None: ...

class AuditLogArchiveList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AuditLogArchive]
    def __init__(self, items: _Optional[_Iterable[_Union[AuditLogArchive, _Mapping]]] = ...) -> None: ...

class ListAuditLogArchivesRequest(_message.Message):
    __slots__ = ["auditlog_id", "include_deleted", "deployment_id", "without_deployments", "project_id", "options"]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    WITHOUT_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    auditlog_id: str
    include_deleted: bool
    deployment_id: str
    without_deployments: bool
    project_id: str
    options: _common_pb2.ListOptions
    def __init__(self, auditlog_id: _Optional[str] = ..., include_deleted: bool = ..., deployment_id: _Optional[str] = ..., without_deployments: bool = ..., project_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class AuditLogEvent(_message.Message):
    __slots__ = ["timestamp", "topic", "project_id", "deployment_id", "server_id", "instance_id", "sequence", "user_id", "database", "client_ip", "authentication", "message", "auditlogarchive_id", "verb"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AUDITLOGARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    topic: str
    project_id: str
    deployment_id: str
    server_id: str
    instance_id: str
    sequence: int
    user_id: str
    database: str
    client_ip: str
    authentication: str
    message: str
    auditlogarchive_id: str
    verb: str
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., topic: _Optional[str] = ..., project_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., server_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., sequence: _Optional[int] = ..., user_id: _Optional[str] = ..., database: _Optional[str] = ..., client_ip: _Optional[str] = ..., authentication: _Optional[str] = ..., message: _Optional[str] = ..., auditlogarchive_id: _Optional[str] = ..., verb: _Optional[str] = ...) -> None: ...

class AuditLogEventList(_message.Message):
    __slots__ = ["items", "cursor"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AuditLogEvent]
    cursor: str
    def __init__(self, items: _Optional[_Iterable[_Union[AuditLogEvent, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...

class GetAuditLogEventsRequest(_message.Message):
    __slots__ = ["auditlog_id", "auditlogarchive_id", "to", "included_topics", "excluded_topics", "limit", "cursor"]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    AUDITLOGARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_TOPICS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_TOPICS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    auditlog_id: str
    auditlogarchive_id: str
    to: _timestamp_pb2.Timestamp
    included_topics: _containers.RepeatedScalarFieldContainer[str]
    excluded_topics: _containers.RepeatedScalarFieldContainer[str]
    limit: int
    cursor: str
    def __init__(self, auditlog_id: _Optional[str] = ..., auditlogarchive_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., included_topics: _Optional[_Iterable[str]] = ..., excluded_topics: _Optional[_Iterable[str]] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ..., **kwargs) -> None: ...

class DeleteAuditLogArchiveEventsRequest(_message.Message):
    __slots__ = ["auditlogarchive_id", "to"]
    AUDITLOGARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    auditlogarchive_id: str
    to: _timestamp_pb2.Timestamp
    def __init__(self, auditlogarchive_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AttachProjectToAuditLogRequest(_message.Message):
    __slots__ = ["project_id", "auditlog_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    auditlog_id: str
    def __init__(self, project_id: _Optional[str] = ..., auditlog_id: _Optional[str] = ...) -> None: ...

class TestAuditLogHttpsPostDestinationRequest(_message.Message):
    __slots__ = ["organization_id", "settings", "auditlog_id", "destination_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    settings: AuditLog.HttpsPostSettings
    auditlog_id: str
    destination_id: str
    def __init__(self, organization_id: _Optional[str] = ..., settings: _Optional[_Union[AuditLog.HttpsPostSettings, _Mapping]] = ..., auditlog_id: _Optional[str] = ..., destination_id: _Optional[str] = ...) -> None: ...

class TestAuditLogHttpsPostDestinationResult(_message.Message):
    __slots__ = ["has_errors", "error_details"]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    error_details: str
    def __init__(self, has_errors: bool = ..., error_details: _Optional[str] = ...) -> None: ...

class AuditLogTopic(_message.Message):
    __slots__ = ["topic", "for_deployment", "for_platform", "exclude_by_default"]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    FOR_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    FOR_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    topic: str
    for_deployment: bool
    for_platform: bool
    exclude_by_default: bool
    def __init__(self, topic: _Optional[str] = ..., for_deployment: bool = ..., for_platform: bool = ..., exclude_by_default: bool = ...) -> None: ...

class AuditLogTopicList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AuditLogTopic]
    def __init__(self, items: _Optional[_Iterable[_Union[AuditLogTopic, _Mapping]]] = ...) -> None: ...

class ListAuditLogTopicsRequest(_message.Message):
    __slots__ = ["options", "for_deployment_only", "for_platform_only"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    FOR_DEPLOYMENT_ONLY_FIELD_NUMBER: _ClassVar[int]
    FOR_PLATFORM_ONLY_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    for_deployment_only: bool
    for_platform_only: bool
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., for_deployment_only: bool = ..., for_platform_only: bool = ...) -> None: ...

class SetDefaultAuditLogRequest(_message.Message):
    __slots__ = ["organization_id", "auditlog_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    auditlog_id: str
    def __init__(self, organization_id: _Optional[str] = ..., auditlog_id: _Optional[str] = ...) -> None: ...
