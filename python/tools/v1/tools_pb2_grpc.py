# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from tools.v1 import tools_pb2 as tools_dot_v1_dot_tools__pb2

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
        + f' but the generated code in tools/v1/tools_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ToolsServiceStub(object):
    """ToolsService is the API used by the compatibility check for an ArangoDB Tool.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.tools.v1.ToolsService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.GetLatestVersion = channel.unary_unary(
                '/arangodb.cloud.tools.v1.ToolsService/GetLatestVersion',
                request_serializer=tools_dot_v1_dot_tools__pb2.GetLatestVersionRequest.SerializeToString,
                response_deserializer=tools_dot_v1_dot_tools__pb2.ToolsVersion.FromString,
                _registered_method=True)


class ToolsServiceServicer(object):
    """ToolsService is the API used by the compatibility check for an ArangoDB Tool.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLatestVersion(self, request, context):
        """Get the latest version for a tool.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ToolsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'GetLatestVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLatestVersion,
                    request_deserializer=tools_dot_v1_dot_tools__pb2.GetLatestVersionRequest.FromString,
                    response_serializer=tools_dot_v1_dot_tools__pb2.ToolsVersion.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.tools.v1.ToolsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.tools.v1.ToolsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ToolsService(object):
    """ToolsService is the API used by the compatibility check for an ArangoDB Tool.
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
            '/arangodb.cloud.tools.v1.ToolsService/GetAPIVersion',
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
    def GetLatestVersion(request,
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
            '/arangodb.cloud.tools.v1.ToolsService/GetLatestVersion',
            tools_dot_v1_dot_tools__pb2.GetLatestVersionRequest.SerializeToString,
            tools_dot_v1_dot_tools__pb2.ToolsVersion.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
