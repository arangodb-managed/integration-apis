from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCreditBundlesRequest(_message.Message):
    __slots__ = ["organization_id", "exclude_expired"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    exclude_expired: bool
    def __init__(self, organization_id: _Optional[str] = ..., exclude_expired: bool = ...) -> None: ...

class CreditBundlesList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CreditBundle]
    def __init__(self, items: _Optional[_Iterable[_Union[CreditBundle, _Mapping]]] = ...) -> None: ...

class CreditBundle(_message.Message):
    __slots__ = ["id", "url", "organization_id", "credits_purchased", "total_price", "currency", "credits_remaining", "purchased_at", "valid_from", "valid_until"]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREDITS_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CREDITS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    organization_id: str
    credits_purchased: float
    total_price: float
    currency: str
    credits_remaining: float
    purchased_at: _timestamp_pb2.Timestamp
    valid_from: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., credits_purchased: _Optional[float] = ..., total_price: _Optional[float] = ..., currency: _Optional[str] = ..., credits_remaining: _Optional[float] = ..., purchased_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
