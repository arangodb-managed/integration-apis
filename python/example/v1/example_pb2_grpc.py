# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from example.v1 import example_pb2 as example_dot_v1_dot_example__pb2

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
        + f' but the generated code in example/v1/example_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ExampleDatasetServiceStub(object):
    """ExampleDatasetService is the API used to query for example datasets.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.example.v1.ExampleDatasetService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.ListExampleDatasets = channel.unary_unary(
                '/arangodb.cloud.example.v1.ExampleDatasetService/ListExampleDatasets',
                request_serializer=example_dot_v1_dot_example__pb2.ListExampleDatasetsRequest.SerializeToString,
                response_deserializer=example_dot_v1_dot_example__pb2.ExampleDatasetList.FromString,
                _registered_method=True)
        self.GetExampleDataset = channel.unary_unary(
                '/arangodb.cloud.example.v1.ExampleDatasetService/GetExampleDataset',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=example_dot_v1_dot_example__pb2.ExampleDataset.FromString,
                _registered_method=True)
        self.ListExampleDatasetInstallations = channel.unary_unary(
                '/arangodb.cloud.example.v1.ExampleDatasetService/ListExampleDatasetInstallations',
                request_serializer=example_dot_v1_dot_example__pb2.ListExampleDatasetInstallationsRequest.SerializeToString,
                response_deserializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallationList.FromString,
                _registered_method=True)
        self.GetExampleDatasetInstallation = channel.unary_unary(
                '/arangodb.cloud.example.v1.ExampleDatasetService/GetExampleDatasetInstallation',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.FromString,
                _registered_method=True)
        self.CreateExampleDatasetInstallation = channel.unary_unary(
                '/arangodb.cloud.example.v1.ExampleDatasetService/CreateExampleDatasetInstallation',
                request_serializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.SerializeToString,
                response_deserializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.FromString,
                _registered_method=True)
        self.UpdateExampleDatasetInstallation = channel.unary_unary(
                '/arangodb.cloud.example.v1.ExampleDatasetService/UpdateExampleDatasetInstallation',
                request_serializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.SerializeToString,
                response_deserializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.FromString,
                _registered_method=True)
        self.DeleteExampleDatasetInstallation = channel.unary_unary(
                '/arangodb.cloud.example.v1.ExampleDatasetService/DeleteExampleDatasetInstallation',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)


class ExampleDatasetServiceServicer(object):
    """ExampleDatasetService is the API used to query for example datasets.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExampleDatasets(self, request, context):
        """Fetch all example datasets.
        Required permissions:
        - None: Caller must be authenticated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleDataset(self, request, context):
        """Fetch an example dataset identified by the given ID.
        Required permissions:
        - None: Caller must be authenticated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExampleDatasetInstallations(self, request, context):
        """Fetch all installations for a specific deployment.
        Required permissions:
        - example.exampledatasetinstallation.list on the deployment that owns the installation and is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExampleDatasetInstallation(self, request, context):
        """Fetch an installations identified by the given ID.
        Required permissions:
        - example.exampledatasetinstallation.get on the installation identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateExampleDatasetInstallation(self, request, context):
        """Create a new example installation. This represents a request made by the user to create an installation
        for a deployment given a specified example dataset.
        Required permissions:
        -  example.exampledatasetinstallation.create on the deployment that the installation is for and is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateExampleDatasetInstallation(self, request, context):
        """Update an installation.
        Required permissions:
        -  example.exampledatasetinstallation.update on the installation identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteExampleDatasetInstallation(self, request, context):
        """Delete an installation identified by the given ID.
        Required permissions:
        -  example.exampledatasetinstallation.delete on the installation identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExampleDatasetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'ListExampleDatasets': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExampleDatasets,
                    request_deserializer=example_dot_v1_dot_example__pb2.ListExampleDatasetsRequest.FromString,
                    response_serializer=example_dot_v1_dot_example__pb2.ExampleDatasetList.SerializeToString,
            ),
            'GetExampleDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleDataset,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=example_dot_v1_dot_example__pb2.ExampleDataset.SerializeToString,
            ),
            'ListExampleDatasetInstallations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExampleDatasetInstallations,
                    request_deserializer=example_dot_v1_dot_example__pb2.ListExampleDatasetInstallationsRequest.FromString,
                    response_serializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallationList.SerializeToString,
            ),
            'GetExampleDatasetInstallation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExampleDatasetInstallation,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.SerializeToString,
            ),
            'CreateExampleDatasetInstallation': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExampleDatasetInstallation,
                    request_deserializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.FromString,
                    response_serializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.SerializeToString,
            ),
            'UpdateExampleDatasetInstallation': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateExampleDatasetInstallation,
                    request_deserializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.FromString,
                    response_serializer=example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.SerializeToString,
            ),
            'DeleteExampleDatasetInstallation': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteExampleDatasetInstallation,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.example.v1.ExampleDatasetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.example.v1.ExampleDatasetService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ExampleDatasetService(object):
    """ExampleDatasetService is the API used to query for example datasets.
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
            '/arangodb.cloud.example.v1.ExampleDatasetService/GetAPIVersion',
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
    def ListExampleDatasets(request,
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
            '/arangodb.cloud.example.v1.ExampleDatasetService/ListExampleDatasets',
            example_dot_v1_dot_example__pb2.ListExampleDatasetsRequest.SerializeToString,
            example_dot_v1_dot_example__pb2.ExampleDatasetList.FromString,
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
    def GetExampleDataset(request,
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
            '/arangodb.cloud.example.v1.ExampleDatasetService/GetExampleDataset',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            example_dot_v1_dot_example__pb2.ExampleDataset.FromString,
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
    def ListExampleDatasetInstallations(request,
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
            '/arangodb.cloud.example.v1.ExampleDatasetService/ListExampleDatasetInstallations',
            example_dot_v1_dot_example__pb2.ListExampleDatasetInstallationsRequest.SerializeToString,
            example_dot_v1_dot_example__pb2.ExampleDatasetInstallationList.FromString,
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
    def GetExampleDatasetInstallation(request,
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
            '/arangodb.cloud.example.v1.ExampleDatasetService/GetExampleDatasetInstallation',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.FromString,
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
    def CreateExampleDatasetInstallation(request,
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
            '/arangodb.cloud.example.v1.ExampleDatasetService/CreateExampleDatasetInstallation',
            example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.SerializeToString,
            example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.FromString,
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
    def UpdateExampleDatasetInstallation(request,
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
            '/arangodb.cloud.example.v1.ExampleDatasetService/UpdateExampleDatasetInstallation',
            example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.SerializeToString,
            example_dot_v1_dot_example__pb2.ExampleDatasetInstallation.FromString,
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
    def DeleteExampleDatasetInstallation(request,
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
            '/arangodb.cloud.example.v1.ExampleDatasetService/DeleteExampleDatasetInstallation',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            common_dot_v1_dot_common__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
