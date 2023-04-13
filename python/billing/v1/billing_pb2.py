# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: billing/v1/billing.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as github_dot_com_dot_golang_dot_protobuf_dot_ptypes_dot_timestamp_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x62illing/v1/billing.proto\x12\x19\x61rangodb.cloud.billing.v1\x1a\x16\x63ommon/v1/common.proto\x1a;github.com/golang/protobuf/ptypes/timestamp/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xa9\x0c\n\x07Invoice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x17\n\x0forganization_id\x18\x03 \x01(\t\x12\x19\n\x11organization_name\x18\x04 \x01(\t\x12\x11\n\tentity_id\x18\x05 \x01(\t\x12\x13\n\x0b\x65ntity_name\x18\x06 \x01(\t\x12\x16\n\x0einvoice_number\x18\x07 \x01(\t\x12.\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x1crequires_manual_verification\x18\x0b \x01(\x08\x12\x33\n\x0flast_updated_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0f\x65mail_addresses\x18\r \x03(\t\x12\x1c\n\x14purchase_order_based\x18\x0e \x01(\x08\x12\x1f\n\x17invoice_builder_version\x18\x14 \x01(\t\x12\x36\n\x05items\x18\x64 \x03(\x0b\x32\'.arangodb.cloud.billing.v1.Invoice.Item\x12\x13\n\x0b\x63urrency_id\x18n \x01(\t\x12\x1f\n\x17total_amount_excl_taxes\x18o \x01(\x02\x12\x11\n\ttotal_vat\x18p \x01(\x02\x12\x1a\n\x12vat_reverse_charge\x18r \x01(\x08\x12\x1b\n\x13vat_percentage_used\x18s \x01(\x02\x12\x17\n\x0ftotal_sales_tax\x18t \x01(\x02\x12!\n\x19sales_tax_percentage_used\x18u \x01(\x02\x12\x1f\n\x17total_amount_incl_taxes\x18q \x01(\x02\x12:\n\x06status\x18\xc8\x01 \x01(\x0b\x32).arangodb.cloud.billing.v1.Invoice.Status\x12=\n\x08payments\x18\xc9\x01 \x03(\x0b\x32*.arangodb.cloud.billing.v1.Invoice.Payment\x1aV\n\x04Item\x12\x15\n\rusageitem_ids\x18\x04 \x03(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x02\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\nis_prepaid\x18\x05 \x01(\x08\x1a\xb6\x02\n\x06Status\x12\x12\n\nis_pending\x18\x01 \x01(\x08\x12\x14\n\x0cis_completed\x18\x02 \x01(\x08\x12\x13\n\x0bis_rejected\x18\x03 \x01(\x08\x12\x13\n\x0bis_verified\x18\x04 \x01(\x08\x12\x15\n\rneeds_rebuild\x18\x05 \x01(\x08\x12\x30\n\x0c\x63ompleted_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0brejected_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11\x63ompletion_reason\x18\x0c \x01(\t\x12\x18\n\x10rejection_reason\x18\r \x01(\t\x12\x14\n\x0c\x63ompleted_by\x18\x0e \x01(\t\x12\x13\n\x0brejected_by\x18\x0f \x01(\t\x1a\x8a\x03\n\x07Payment\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13payment_provider_id\x18\x02 \x01(\t\x12\x12\n\npayment_id\x18\x03 \x01(\t\x12\x19\n\x11payment_method_id\x18\x04 \x01(\t\x12\x12\n\nis_pending\x18\n \x01(\x08\x12\x14\n\x0cis_completed\x18\x0b \x01(\x08\x12\x13\n\x0bis_rejected\x18\x0c \x01(\x08\x12\x30\n\x0c\x63ompleted_at\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0brejected_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10rejection_reason\x18\x16 \x01(\t\x12\x1d\n\x15\x63onverted_currency_id\x18\x1e \x01(\t\x12\x18\n\x10\x63onverted_amount\x18\x1f \x01(\x02\x12\x0e\n\x06\x61mount\x18  \x01(\x02\"@\n\x0bInvoiceList\x12\x31\n\x05items\x18\x01 \x03(\x0b\x32\".arangodb.cloud.billing.v1.Invoice\"\xd7\x01\n\x13ListInvoicesRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12(\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x07options\x18\n \x01(\x0b\x32%.arangodb.cloud.common.v1.ListOptions\x12\x1d\n\x15include_usageitem_ids\x18\x14 \x01(\x08\"7\n\x1cGetPreliminaryInvoiceRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\"N\n\x0fPaymentProvider\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\"P\n\x13PaymentProviderList\x12\x39\n\x05items\x18\x01 \x03(\x0b\x32*.arangodb.cloud.billing.v1.PaymentProvider\"`\n\x1bPreparePaymentMethodRequest\x12\x13\n\x0bprovider_id\x18\x01 \x01(\t\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\x12\x13\n\x0b\x63urrency_id\x18\x03 \x01(\t\"\x90\x01\n\x15PreparedPaymentMethod\x12\x13\n\x0bprovider_id\x18\x01 \x01(\t\x12\x17\n\x0forganization_id\x18\x02 \x01(\t\x12\x13\n\x0b\x63urrency_id\x18\x03 \x01(\t\x12\r\n\x05token\x18\x0b \x01(\t\x12\x12\n\nscript_url\x18\x0c \x01(\t\x12\x11\n\tsignature\x18\x65 \x01(\t\"\x96\x01\n\x1a\x43reatePaymentMethodRequest\x12Q\n\x17prepared_payment_method\x18\x01 \x01(\x0b\x32\x30.arangodb.cloud.billing.v1.PreparedPaymentMethod\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\"\x88\x01\n\x1bListPaymentProvidersRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x36\n\x07options\x18\x02 \x01(\x0b\x32%.arangodb.cloud.common.v1.ListOptions\x12\x18\n\x10include_internal\x18\x03 \x01(\x08\"\xec\x03\n\rPaymentMethod\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1b\n\x13payment_provider_id\x18\x04 \x01(\t\x12\x17\n\x0forganization_id\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nis_deleted\x18\x0c \x01(\x08\x12/\n\x0bvalid_until\x18\r \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05token\x18\x0e \x01(\t\x12\x0c\n\x04type\x18\x0f \x01(\t\x12\x12\n\nis_default\x18\x10 \x01(\x08\x12\x13\n\x0b\x63urrency_id\x18\x11 \x01(\t\x12Q\n\x10\x63redit_card_info\x18\x65 \x01(\x0b\x32\x37.arangodb.cloud.billing.v1.PaymentMethod.CreditCardInfo\x1a\x38\n\x0e\x43reditCardInfo\x12\x13\n\x0blast_digits\x18\x01 \x01(\t\x12\x11\n\tcard_type\x18\x02 \x01(\t\"L\n\x11PaymentMethodList\x12\x37\n\x05items\x18\x01 \x03(\x0b\x32(.arangodb.cloud.billing.v1.PaymentMethod\"l\n\x19ListPaymentMethodsRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x36\n\x07options\x18\x02 \x01(\x0b\x32%.arangodb.cloud.common.v1.ListOptions\"T\n\x1eSetDefaultPaymentMethodRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x19\n\x11payment_method_id\x18\x02 \x01(\t\"^\n\x07\x41\x64\x64ress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x03(\t\x12\x0f\n\x07zipcode\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x05 \x01(\t\"m\n\x18OrganizationBillingFlags\x12#\n\x1bis_allowed_to_list_invoices\x18\x01 \x01(\x08\x12,\n$is_allowed_to_access_payment_methods\x18\x02 \x01(\x08\"\xa4\x01\n\rBillingConfig\x12\x33\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\".arangodb.cloud.billing.v1.Address\x12\x12\n\nvat_number\x18\x02 \x01(\t\x12\x17\n\x0f\x65mail_addresses\x18\x03 \x03(\t\x12\x15\n\rus_tax_number\x18\x04 \x01(\t\x12\x1a\n\x12\x63ompany_legal_name\x18\x05 \x01(\t\"l\n\x17SetBillingConfigRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x38\n\x06\x63onfig\x18\x02 \x01(\x0b\x32(.arangodb.cloud.billing.v1.BillingConfig\"0\n\x0bPDFDocument\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"5\n\x1aGetAvailableCreditsRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\"\xa2\x01\n\x10\x41vailableCredits\x12Q\n\x07\x63redits\x18\x01 \x03(\x0b\x32@.arangodb.cloud.billing.v1.AvailableCredits.CreditCurrencyAmount\x1a;\n\x14\x43reditCurrencyAmount\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x02\x12\x13\n\x0b\x63urrency_id\x18\x02 \x01(\t2\xde\x18\n\x0e\x42illingService\x12x\n\rGetAPIVersion\x12\x1f.arangodb.cloud.common.v1.Empty\x1a!.arangodb.cloud.common.v1.Version\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/api/billing/v1/api-version\x12\xb0\x01\n\x1bGetOrganizationBillingFlags\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x33.arangodb.cloud.billing.v1.OrganizationBillingFlags\"7\x82\xd3\xe4\x93\x02\x31\x12//api/billing/v1/organization/{id}/billing-flags\x12\xa7\x01\n\x0cListInvoices\x12..arangodb.cloud.billing.v1.ListInvoicesRequest\x1a&.arangodb.cloud.billing.v1.InvoiceList\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/api/billing/v1/organization/{organization_id}/invoices\x12|\n\nGetInvoice\x12#.arangodb.cloud.common.v1.IDOptions\x1a\".arangodb.cloud.billing.v1.Invoice\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/api/billing/v1/invoices/{id}\x12\xb4\x01\n\x15GetPreliminaryInvoice\x12\x37.arangodb.cloud.billing.v1.GetPreliminaryInvoiceRequest\x1a\".arangodb.cloud.billing.v1.Invoice\">\x82\xd3\xe4\x93\x02\x38\x12\x36/api/billing/v1/invoices/{organization_id}/preliminary\x12\x87\x01\n\rGetInvoicePDF\x12#.arangodb.cloud.common.v1.IDOptions\x1a&.arangodb.cloud.billing.v1.PDFDocument\")\x82\xd3\xe4\x93\x02#\x12!/api/billing/v1/invoices/{id}/pdf\x12\xc7\x01\n\x14ListPaymentProviders\x12\x36.arangodb.cloud.billing.v1.ListPaymentProvidersRequest\x1a..arangodb.cloud.billing.v1.PaymentProviderList\"G\x82\xd3\xe4\x93\x02\x41\x12?/api/billing/v1/organization/{organization_id}/paymentproviders\x12\x94\x01\n\x12GetPaymentProvider\x12#.arangodb.cloud.common.v1.IDOptions\x1a*.arangodb.cloud.billing.v1.PaymentProvider\"-\x82\xd3\xe4\x93\x02\'\x12%/api/billing/v1/paymentproviders/{id}\x12\xbf\x01\n\x12ListPaymentMethods\x12\x34.arangodb.cloud.billing.v1.ListPaymentMethodsRequest\x1a,.arangodb.cloud.billing.v1.PaymentMethodList\"E\x82\xd3\xe4\x93\x02?\x12=/api/billing/v1/organization/{organization_id}/paymentmethods\x12\x8e\x01\n\x10GetPaymentMethod\x12#.arangodb.cloud.common.v1.IDOptions\x1a(.arangodb.cloud.billing.v1.PaymentMethod\"+\x82\xd3\xe4\x93\x02%\x12#/api/billing/v1/paymentmethods/{id}\x12\xc3\x01\n\x14PreparePaymentMethod\x12\x36.arangodb.cloud.billing.v1.PreparePaymentMethodRequest\x1a\x30.arangodb.cloud.billing.v1.PreparedPaymentMethod\"A\x82\xd3\xe4\x93\x02;\"6/api/billing/v1/paymentproviders/{provider_id}/prepare:\x01*\x12\xa1\x01\n\x13\x43reatePaymentMethod\x12\x35.arangodb.cloud.billing.v1.CreatePaymentMethodRequest\x1a(.arangodb.cloud.billing.v1.PaymentMethod\")\x82\xd3\xe4\x93\x02#\"\x1e/api/billing/v1/paymentmethods:\x01*\x12\x99\x01\n\x13UpdatePaymentMethod\x12(.arangodb.cloud.billing.v1.PaymentMethod\x1a(.arangodb.cloud.billing.v1.PaymentMethod\".\x82\xd3\xe4\x93\x02(\x1a#/api/billing/v1/paymentmethods/{id}:\x01*\x12\x88\x01\n\x13\x44\x65letePaymentMethod\x12#.arangodb.cloud.common.v1.IDOptions\x1a\x1f.arangodb.cloud.common.v1.Empty\"+\x82\xd3\xe4\x93\x02%*#/api/billing/v1/paymentmethods/{id}\x12\xa9\x01\n\x17GetDefaultPaymentMethod\x12#.arangodb.cloud.common.v1.IDOptions\x1a(.arangodb.cloud.billing.v1.PaymentMethod\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/api/billing/v1/organization/{id}/default-paymentmethod\x12\xc6\x01\n\x17SetDefaultPaymentMethod\x12\x39.arangodb.cloud.billing.v1.SetDefaultPaymentMethodRequest\x1a\x1f.arangodb.cloud.common.v1.Empty\"O\x82\xd3\xe4\x93\x02I\x1a\x44/api/billing/v1/organization/{organization_id}/default-paymentmethod:\x01*\x12\x93\x01\n\x10GetBillingConfig\x12#.arangodb.cloud.common.v1.IDOptions\x1a(.arangodb.cloud.billing.v1.BillingConfig\"0\x82\xd3\xe4\x93\x02*\x12(/api/billing/v1/organization/{id}/config\x12\xa9\x01\n\x10SetBillingConfig\x12\x32.arangodb.cloud.billing.v1.SetBillingConfigRequest\x1a\x1f.arangodb.cloud.common.v1.Empty\"@\x82\xd3\xe4\x93\x02:\x1a\x35/api/billing/v1/organization/{organization_id}/config:\x01*\x12\xb9\x01\n\x13GetAvailableCredits\x12\x35.arangodb.cloud.billing.v1.GetAvailableCreditsRequest\x1a+.arangodb.cloud.billing.v1.AvailableCredits\">\x82\xd3\xe4\x93\x02\x38\x12\x36/api/billing/v1/organization/{organization_id}/creditsB-Z+github.com/arangodb-managed/apis/billing/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'billing.v1.billing_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/arangodb-managed/apis/billing/v1'
  _BILLINGSERVICE.methods_by_name['GetAPIVersion']._options = None
  _BILLINGSERVICE.methods_by_name['GetAPIVersion']._serialized_options = b'\202\323\344\223\002\035\022\033/api/billing/v1/api-version'
  _BILLINGSERVICE.methods_by_name['GetOrganizationBillingFlags']._options = None
  _BILLINGSERVICE.methods_by_name['GetOrganizationBillingFlags']._serialized_options = b'\202\323\344\223\0021\022//api/billing/v1/organization/{id}/billing-flags'
  _BILLINGSERVICE.methods_by_name['ListInvoices']._options = None
  _BILLINGSERVICE.methods_by_name['ListInvoices']._serialized_options = b'\202\323\344\223\0029\0227/api/billing/v1/organization/{organization_id}/invoices'
  _BILLINGSERVICE.methods_by_name['GetInvoice']._options = None
  _BILLINGSERVICE.methods_by_name['GetInvoice']._serialized_options = b'\202\323\344\223\002\037\022\035/api/billing/v1/invoices/{id}'
  _BILLINGSERVICE.methods_by_name['GetPreliminaryInvoice']._options = None
  _BILLINGSERVICE.methods_by_name['GetPreliminaryInvoice']._serialized_options = b'\202\323\344\223\0028\0226/api/billing/v1/invoices/{organization_id}/preliminary'
  _BILLINGSERVICE.methods_by_name['GetInvoicePDF']._options = None
  _BILLINGSERVICE.methods_by_name['GetInvoicePDF']._serialized_options = b'\202\323\344\223\002#\022!/api/billing/v1/invoices/{id}/pdf'
  _BILLINGSERVICE.methods_by_name['ListPaymentProviders']._options = None
  _BILLINGSERVICE.methods_by_name['ListPaymentProviders']._serialized_options = b'\202\323\344\223\002A\022?/api/billing/v1/organization/{organization_id}/paymentproviders'
  _BILLINGSERVICE.methods_by_name['GetPaymentProvider']._options = None
  _BILLINGSERVICE.methods_by_name['GetPaymentProvider']._serialized_options = b'\202\323\344\223\002\'\022%/api/billing/v1/paymentproviders/{id}'
  _BILLINGSERVICE.methods_by_name['ListPaymentMethods']._options = None
  _BILLINGSERVICE.methods_by_name['ListPaymentMethods']._serialized_options = b'\202\323\344\223\002?\022=/api/billing/v1/organization/{organization_id}/paymentmethods'
  _BILLINGSERVICE.methods_by_name['GetPaymentMethod']._options = None
  _BILLINGSERVICE.methods_by_name['GetPaymentMethod']._serialized_options = b'\202\323\344\223\002%\022#/api/billing/v1/paymentmethods/{id}'
  _BILLINGSERVICE.methods_by_name['PreparePaymentMethod']._options = None
  _BILLINGSERVICE.methods_by_name['PreparePaymentMethod']._serialized_options = b'\202\323\344\223\002;\"6/api/billing/v1/paymentproviders/{provider_id}/prepare:\001*'
  _BILLINGSERVICE.methods_by_name['CreatePaymentMethod']._options = None
  _BILLINGSERVICE.methods_by_name['CreatePaymentMethod']._serialized_options = b'\202\323\344\223\002#\"\036/api/billing/v1/paymentmethods:\001*'
  _BILLINGSERVICE.methods_by_name['UpdatePaymentMethod']._options = None
  _BILLINGSERVICE.methods_by_name['UpdatePaymentMethod']._serialized_options = b'\202\323\344\223\002(\032#/api/billing/v1/paymentmethods/{id}:\001*'
  _BILLINGSERVICE.methods_by_name['DeletePaymentMethod']._options = None
  _BILLINGSERVICE.methods_by_name['DeletePaymentMethod']._serialized_options = b'\202\323\344\223\002%*#/api/billing/v1/paymentmethods/{id}'
  _BILLINGSERVICE.methods_by_name['GetDefaultPaymentMethod']._options = None
  _BILLINGSERVICE.methods_by_name['GetDefaultPaymentMethod']._serialized_options = b'\202\323\344\223\0029\0227/api/billing/v1/organization/{id}/default-paymentmethod'
  _BILLINGSERVICE.methods_by_name['SetDefaultPaymentMethod']._options = None
  _BILLINGSERVICE.methods_by_name['SetDefaultPaymentMethod']._serialized_options = b'\202\323\344\223\002I\032D/api/billing/v1/organization/{organization_id}/default-paymentmethod:\001*'
  _BILLINGSERVICE.methods_by_name['GetBillingConfig']._options = None
  _BILLINGSERVICE.methods_by_name['GetBillingConfig']._serialized_options = b'\202\323\344\223\002*\022(/api/billing/v1/organization/{id}/config'
  _BILLINGSERVICE.methods_by_name['SetBillingConfig']._options = None
  _BILLINGSERVICE.methods_by_name['SetBillingConfig']._serialized_options = b'\202\323\344\223\002:\0325/api/billing/v1/organization/{organization_id}/config:\001*'
  _BILLINGSERVICE.methods_by_name['GetAvailableCredits']._options = None
  _BILLINGSERVICE.methods_by_name['GetAvailableCredits']._serialized_options = b'\202\323\344\223\0028\0226/api/billing/v1/organization/{organization_id}/credits'
  _INVOICE._serialized_start=171
  _INVOICE._serialized_end=1748
  _INVOICE_ITEM._serialized_start=952
  _INVOICE_ITEM._serialized_end=1038
  _INVOICE_STATUS._serialized_start=1041
  _INVOICE_STATUS._serialized_end=1351
  _INVOICE_PAYMENT._serialized_start=1354
  _INVOICE_PAYMENT._serialized_end=1748
  _INVOICELIST._serialized_start=1750
  _INVOICELIST._serialized_end=1814
  _LISTINVOICESREQUEST._serialized_start=1817
  _LISTINVOICESREQUEST._serialized_end=2032
  _GETPRELIMINARYINVOICEREQUEST._serialized_start=2034
  _GETPRELIMINARYINVOICEREQUEST._serialized_end=2089
  _PAYMENTPROVIDER._serialized_start=2091
  _PAYMENTPROVIDER._serialized_end=2169
  _PAYMENTPROVIDERLIST._serialized_start=2171
  _PAYMENTPROVIDERLIST._serialized_end=2251
  _PREPAREPAYMENTMETHODREQUEST._serialized_start=2253
  _PREPAREPAYMENTMETHODREQUEST._serialized_end=2349
  _PREPAREDPAYMENTMETHOD._serialized_start=2352
  _PREPAREDPAYMENTMETHOD._serialized_end=2496
  _CREATEPAYMENTMETHODREQUEST._serialized_start=2499
  _CREATEPAYMENTMETHODREQUEST._serialized_end=2649
  _LISTPAYMENTPROVIDERSREQUEST._serialized_start=2652
  _LISTPAYMENTPROVIDERSREQUEST._serialized_end=2788
  _PAYMENTMETHOD._serialized_start=2791
  _PAYMENTMETHOD._serialized_end=3283
  _PAYMENTMETHOD_CREDITCARDINFO._serialized_start=3227
  _PAYMENTMETHOD_CREDITCARDINFO._serialized_end=3283
  _PAYMENTMETHODLIST._serialized_start=3285
  _PAYMENTMETHODLIST._serialized_end=3361
  _LISTPAYMENTMETHODSREQUEST._serialized_start=3363
  _LISTPAYMENTMETHODSREQUEST._serialized_end=3471
  _SETDEFAULTPAYMENTMETHODREQUEST._serialized_start=3473
  _SETDEFAULTPAYMENTMETHODREQUEST._serialized_end=3557
  _ADDRESS._serialized_start=3559
  _ADDRESS._serialized_end=3653
  _ORGANIZATIONBILLINGFLAGS._serialized_start=3655
  _ORGANIZATIONBILLINGFLAGS._serialized_end=3764
  _BILLINGCONFIG._serialized_start=3767
  _BILLINGCONFIG._serialized_end=3931
  _SETBILLINGCONFIGREQUEST._serialized_start=3933
  _SETBILLINGCONFIGREQUEST._serialized_end=4041
  _PDFDOCUMENT._serialized_start=4043
  _PDFDOCUMENT._serialized_end=4091
  _GETAVAILABLECREDITSREQUEST._serialized_start=4093
  _GETAVAILABLECREDITSREQUEST._serialized_end=4146
  _AVAILABLECREDITS._serialized_start=4149
  _AVAILABLECREDITS._serialized_end=4311
  _AVAILABLECREDITS_CREDITCURRENCYAMOUNT._serialized_start=4252
  _AVAILABLECREDITS_CREDITCURRENCYAMOUNT._serialized_end=4311
  _BILLINGSERVICE._serialized_start=4314
  _BILLINGSERVICE._serialized_end=7480
# @@protoc_insertion_point(module_scope)
