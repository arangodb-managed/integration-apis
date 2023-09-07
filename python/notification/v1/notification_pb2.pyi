from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Notification(_message.Message):
    __slots__ = ["id", "type", "created_at", "title", "recipients", "content", "read_at", "is_read"]
    class ReadAt(_message.Message):
        __slots__ = ["read_at", "read_by_id"]
        READ_AT_FIELD_NUMBER: _ClassVar[int]
        READ_BY_ID_FIELD_NUMBER: _ClassVar[int]
        read_at: _timestamp_pb2.Timestamp
        read_by_id: str
        def __init__(self, read_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., read_by_id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    created_at: _timestamp_pb2.Timestamp
    title: str
    recipients: _containers.RepeatedScalarFieldContainer[str]
    content: _containers.RepeatedCompositeFieldContainer[NotificationContent]
    read_at: Notification.ReadAt
    is_read: bool
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., title: _Optional[str] = ..., recipients: _Optional[_Iterable[str]] = ..., content: _Optional[_Iterable[_Union[NotificationContent, _Mapping]]] = ..., read_at: _Optional[_Union[Notification.ReadAt, _Mapping]] = ..., is_read: bool = ...) -> None: ...

class NotificationContent(_message.Message):
    __slots__ = ["content_type", "content"]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content_type: str
    content: str
    def __init__(self, content_type: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class ListDeploymentNotificationsRequest(_message.Message):
    __slots__ = ["deployment_id", "options", "read_only", "unread_only"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    UNREAD_ONLY_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    options: _common_pb2.ListOptions
    read_only: bool
    unread_only: bool
    def __init__(self, deployment_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., read_only: bool = ..., unread_only: bool = ...) -> None: ...

class NotificationList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Notification]
    def __init__(self, items: _Optional[_Iterable[_Union[Notification, _Mapping]]] = ...) -> None: ...

class MarkNotificationRequest(_message.Message):
    __slots__ = ["notification_id"]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    def __init__(self, notification_id: _Optional[str] = ...) -> None: ...
