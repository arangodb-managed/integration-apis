from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Invoice(_message.Message):
    __slots__ = ["id", "url", "organization_id", "organization_name", "entity_id", "entity_name", "invoice_number", "created_at", "requires_manual_verification", "last_updated_at", "email_addresses", "purchase_order_based", "invoice_builder_version", "items", "currency_id", "total_amount_excl_taxes", "total_vat", "vat_reverse_charge", "vat_percentage_used", "total_sales_tax", "sales_tax_percentage_used", "total_amount_incl_taxes", "status", "payments"]
    class Item(_message.Message):
        __slots__ = ["usageitem_ids", "amount", "description", "is_prepaid"]
        USAGEITEM_IDS_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_PREPAID_FIELD_NUMBER: _ClassVar[int]
        usageitem_ids: _containers.RepeatedScalarFieldContainer[str]
        amount: float
        description: str
        is_prepaid: bool
        def __init__(self, usageitem_ids: _Optional[_Iterable[str]] = ..., amount: _Optional[float] = ..., description: _Optional[str] = ..., is_prepaid: bool = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["is_pending", "is_completed", "is_rejected", "is_verified", "needs_rebuild", "completed_at", "rejected_at", "completion_reason", "rejection_reason", "completed_by", "rejected_by"]
        IS_PENDING_FIELD_NUMBER: _ClassVar[int]
        IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        IS_REJECTED_FIELD_NUMBER: _ClassVar[int]
        IS_VERIFIED_FIELD_NUMBER: _ClassVar[int]
        NEEDS_REBUILD_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
        REJECTED_AT_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_REASON_FIELD_NUMBER: _ClassVar[int]
        REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_BY_FIELD_NUMBER: _ClassVar[int]
        REJECTED_BY_FIELD_NUMBER: _ClassVar[int]
        is_pending: bool
        is_completed: bool
        is_rejected: bool
        is_verified: bool
        needs_rebuild: bool
        completed_at: _timestamp_pb2.Timestamp
        rejected_at: _timestamp_pb2.Timestamp
        completion_reason: str
        rejection_reason: str
        completed_by: str
        rejected_by: str
        def __init__(self, is_pending: bool = ..., is_completed: bool = ..., is_rejected: bool = ..., is_verified: bool = ..., needs_rebuild: bool = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion_reason: _Optional[str] = ..., rejection_reason: _Optional[str] = ..., completed_by: _Optional[str] = ..., rejected_by: _Optional[str] = ...) -> None: ...
    class Payment(_message.Message):
        __slots__ = ["created_at", "payment_provider_id", "payment_id", "payment_method_id", "is_pending", "is_completed", "is_rejected", "completed_at", "rejected_at", "rejection_reason", "converted_currency_id", "converted_amount", "amount"]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
        IS_PENDING_FIELD_NUMBER: _ClassVar[int]
        IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        IS_REJECTED_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
        REJECTED_AT_FIELD_NUMBER: _ClassVar[int]
        REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
        CONVERTED_CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
        CONVERTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        created_at: _timestamp_pb2.Timestamp
        payment_provider_id: str
        payment_id: str
        payment_method_id: str
        is_pending: bool
        is_completed: bool
        is_rejected: bool
        completed_at: _timestamp_pb2.Timestamp
        rejected_at: _timestamp_pb2.Timestamp
        rejection_reason: str
        converted_currency_id: str
        converted_amount: float
        amount: float
        def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., payment_provider_id: _Optional[str] = ..., payment_id: _Optional[str] = ..., payment_method_id: _Optional[str] = ..., is_pending: bool = ..., is_completed: bool = ..., is_rejected: bool = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejection_reason: _Optional[str] = ..., converted_currency_id: _Optional[str] = ..., converted_amount: _Optional[float] = ..., amount: _Optional[float] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_MANUAL_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_ORDER_BASED_FIELD_NUMBER: _ClassVar[int]
    INVOICE_BUILDER_VERSION_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_EXCL_TAXES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VAT_FIELD_NUMBER: _ClassVar[int]
    VAT_REVERSE_CHARGE_FIELD_NUMBER: _ClassVar[int]
    VAT_PERCENTAGE_USED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SALES_TAX_FIELD_NUMBER: _ClassVar[int]
    SALES_TAX_PERCENTAGE_USED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_INCL_TAXES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    organization_id: str
    organization_name: str
    entity_id: str
    entity_name: str
    invoice_number: str
    created_at: _timestamp_pb2.Timestamp
    requires_manual_verification: bool
    last_updated_at: _timestamp_pb2.Timestamp
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    purchase_order_based: bool
    invoice_builder_version: str
    items: _containers.RepeatedCompositeFieldContainer[Invoice.Item]
    currency_id: str
    total_amount_excl_taxes: float
    total_vat: float
    vat_reverse_charge: bool
    vat_percentage_used: float
    total_sales_tax: float
    sales_tax_percentage_used: float
    total_amount_incl_taxes: float
    status: Invoice.Status
    payments: _containers.RepeatedCompositeFieldContainer[Invoice.Payment]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., organization_name: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_name: _Optional[str] = ..., invoice_number: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., requires_manual_verification: bool = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., email_addresses: _Optional[_Iterable[str]] = ..., purchase_order_based: bool = ..., invoice_builder_version: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Invoice.Item, _Mapping]]] = ..., currency_id: _Optional[str] = ..., total_amount_excl_taxes: _Optional[float] = ..., total_vat: _Optional[float] = ..., vat_reverse_charge: bool = ..., vat_percentage_used: _Optional[float] = ..., total_sales_tax: _Optional[float] = ..., sales_tax_percentage_used: _Optional[float] = ..., total_amount_incl_taxes: _Optional[float] = ..., status: _Optional[_Union[Invoice.Status, _Mapping]] = ..., payments: _Optional[_Iterable[_Union[Invoice.Payment, _Mapping]]] = ...) -> None: ...

class InvoiceList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Invoice]
    def __init__(self, items: _Optional[_Iterable[_Union[Invoice, _Mapping]]] = ...) -> None: ...

class ListInvoicesRequest(_message.Message):
    __slots__ = ["organization_id", "to", "options", "include_usageitem_ids"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USAGEITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    to: _timestamp_pb2.Timestamp
    options: _common_pb2.ListOptions
    include_usageitem_ids: bool
    def __init__(self, organization_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., include_usageitem_ids: bool = ..., **kwargs) -> None: ...

class GetPreliminaryInvoiceRequest(_message.Message):
    __slots__ = ["organization_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ...) -> None: ...

class PaymentProvider(_message.Message):
    __slots__ = ["id", "name", "description", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    type: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class PaymentProviderList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PaymentProvider]
    def __init__(self, items: _Optional[_Iterable[_Union[PaymentProvider, _Mapping]]] = ...) -> None: ...

class PreparePaymentMethodRequest(_message.Message):
    __slots__ = ["provider_id", "organization_id", "currency_id"]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    organization_id: str
    currency_id: str
    def __init__(self, provider_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., currency_id: _Optional[str] = ...) -> None: ...

class PreparedPaymentMethod(_message.Message):
    __slots__ = ["provider_id", "organization_id", "currency_id", "token", "script_url", "signature"]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_URL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    organization_id: str
    currency_id: str
    token: str
    script_url: str
    signature: str
    def __init__(self, provider_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., currency_id: _Optional[str] = ..., token: _Optional[str] = ..., script_url: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class CreatePaymentMethodRequest(_message.Message):
    __slots__ = ["prepared_payment_method", "first_name", "last_name"]
    PREPARED_PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    prepared_payment_method: PreparedPaymentMethod
    first_name: str
    last_name: str
    def __init__(self, prepared_payment_method: _Optional[_Union[PreparedPaymentMethod, _Mapping]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class ListPaymentProvidersRequest(_message.Message):
    __slots__ = ["organization_id", "options", "include_internal"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    options: _common_pb2.ListOptions
    include_internal: bool
    def __init__(self, organization_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., include_internal: bool = ...) -> None: ...

class PaymentMethod(_message.Message):
    __slots__ = ["id", "name", "description", "payment_provider_id", "organization_id", "created_at", "deleted_at", "is_deleted", "valid_until", "token", "type", "is_default", "currency_id", "credit_card_info"]
    class CreditCardInfo(_message.Message):
        __slots__ = ["last_digits", "card_type"]
        LAST_DIGITS_FIELD_NUMBER: _ClassVar[int]
        CARD_TYPE_FIELD_NUMBER: _ClassVar[int]
        last_digits: str
        card_type: str
        def __init__(self, last_digits: _Optional[str] = ..., card_type: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    CREDIT_CARD_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    payment_provider_id: str
    organization_id: str
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    is_deleted: bool
    valid_until: _timestamp_pb2.Timestamp
    token: str
    type: str
    is_default: bool
    currency_id: str
    credit_card_info: PaymentMethod.CreditCardInfo
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., payment_provider_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., token: _Optional[str] = ..., type: _Optional[str] = ..., is_default: bool = ..., currency_id: _Optional[str] = ..., credit_card_info: _Optional[_Union[PaymentMethod.CreditCardInfo, _Mapping]] = ...) -> None: ...

class PaymentMethodList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    def __init__(self, items: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ...) -> None: ...

class ListPaymentMethodsRequest(_message.Message):
    __slots__ = ["organization_id", "options"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    options: _common_pb2.ListOptions
    def __init__(self, organization_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class SetDefaultPaymentMethodRequest(_message.Message):
    __slots__ = ["organization_id", "payment_method_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    payment_method_id: str
    def __init__(self, organization_id: _Optional[str] = ..., payment_method_id: _Optional[str] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ["address", "zipcode", "city", "state", "country_code"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ZIPCODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    address: _containers.RepeatedScalarFieldContainer[str]
    zipcode: str
    city: str
    state: str
    country_code: str
    def __init__(self, address: _Optional[_Iterable[str]] = ..., zipcode: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country_code: _Optional[str] = ...) -> None: ...

class OrganizationBillingFlags(_message.Message):
    __slots__ = ["is_allowed_to_list_invoices", "is_allowed_to_access_payment_methods"]
    IS_ALLOWED_TO_LIST_INVOICES_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_TO_ACCESS_PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    is_allowed_to_list_invoices: bool
    is_allowed_to_access_payment_methods: bool
    def __init__(self, is_allowed_to_list_invoices: bool = ..., is_allowed_to_access_payment_methods: bool = ...) -> None: ...

class BillingConfig(_message.Message):
    __slots__ = ["address", "vat_number", "email_addresses", "us_tax_number", "company_legal_name"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VAT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    US_TAX_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COMPANY_LEGAL_NAME_FIELD_NUMBER: _ClassVar[int]
    address: Address
    vat_number: str
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    us_tax_number: str
    company_legal_name: str
    def __init__(self, address: _Optional[_Union[Address, _Mapping]] = ..., vat_number: _Optional[str] = ..., email_addresses: _Optional[_Iterable[str]] = ..., us_tax_number: _Optional[str] = ..., company_legal_name: _Optional[str] = ...) -> None: ...

class SetBillingConfigRequest(_message.Message):
    __slots__ = ["organization_id", "config"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    config: BillingConfig
    def __init__(self, organization_id: _Optional[str] = ..., config: _Optional[_Union[BillingConfig, _Mapping]] = ...) -> None: ...

class PDFDocument(_message.Message):
    __slots__ = ["content", "filename"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    filename: str
    def __init__(self, content: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class GetAvailableCreditsRequest(_message.Message):
    __slots__ = ["organization_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ...) -> None: ...

class AvailableCredits(_message.Message):
    __slots__ = ["credits"]
    class CreditCurrencyAmount(_message.Message):
        __slots__ = ["amount", "currency_id"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
        amount: float
        currency_id: str
        def __init__(self, amount: _Optional[float] = ..., currency_id: _Optional[str] = ...) -> None: ...
    CREDITS_FIELD_NUMBER: _ClassVar[int]
    credits: _containers.RepeatedCompositeFieldContainer[AvailableCredits.CreditCurrencyAmount]
    def __init__(self, credits: _Optional[_Iterable[_Union[AvailableCredits.CreditCurrencyAmount, _Mapping]]] = ...) -> None: ...
