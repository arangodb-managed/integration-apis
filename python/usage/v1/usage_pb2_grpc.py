# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from usage.v1 import usage_pb2 as usage_dot_v1_dot_usage__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in usage/v1/usage_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UsageServiceStub(object):
    """UsageService is the API used to fetch usage tracking information.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.usage.v1.UsageService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.ListUsageItems = channel.unary_unary(
                '/arangodb.cloud.usage.v1.UsageService/ListUsageItems',
                request_serializer=usage_dot_v1_dot_usage__pb2.ListUsageItemsRequest.SerializeToString,
                response_deserializer=usage_dot_v1_dot_usage__pb2.UsageItemList.FromString,
                _registered_method=True)


class UsageServiceServicer(object):
    """UsageService is the API used to fetch usage tracking information.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsageItems(self, request, context):
        """Fetch all UsageItem resources in the organization identified by the given
        organization ID that match the given criteria.
        Required permissions:
        - usage.usageitem.list on the organization identified by the given organization ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'ListUsageItems': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsageItems,
                    request_deserializer=usage_dot_v1_dot_usage__pb2.ListUsageItemsRequest.FromString,
                    response_serializer=usage_dot_v1_dot_usage__pb2.UsageItemList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.usage.v1.UsageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.usage.v1.UsageService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UsageService(object):
    """UsageService is the API used to fetch usage tracking information.
    """

    @staticmethod
    def GetAPIVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/arangodb.cloud.usage.v1.UsageService/GetAPIVersion',
            common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            common_dot_v1_dot_common__pb2.Version.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListUsageItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/arangodb.cloud.usage.v1.UsageService/ListUsageItems',
            usage_dot_v1_dot_usage__pb2.ListUsageItemsRequest.SerializeToString,
            usage_dot_v1_dot_usage__pb2.UsageItemList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
