from common.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreditDebt(_message.Message):
    __slots__ = ("organization_id", "amount", "created_at")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    amount: float
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, organization_id: _Optional[str] = ..., amount: _Optional[float] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreditBundleUsageProjection(_message.Message):
    __slots__ = ("projections",)
    class Projection(_message.Message):
        __slots__ = ("value", "timestamp")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        value: float
        timestamp: _timestamp_pb2.Timestamp
        def __init__(self, value: _Optional[float] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    PROJECTIONS_FIELD_NUMBER: _ClassVar[int]
    projections: _containers.RepeatedCompositeFieldContainer[CreditBundleUsageProjection.Projection]
    def __init__(self, projections: _Optional[_Iterable[_Union[CreditBundleUsageProjection.Projection, _Mapping]]] = ...) -> None: ...

class GetCreditBundleUsageProjectionRequest(_message.Message):
    __slots__ = ("organization_id", "projections_limit")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECTIONS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    projections_limit: int
    def __init__(self, organization_id: _Optional[str] = ..., projections_limit: _Optional[int] = ...) -> None: ...

class CreditUsageReportList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CreditUsageReport]
    def __init__(self, items: _Optional[_Iterable[_Union[CreditUsageReport, _Mapping]]] = ...) -> None: ...

class ListCreditUsageReportsRequest(_message.Message):
    __slots__ = ("organization_id", "to", "options")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    to: _timestamp_pb2.Timestamp
    options: _common_pb2.ListOptions
    def __init__(self, organization_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., **kwargs) -> None: ...

class CreditUsageReport(_message.Message):
    __slots__ = ("id", "url", "organization_id", "amount", "opening_balance", "closing_balance", "created_at", "items", "status")
    class Item(_message.Message):
        __slots__ = ("creditusage_ids", "amount", "description")
        CREDITUSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        creditusage_ids: _containers.RepeatedScalarFieldContainer[str]
        amount: float
        description: str
        def __init__(self, creditusage_ids: _Optional[_Iterable[str]] = ..., amount: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ("is_complete",)
        IS_COMPLETE_FIELD_NUMBER: _ClassVar[int]
        is_complete: bool
        def __init__(self, is_complete: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    OPENING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    CLOSING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    organization_id: str
    amount: float
    opening_balance: float
    closing_balance: float
    created_at: _timestamp_pb2.Timestamp
    items: _containers.RepeatedCompositeFieldContainer[CreditUsageReport.Item]
    status: CreditUsageReport.Status
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., amount: _Optional[float] = ..., opening_balance: _Optional[float] = ..., closing_balance: _Optional[float] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., items: _Optional[_Iterable[_Union[CreditUsageReport.Item, _Mapping]]] = ..., status: _Optional[_Union[CreditUsageReport.Status, _Mapping]] = ...) -> None: ...

class PDFDocument(_message.Message):
    __slots__ = ("contents", "filename")
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    contents: bytes
    filename: str
    def __init__(self, contents: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class ListCreditBundleUsageRequest(_message.Message):
    __slots__ = ("organization_id", "credit_bundle_id", "starts_at", "ends_at", "usage_item_id", "options")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREDIT_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    USAGE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    credit_bundle_id: str
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    usage_item_id: str
    options: _common_pb2.ListOptions
    def __init__(self, organization_id: _Optional[str] = ..., credit_bundle_id: _Optional[str] = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., usage_item_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class ListCreditBundlesRequest(_message.Message):
    __slots__ = ("organization_id", "exclude_expired")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    exclude_expired: bool
    def __init__(self, organization_id: _Optional[str] = ..., exclude_expired: bool = ...) -> None: ...

class CreditBundlesList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CreditBundle]
    def __init__(self, items: _Optional[_Iterable[_Union[CreditBundle, _Mapping]]] = ...) -> None: ...

class CreditBundle(_message.Message):
    __slots__ = ("id", "url", "organization_id", "credits_purchased", "total_price", "currency", "credits_remaining", "purchased_at", "valid_from", "valid_until", "last_used_at")
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
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
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
    last_used_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., credits_purchased: _Optional[float] = ..., total_price: _Optional[float] = ..., currency: _Optional[str] = ..., credits_remaining: _Optional[float] = ..., purchased_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreditBundleUsage(_message.Message):
    __slots__ = ("id", "usage_item_id", "credit_bundle_id", "organization_id", "usage", "remaining", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    CREDIT_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    REMAINING_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    usage_item_id: str
    credit_bundle_id: str
    organization_id: str
    usage: float
    remaining: float
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., usage_item_id: _Optional[str] = ..., credit_bundle_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., usage: _Optional[float] = ..., remaining: _Optional[float] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreditBundleUsageList(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CreditBundleUsage]
    def __init__(self, items: _Optional[_Iterable[_Union[CreditBundleUsage, _Mapping]]] = ...) -> None: ...
