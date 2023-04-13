from common.v1 import common_pb2 as _common_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaqGroup(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FaqGroupEntry(_message.Message):
    __slots__ = ["answer", "question"]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    answer: str
    question: str
    def __init__(self, question: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...

class FaqGroupEntryList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FaqGroupEntry]
    def __init__(self, items: _Optional[_Iterable[_Union[FaqGroupEntry, _Mapping]]] = ...) -> None: ...

class FaqGroupList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[FaqGroup]
    def __init__(self, items: _Optional[_Iterable[_Union[FaqGroup, _Mapping]]] = ...) -> None: ...

class ListPlansRequest(_message.Message):
    __slots__ = ["model", "options", "organization_id"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    model: str
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., organization_id: _Optional[str] = ..., model: _Optional[str] = ...) -> None: ...

class Plan(_message.Message):
    __slots__ = ["description", "first_response_times", "id", "is_default", "is_unavailable", "name", "support_hours"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIRST_RESPONSE_TIMES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    IS_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_HOURS_FIELD_NUMBER: _ClassVar[int]
    description: str
    first_response_times: ResponseTimes
    id: str
    is_default: bool
    is_unavailable: bool
    name: str
    support_hours: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., is_default: bool = ..., description: _Optional[str] = ..., is_unavailable: bool = ..., first_response_times: _Optional[_Union[ResponseTimes, _Mapping]] = ..., support_hours: _Optional[str] = ...) -> None: ...

class PlanList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Plan]
    def __init__(self, items: _Optional[_Iterable[_Union[Plan, _Mapping]]] = ...) -> None: ...

class ResponseTimes(_message.Message):
    __slots__ = ["critical", "high", "low", "normal"]
    CRITICAL_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    critical: int
    high: int
    low: int
    normal: int
    def __init__(self, critical: _Optional[int] = ..., high: _Optional[int] = ..., normal: _Optional[int] = ..., low: _Optional[int] = ...) -> None: ...

class SupportRequest(_message.Message):
    __slots__ = ["deployment_id", "description", "email_address", "id", "organization_id", "project_id", "severity", "title", "user_id", "user_name"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    description: str
    email_address: str
    id: str
    organization_id: str
    project_id: str
    severity: str
    title: str
    user_id: str
    user_name: str
    def __init__(self, id: _Optional[str] = ..., user_name: _Optional[str] = ..., user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., organization_id: _Optional[str] = ..., project_id: _Optional[str] = ..., deployment_id: _Optional[str] = ..., description: _Optional[str] = ..., severity: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
