from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ["address", "city", "country_code", "state", "zipcode"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIPCODE_FIELD_NUMBER: _ClassVar[int]
    address: _containers.RepeatedScalarFieldContainer[str]
    city: str
    country_code: str
    state: str
    zipcode: str
    def __init__(self, address: _Optional[_Iterable[str]] = ..., zipcode: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country_code: _Optional[str] = ...) -> None: ...

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

class BillingConfig(_message.Message):
    __slots__ = ["address", "company_legal_name", "email_addresses", "us_tax_number", "vat_number"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COMPANY_LEGAL_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    US_TAX_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VAT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    address: Address
    company_legal_name: str
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    us_tax_number: str
    vat_number: str
    def __init__(self, address: _Optional[_Union[Address, _Mapping]] = ..., vat_number: _Optional[str] = ..., email_addresses: _Optional[_Iterable[str]] = ..., us_tax_number: _Optional[str] = ..., company_legal_name: _Optional[str] = ...) -> None: ...

class CreatePaymentMethodRequest(_message.Message):
    __slots__ = ["first_name", "last_name", "prepared_payment_method"]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PREPARED_PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    prepared_payment_method: PreparedPaymentMethod
    def __init__(self, prepared_payment_method: _Optional[_Union[PreparedPaymentMethod, _Mapping]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class GetAvailableCreditsRequest(_message.Message):
    __slots__ = ["organization_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ...) -> None: ...

class GetPreliminaryInvoiceRequest(_message.Message):
    __slots__ = ["organization_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ...) -> None: ...

class Invoice(_message.Message):
    __slots__ = ["created_at", "currency_id", "email_addresses", "entity_id", "entity_name", "id", "invoice_builder_version", "invoice_number", "items", "last_updated_at", "organization_id", "organization_name", "payments", "purchase_order_based", "requires_manual_verification", "sales_tax_percentage_used", "status", "total_amount_excl_taxes", "total_amount_incl_taxes", "total_sales_tax", "total_vat", "url", "vat_percentage_used", "vat_reverse_charge"]
    class Item(_message.Message):
        __slots__ = ["amount", "description", "is_prepaid", "usageitem_ids"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_PREPAID_FIELD_NUMBER: _ClassVar[int]
        USAGEITEM_IDS_FIELD_NUMBER: _ClassVar[int]
        amount: float
        description: str
        is_prepaid: bool
        usageitem_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, usageitem_ids: _Optional[_Iterable[str]] = ..., amount: _Optional[float] = ..., description: _Optional[str] = ..., is_prepaid: bool = ...) -> None: ...
    class Payment(_message.Message):
        __slots__ = ["amount", "completed_at", "converted_amount", "converted_currency_id", "created_at", "is_completed", "is_pending", "is_rejected", "payment_id", "payment_method_id", "payment_provider_id", "rejected_at", "rejection_reason"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
        CONVERTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        CONVERTED_CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        IS_PENDING_FIELD_NUMBER: _ClassVar[int]
        IS_REJECTED_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
        REJECTED_AT_FIELD_NUMBER: _ClassVar[int]
        REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
        amount: float
        completed_at: _timestamp_pb2.Timestamp
        converted_amount: float
        converted_currency_id: str
        created_at: _timestamp_pb2.Timestamp
        is_completed: bool
        is_pending: bool
        is_rejected: bool
        payment_id: str
        payment_method_id: str
        payment_provider_id: str
        rejected_at: _timestamp_pb2.Timestamp
        rejection_reason: str
        def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., payment_provider_id: _Optional[str] = ..., payment_id: _Optional[str] = ..., payment_method_id: _Optional[str] = ..., is_pending: bool = ..., is_completed: bool = ..., is_rejected: bool = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejection_reason: _Optional[str] = ..., converted_currency_id: _Optional[str] = ..., converted_amount: _Optional[float] = ..., amount: _Optional[float] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["completed_at", "completed_by", "completion_reason", "is_completed", "is_pending", "is_rejected", "is_verified", "needs_rebuild", "rejected_at", "rejected_by", "rejection_reason"]
        COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_BY_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_REASON_FIELD_NUMBER: _ClassVar[int]
        IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        IS_PENDING_FIELD_NUMBER: _ClassVar[int]
        IS_REJECTED_FIELD_NUMBER: _ClassVar[int]
        IS_VERIFIED_FIELD_NUMBER: _ClassVar[int]
        NEEDS_REBUILD_FIELD_NUMBER: _ClassVar[int]
        REJECTED_AT_FIELD_NUMBER: _ClassVar[int]
        REJECTED_BY_FIELD_NUMBER: _ClassVar[int]
        REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
        completed_at: _timestamp_pb2.Timestamp
        completed_by: str
        completion_reason: str
        is_completed: bool
        is_pending: bool
        is_rejected: bool
        is_verified: bool
        needs_rebuild: bool
        rejected_at: _timestamp_pb2.Timestamp
        rejected_by: str
        rejection_reason: str
        def __init__(self, is_pending: bool = ..., is_completed: bool = ..., is_rejected: bool = ..., is_verified: bool = ..., needs_rebuild: bool = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion_reason: _Optional[str] = ..., rejection_reason: _Optional[str] = ..., completed_by: _Optional[str] = ..., rejected_by: _Optional[str] = ...) -> None: ...
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_BUILDER_VERSION_FIELD_NUMBER: _ClassVar[int]
    INVOICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_ORDER_BASED_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_MANUAL_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    SALES_TAX_PERCENTAGE_USED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_EXCL_TAXES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_INCL_TAXES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SALES_TAX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VAT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VAT_PERCENTAGE_USED_FIELD_NUMBER: _ClassVar[int]
    VAT_REVERSE_CHARGE_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    currency_id: str
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    entity_id: str
    entity_name: str
    id: str
    invoice_builder_version: str
    invoice_number: str
    items: _containers.RepeatedCompositeFieldContainer[Invoice.Item]
    last_updated_at: _timestamp_pb2.Timestamp
    organization_id: str
    organization_name: str
    payments: _containers.RepeatedCompositeFieldContainer[Invoice.Payment]
    purchase_order_based: bool
    requires_manual_verification: bool
    sales_tax_percentage_used: float
    status: Invoice.Status
    total_amount_excl_taxes: float
    total_amount_incl_taxes: float
    total_sales_tax: float
    total_vat: float
    url: str
    vat_percentage_used: float
    vat_reverse_charge: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., organization_id: _Optional[str] = ..., organization_name: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_name: _Optional[str] = ..., invoice_number: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., requires_manual_verification: bool = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., email_addresses: _Optional[_Iterable[str]] = ..., purchase_order_based: bool = ..., invoice_builder_version: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Invoice.Item, _Mapping]]] = ..., currency_id: _Optional[str] = ..., total_amount_excl_taxes: _Optional[float] = ..., total_vat: _Optional[float] = ..., vat_reverse_charge: bool = ..., vat_percentage_used: _Optional[float] = ..., total_sales_tax: _Optional[float] = ..., sales_tax_percentage_used: _Optional[float] = ..., total_amount_incl_taxes: _Optional[float] = ..., status: _Optional[_Union[Invoice.Status, _Mapping]] = ..., payments: _Optional[_Iterable[_Union[Invoice.Payment, _Mapping]]] = ...) -> None: ...

class InvoiceList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Invoice]
    def __init__(self, items: _Optional[_Iterable[_Union[Invoice, _Mapping]]] = ...) -> None: ...

class ListInvoicesRequest(_message.Message):
    __slots__ = ["include_usageitem_ids", "options", "organization_id", "to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USAGEITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    include_usageitem_ids: bool
    options: _common_pb2.ListOptions
    organization_id: str
    to: _timestamp_pb2.Timestamp
    def __init__(self, organization_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., include_usageitem_ids: bool = ..., **kwargs) -> None: ...

class ListPaymentMethodsRequest(_message.Message):
    __slots__ = ["options", "organization_id"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ...) -> None: ...

class ListPaymentProvidersRequest(_message.Message):
    __slots__ = ["include_internal", "options", "organization_id"]
    INCLUDE_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    include_internal: bool
    options: _common_pb2.ListOptions
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.ListOptions, _Mapping]] = ..., include_internal: bool = ...) -> None: ...

class OrganizationBillingFlags(_message.Message):
    __slots__ = ["is_allowed_to_access_payment_methods", "is_allowed_to_list_invoices"]
    IS_ALLOWED_TO_ACCESS_PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_TO_LIST_INVOICES_FIELD_NUMBER: _ClassVar[int]
    is_allowed_to_access_payment_methods: bool
    is_allowed_to_list_invoices: bool
    def __init__(self, is_allowed_to_list_invoices: bool = ..., is_allowed_to_access_payment_methods: bool = ...) -> None: ...

class PDFDocument(_message.Message):
    __slots__ = ["content", "filename"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    filename: str
    def __init__(self, content: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class PaymentMethod(_message.Message):
    __slots__ = ["created_at", "credit_card_info", "currency_id", "deleted_at", "description", "id", "is_default", "is_deleted", "name", "organization_id", "payment_provider_id", "token", "type", "valid_until"]
    class CreditCardInfo(_message.Message):
        __slots__ = ["card_type", "last_digits"]
        CARD_TYPE_FIELD_NUMBER: _ClassVar[int]
        LAST_DIGITS_FIELD_NUMBER: _ClassVar[int]
        card_type: str
        last_digits: str
        def __init__(self, last_digits: _Optional[str] = ..., card_type: _Optional[str] = ...) -> None: ...
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREDIT_CARD_INFO_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    credit_card_info: PaymentMethod.CreditCardInfo
    currency_id: str
    deleted_at: _timestamp_pb2.Timestamp
    description: str
    id: str
    is_default: bool
    is_deleted: bool
    name: str
    organization_id: str
    payment_provider_id: str
    token: str
    type: str
    valid_until: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., payment_provider_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., token: _Optional[str] = ..., type: _Optional[str] = ..., is_default: bool = ..., currency_id: _Optional[str] = ..., credit_card_info: _Optional[_Union[PaymentMethod.CreditCardInfo, _Mapping]] = ...) -> None: ...

class PaymentMethodList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    def __init__(self, items: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ...) -> None: ...

class PaymentProvider(_message.Message):
    __slots__ = ["description", "id", "name", "type"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    name: str
    type: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class PaymentProviderList(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PaymentProvider]
    def __init__(self, items: _Optional[_Iterable[_Union[PaymentProvider, _Mapping]]] = ...) -> None: ...

class PreparePaymentMethodRequest(_message.Message):
    __slots__ = ["currency_id", "organization_id", "provider_id"]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    currency_id: str
    organization_id: str
    provider_id: str
    def __init__(self, provider_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., currency_id: _Optional[str] = ...) -> None: ...

class PreparedPaymentMethod(_message.Message):
    __slots__ = ["currency_id", "organization_id", "provider_id", "script_url", "signature", "token"]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_URL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    currency_id: str
    organization_id: str
    provider_id: str
    script_url: str
    signature: str
    token: str
    def __init__(self, provider_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., currency_id: _Optional[str] = ..., token: _Optional[str] = ..., script_url: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class SetBillingConfigRequest(_message.Message):
    __slots__ = ["config", "organization_id"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    config: BillingConfig
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ..., config: _Optional[_Union[BillingConfig, _Mapping]] = ...) -> None: ...

class SetDefaultPaymentMethodRequest(_message.Message):
    __slots__ = ["organization_id", "payment_method_id"]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    payment_method_id: str
    def __init__(self, organization_id: _Optional[str] = ..., payment_method_id: _Optional[str] = ...) -> None: ...
