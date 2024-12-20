# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from monitoring.v1 import monitoring_pb2 as monitoring_dot_v1_dot_monitoring__pb2

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
        + f' but the generated code in monitoring/v1/monitoring_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MonitoringServiceStub(object):
    """MonitoringService is the API used to monitor deployments.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.monitoring.v1.MonitoringService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.GetDeploymentLogs = channel.unary_stream(
                '/arangodb.cloud.monitoring.v1.MonitoringService/GetDeploymentLogs',
                request_serializer=monitoring_dot_v1_dot_monitoring__pb2.GetDeploymentLogsRequest.SerializeToString,
                response_deserializer=monitoring_dot_v1_dot_monitoring__pb2.DeploymentLogsChunk.FromString,
                _registered_method=True)
        self.GetDeploymentUsageMetrics = channel.unary_unary(
                '/arangodb.cloud.monitoring.v1.MonitoringService/GetDeploymentUsageMetrics',
                request_serializer=monitoring_dot_v1_dot_monitoring__pb2.GetDeploymentMetricsRequest.SerializeToString,
                response_deserializer=monitoring_dot_v1_dot_monitoring__pb2.DeploymentMetrics.FromString,
                _registered_method=True)


class MonitoringServiceServicer(object):
    """MonitoringService is the API used to monitor deployments.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeploymentLogs(self, request, context):
        """Fetch all logs of the deployment that matches the given request.
        Required permissions:
        - monitoring.logs.get on the deployment identified by the given deployment ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeploymentUsageMetrics(self, request, context):
        """Get the usage metrics for the deployment based on the given request.
        Note: Only at most 1 week worth of data may be requested.
        Required permissions:
        - monitoring.metrics.get on the deployment identified by the given deployment ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitoringServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'GetDeploymentLogs': grpc.unary_stream_rpc_method_handler(
                    servicer.GetDeploymentLogs,
                    request_deserializer=monitoring_dot_v1_dot_monitoring__pb2.GetDeploymentLogsRequest.FromString,
                    response_serializer=monitoring_dot_v1_dot_monitoring__pb2.DeploymentLogsChunk.SerializeToString,
            ),
            'GetDeploymentUsageMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeploymentUsageMetrics,
                    request_deserializer=monitoring_dot_v1_dot_monitoring__pb2.GetDeploymentMetricsRequest.FromString,
                    response_serializer=monitoring_dot_v1_dot_monitoring__pb2.DeploymentMetrics.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.monitoring.v1.MonitoringService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.monitoring.v1.MonitoringService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MonitoringService(object):
    """MonitoringService is the API used to monitor deployments.
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
            '/arangodb.cloud.monitoring.v1.MonitoringService/GetAPIVersion',
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
    def GetDeploymentLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/arangodb.cloud.monitoring.v1.MonitoringService/GetDeploymentLogs',
            monitoring_dot_v1_dot_monitoring__pb2.GetDeploymentLogsRequest.SerializeToString,
            monitoring_dot_v1_dot_monitoring__pb2.DeploymentLogsChunk.FromString,
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
    def GetDeploymentUsageMetrics(request,
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
            '/arangodb.cloud.monitoring.v1.MonitoringService/GetDeploymentUsageMetrics',
            monitoring_dot_v1_dot_monitoring__pb2.GetDeploymentMetricsRequest.SerializeToString,
            monitoring_dot_v1_dot_monitoring__pb2.DeploymentMetrics.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
