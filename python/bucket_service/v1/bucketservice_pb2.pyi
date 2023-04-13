from common.v1 import common_pb2 as _common_pb2
from common.v1 import icommon_pb2 as _icommon_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BucketRequest(_message.Message):
    __slots__ = ["tags"]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[_icommon_pb2.KeyValuePair]
    def __init__(self, tags: _Optional[_Iterable[_Union[_icommon_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class ObjectInfo(_message.Message):
    __slots__ = ["is_locked", "last_updated_at", "size_in_bytes"]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    is_locked: bool
    last_updated_at: _timestamp_pb2.Timestamp
    size_in_bytes: int
    def __init__(self, is_locked: bool = ..., size_in_bytes: _Optional[int] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PathRequest(_message.Message):
    __slots__ = ["path"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class PathSize(_message.Message):
    __slots__ = ["number_of_files", "number_of_folders", "size_in_bytes"]
    NUMBER_OF_FILES_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    number_of_files: int
    number_of_folders: int
    size_in_bytes: int
    def __init__(self, size_in_bytes: _Optional[int] = ..., number_of_files: _Optional[int] = ..., number_of_folders: _Optional[int] = ...) -> None: ...

class ReadObjectChunk(_message.Message):
    __slots__ = ["chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class RepositoryURL(_message.Message):
    __slots__ = ["bucket_path", "url"]
    BUCKET_PATH_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    bucket_path: str
    url: str
    def __init__(self, url: _Optional[str] = ..., bucket_path: _Optional[str] = ...) -> None: ...

class WriteObjectChunk(_message.Message):
    __slots__ = ["chunk", "has_more", "path"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    has_more: bool
    path: PathRequest
    def __init__(self, path: _Optional[_Union[PathRequest, _Mapping]] = ..., chunk: _Optional[bytes] = ..., has_more: bool = ...) -> None: ...

class WriteObjectControl(_message.Message):
    __slots__ = ["allow_more_output", "max_chunk_bytes"]
    ALLOW_MORE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    MAX_CHUNK_BYTES_FIELD_NUMBER: _ClassVar[int]
    allow_more_output: bool
    max_chunk_bytes: int
    def __init__(self, allow_more_output: bool = ..., max_chunk_bytes: _Optional[int] = ...) -> None: ...
