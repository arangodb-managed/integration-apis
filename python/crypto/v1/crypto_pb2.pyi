from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.duration import duration_pb2 as _duration_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CACertificate(_message.Message):
    __slots__ = ["id", "url", "name", "description", "project_id", "lifetime", "created_at", "deleted_at", "expires_at", "certificate_pem", "is_deleted", "is_expired", "will_expire_soon", "is_default", "use_well_known_certificate", "locked", "rotation_needed", "cloned_from_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_PEM_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    WILL_EXPIRE_SOON_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    USE_WELL_KNOWN_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    ROTATION_NEEDED_FIELD_NUMBER: _ClassVar[int]
    CLONED_FROM_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    description: str
    project_id: str
    lifetime: _duration_pb2.Duration
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    certificate_pem: str
    is_deleted: bool
    is_expired: bool
    will_expire_soon: bool
    is_default: bool
    use_well_known_certificate: bool
    locked: bool
    rotation_needed: bool
    cloned_from_id: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., project_id: _Optional[str] = ..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., certificate_pem: _Optional[str] = ..., is_deleted: bool = ..., is_expired: bool = ..., will_expire_soon: bool = ..., is_default: bool = ..., use_well_known_certificate: bool = ..., locked: bool = ..., rotation_needed: bool = ..., cloned_from_id: _Optional[str] = ...) -> None: ...

class CACertificateList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CACertificate]
    def __init__(self, items: _Optional[_Iterable[_Union[CACertificate, _Mapping]]] = ...) -> None: ...

class ListCACertificatesRequest(_message.Message):
    __slots__ = ["options", "project_id", "cloned_from_id"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLONED_FROM_ID_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    project_id: str
    cloned_from_id: str
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., project_id: _Optional[str] = ..., cloned_from_id: _Optional[str] = ...) -> None: ...

class CACertificateInstructions(_message.Message):
    __slots__ = ["platforms"]
    class PlatformInstructions(_message.Message):
        __slots__ = ["platform", "install_steps", "uninstall_steps"]
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        INSTALL_STEPS_FIELD_NUMBER: _ClassVar[int]
        UNINSTALL_STEPS_FIELD_NUMBER: _ClassVar[int]
        platform: str
        install_steps: _containers.RepeatedScalarFieldContainer[str]
        uninstall_steps: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, platform: _Optional[str] = ..., install_steps: _Optional[_Iterable[str]] = ..., uninstall_steps: _Optional[_Iterable[str]] = ...) -> None: ...
    PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    platforms: _containers.RepeatedCompositeFieldContainer[CACertificateInstructions.PlatformInstructions]
    def __init__(self, platforms: _Optional[_Iterable[_Union[CACertificateInstructions.PlatformInstructions, _Mapping]]] = ...) -> None: ...
