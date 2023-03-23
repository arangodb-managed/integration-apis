from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from github.com.golang.protobuf.ptypes.duration import duration_pb2 as _duration_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttachProjectToAuditLogRequest(_message.Message):
    __slots__ = ["auditlog_id", "project_id"]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    auditlog_id: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., auditlog_id: _Optional[str] = ...) -> None: ...

class AuditLog(_message.Message):
    __slots__ = ["created_at", "created_by_id", "deleted_at", "description", "destinations", "id", "is_default", "is_deleted", "name", "organization_id", "url"]
    class Destination(_message.Message):
        __slots__ = ["Statuses", "excluded_topics", "http_post", "id", "type"]
        EXCLUDED_TOPICS_FIELD_NUMBER: _ClassVar[int]
        HTTP_POST_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUSES_FIELD_NUMBER: _ClassVar[int]
        Statuses: _containers.RepeatedCompositeFieldContainer[AuditLog.DestinationStatus]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        excluded_topics: _containers.RepeatedScalarFieldContainer[str]
        http_post: AuditLog.HttpsPostSettings
        id: str
        type: str
        def __init__(self, type: _Optional[str] = ..., excluded_topics: _Optional[_Iterable[str]] = ..., http_post: _Optional[_Union[AuditLog.HttpsPostSettings, _Mapping]] = ..., Statuses: _Optional[_Iterable[_Union[AuditLog.DestinationStatus, _Mapping]]] = ..., id: _Optional[str] = ...) -> None: ...
    class DestinationCounters(_message.Message):
        __slots__ = ["bytes_failed", "bytes_succeeded", "events", "events_excluded", "events_undeliverable", "https_posts_failed", "https_posts_succeeded"]
        BYTES_FAILED_FIELD_NUMBER: _ClassVar[int]
        BYTES_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
        EVENTS_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        EVENTS_UNDELIVERABLE_FIELD_NUMBER: _ClassVar[int]
        HTTPS_POSTS_FAILED_FIELD_NUMBER: _ClassVar[int]
        HTTPS_POSTS_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
        bytes_failed: int
        bytes_succeeded: int
        events: int
        events_excluded: int
        events_undeliverable: int
        https_posts_failed: int
        https_posts_succeeded: int
        def __init__(self, events: _Optional[int] = ..., events_excluded: _Optional[int] = ..., events_undeliverable: _Optional[int] = ..., bytes_succeeded: _Optional[int] = ..., bytes_failed: _Optional[int] = ..., https_posts_succeeded: _Optional[int] = ..., https_posts_failed: _Optional[int] = ...) -> None: ...
    class DestinationStatus(_message.Message):
        __slots__ = ["counters_since_midnight", "counters_yesterday", "deployment_id", "deployment_name", "error_details", "has_errors", "updated_at"]
        COUNTERS_SINCE_MIDNIGHT_FIELD_NUMBER: _ClassVar[int]
        COUNTERS_YESTERDAY_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        counters_since_midnight: AuditLog.DestinationCounters
        counters_yesterday: AuditLog.DestinationCounters
        deployment_id: str
        deployment_name: str
        error_details: str
        has_errors: bool
        updated_at: _timestamp_pb2.Timestamp
        def __init__(self, deployment_id: _Optional[str] = ..., has_errors: bool = ..., error_details: _Optional[str] = ..., counters_since_midnight: _Optional[_Union[AuditLog.DestinationCounters, _Mapping]] = ..., counters_yesterday: _Optional[_Union[AuditLog.DestinationCounters, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deployment_name: _Optional[str] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class HttpsPostSettings(_message.Message):
        __slots__ = ["client_certificate_pem", "client_key_pem", "headers", "retry_period", "trusted_server_ca_pem", "url"]
        CLIENT_CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
        CLIENT_KEY_PEM_FIELD_NUMBER: _ClassVar[int]
        HEADERS_FIELD_NUMBER: _ClassVar[int]
        RETRY_PERIOD_FIELD_NUMBER: _ClassVar[int]
        TRUSTED_SERVER_CA_PEM_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        client_certificate_pem: str
        client_key_pem: str
        headers: _containers.RepeatedCompositeFieldContainer[AuditLog.Header]
        retry_period: _duration_pb2.Duration
        trusted_server_ca_pem: str
        url: str
        def __init__(self, url: _Optional[str] = ..., trusted_server_ca_pem: _Optional[str] = ..., client_certificate_pem: _Optional[str] = ..., client_key_pem: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[AuditLog.Header, _Mapping]]] = ..., retry_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    created_by_id: str
    deleted_at: _timestamp_pb2.Timestamp
    description: str
    destinations: _containers.RepeatedCompositeFieldContainer[AuditLog.Destination]
    id: str
    is_default: bool
    is_deleted: bool
    name: str
    organization_id: str
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., created_by_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., is_default: bool = ..., destinations: _Optional[_Iterable[_Union[AuditLog.Destination, _Mapping]]] = ...) -> None: ...

class AuditLogArchive(_message.Message):
    __slots__ = ["auditlog_id", "can_delete", "created_at", "deleted_at", "deployment_id", "deployment_name", "id", "is_deleted", "project_id", "project_name", "size_in_bytes", "size_in_bytes_changed_at", "url"]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    CAN_DELETE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_CHANGED_AT_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    auditlog_id: str
    can_delete: bool
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    deployment_id: str
    deployment_name: str
    id: str
    is_deleted: bool
    project_id: str
    project_name: str
    size_in_bytes: int
    size_in_bytes_changed_at: _timestamp_pb2.Timestamp
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., auditlog_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., size_in_bytes: _Optional[int] = ..., size_in_bytes_changed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., project_id: _Optional[str] = ..., deployment_name: _Optional[str] = ..., project_name: _Optional[str] = ..., can_delete: bool = ...) -> None: ...

class AuditLogArchiveList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AuditLogArchive]
    def __init__(self, items: _Optional[_Iterable[_Union[AuditLogArchive, _Mapping]]] = ...) -> None: ...

class AuditLogEvent(_message.Message):
    __slots__ = ["auditlogarchive_id", "authentication", "client_ip", "database", "deployment_id", "instance_id", "message", "project_id", "sequence", "server_id", "timestamp", "topic", "user_id", "verb"]
    AUDITLOGARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    auditlogarchive_id: str
    authentication: str
    client_ip: str
    database: str
    deployment_id: str
    instance_id: str
    message: str
    project_id: str
    sequence: int
    server_id: str
    timestamp: _timestamp_pb2.Timestamp
    topic: str
    user_id: str
    verb: str
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., topic: _Optional[str] = ..., project_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., server_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., sequence: _Optional[int] = ..., user_id: _Optional[str] = ..., database: _Optional[str] = ..., client_ip: _Optional[str] = ..., authentication: _Optional[str] = ..., message: _Optional[str] = ..., auditlogarchive_id: _Optional[str] = ..., verb: _Optional[str] = ...) -> None: ...

class AuditLogEventList(_message.Message):
    __slots__ = ["cursor", "items"]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    cursor: str
    items: _containers.RepeatedCompositeFieldContainer[AuditLogEvent]
    def __init__(self, items: _Optional[_Iterable[_Union[AuditLogEvent, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...

class AuditLogList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AuditLog]
    def __init__(self, items: _Optional[_Iterable[_Union[AuditLog, _Mapping]]] = ...) -> None: ...

class AuditLogTopic(_message.Message):
    __slots__ = ["exclude_by_default", "for_deployment", "for_platform", "topic"]
    EXCLUDE_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    FOR_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    FOR_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    exclude_by_default: bool
    for_deployment: bool
    for_platform: bool
    topic: str
    def __init__(self, topic: _Optional[str] = ..., for_deployment: bool = ..., for_platform: bool = ..., exclude_by_default: bool = ...) -> None: ...

class AuditLogTopicList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AuditLogTopic]
    def __init__(self, items: _Optional[_Iterable[_Union[AuditLogTopic, _Mapping]]] = ...) -> None: ...

class DeleteAuditLogArchiveEventsRequest(_message.Message):
    __slots__ = ["auditlogarchive_id", "to"]
    AUDITLOGARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    auditlogarchive_id: str
    to: _timestamp_pb2.Timestamp
    def __init__(self, auditlogarchive_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAuditLogEventsRequest(_message.Message):
    __slots__ = ["auditlog_id", "auditlogarchive_id", "cursor", "excluded_topics", "included_topics", "limit", "to"]
    AUDITLOGARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_TOPICS_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_TOPICS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    auditlog_id: str
    auditlogarchive_id: str
    cursor: str
    excluded_topics: _containers.RepeatedScalarFieldContainer[str]
    included_topics: _containers.RepeatedScalarFieldContainer[str]
    limit: int
    to: _timestamp_pb2.Timestamp
    def __init__(self, auditlog_id: _Optional[str] = ..., auditlogarchive_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., included_topics: _Optional[_Iterable[str]] = ..., excluded_topics: _Optional[_Iterable[str]] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ..., **kwargs) -> None: ...

class ListAuditLogArchivesRequest(_message.Message):
    __slots__ = ["auditlog_id", "deployment_id", "include_deleted", "options", "project_id", "without_deployments"]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    WITHOUT_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    auditlog_id: str
    deployment_id: str
    include_deleted: bool
    options: _common_pb2.ListOptions
    project_id: str
    without_deployments: bool
    def __init__(self, auditlog_id: _Optional[str] = ..., include_deleted: bool = ..., deployment_id: _Optional[str] = ..., without_deployments: bool = ..., project_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class ListAuditLogTopicsRequest(_message.Message):
    __slots__ = ["for_deployment_only", "for_platform_only", "options"]
    FOR_DEPLOYMENT_ONLY_FIELD_NUMBER: _ClassVar[int]
    FOR_PLATFORM_ONLY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    for_deployment_only: bool
    for_platform_only: bool
    options: _common_pb2.ListOptions
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., for_deployment_only: bool = ..., for_platform_only: bool = ...) -> None: ...

class ListAuditLogsRequest(_message.Message):
    __slots__ = ["include_deleted", "options", "organization_id"]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    include_deleted: bool
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ..., include_deleted: bool = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class SetDefaultAuditLogRequest(_message.Message):
    __slots__ = ["auditlog_id", "organization_id"]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    auditlog_id: str
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ..., auditlog_id: _Optional[str] = ...) -> None: ...

class TestAuditLogHttpsPostDestinationRequest(_message.Message):
    __slots__ = ["auditlog_id", "destination_id", "organization_id", "settings"]
    AUDITLOG_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    auditlog_id: str
    destination_id: str
    organization_id: str
    settings: AuditLog.HttpsPostSettings
    def __init__(self, organization_id: _Optional[str] = ..., settings: _Optional[_Union[AuditLog.HttpsPostSettings, _Mapping]] = ..., auditlog_id: _Optional[str] = ..., destination_id: _Optional[str] = ...) -> None: ...

class TestAuditLogHttpsPostDestinationResult(_message.Message):
    __slots__ = ["error_details", "has_errors"]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    error_details: str
    has_errors: bool
    def __init__(self, has_errors: bool = ..., error_details: _Optional[str] = ...) -> None: ...
