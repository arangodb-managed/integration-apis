# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from crypto.v1 import crypto_pb2 as crypto_dot_v1_dot_crypto__pb2

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
        + f' but the generated code in crypto/v1/crypto_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CryptoServiceStub(object):
    """CryptoService is the API used to configure various crypto objects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.ListCACertificates = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/ListCACertificates',
                request_serializer=common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
                response_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificateList.FromString,
                _registered_method=True)
        self.ListCACertificatesWithFilter = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/ListCACertificatesWithFilter',
                request_serializer=crypto_dot_v1_dot_crypto__pb2.ListCACertificatesRequest.SerializeToString,
                response_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificateList.FromString,
                _registered_method=True)
        self.GetCACertificate = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/GetCACertificate',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
                _registered_method=True)
        self.GetCACertificateInstructions = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/GetCACertificateInstructions',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificateInstructions.FromString,
                _registered_method=True)
        self.CreateCACertificate = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/CreateCACertificate',
                request_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
                response_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
                _registered_method=True)
        self.CloneCACertificate = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/CloneCACertificate',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
                _registered_method=True)
        self.UpdateCACertificate = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/UpdateCACertificate',
                request_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
                response_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
                _registered_method=True)
        self.DeleteCACertificate = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/DeleteCACertificate',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)
        self.SetDefaultCACertificate = channel.unary_unary(
                '/arangodb.cloud.crypto.v1.CryptoService/SetDefaultCACertificate',
                request_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)


class CryptoServiceServicer(object):
    """CryptoService is the API used to configure various crypto objects.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCACertificates(self, request, context):
        """Fetch all CA certificates in the project identified by the given context ID.
        Required permissions:
        - crypto.cacertificate.list on the project identified by the given context ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCACertificatesWithFilter(self, request, context):
        """Fetch all CA certificates in the project identified by the given project ID
        that match the given filter.
        Required permissions:
        - crypto.cacertificate.list on the project identified by the given context ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCACertificate(self, request, context):
        """Fetch a CA certificate by its id.
        Required permissions:
        - crypto.cacertificate.get on the CA certificate identified by the given ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCACertificateInstructions(self, request, context):
        """Fetch instructions for installing & unistalling a CA certificate identified by its id
        on various platforms.
        Required permissions:
        - crypto.cacertificate.get on the CA certificate identified by the given ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCACertificate(self, request, context):
        """Create a new CA certificate
        Required permissions:
        - crypto.cacertificate.create on the project that owns the CA certificate
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloneCACertificate(self, request, context):
        """Clone a CA certificate identified by given id.
        Required permissions:
        - crypto.cacertificate.clone on the project that owns the CA certificate identified by the given ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCACertificate(self, request, context):
        """Update a CA certificate
        Required permissions:
        - crypto.cacertificate.update on the CA certificate
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCACertificate(self, request, context):
        """Delete a CA certificate
        Note that CA certificate are initially only marked for deleted.
        Once all the resources that depend on it are removed the CA certificate itself is deleted
        and cannot be restored.
        Required permissions:
        - crypto.cacertificate.delete on the CA certificate
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDefaultCACertificate(self, request, context):
        """Mark the given CA certificate as default for its containing project.
        Required permissions:
        - crypto.cacertificate.set-default on the project that owns the certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CryptoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'ListCACertificates': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCACertificates,
                    request_deserializer=common_dot_v1_dot_common__pb2.ListOptions.FromString,
                    response_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificateList.SerializeToString,
            ),
            'ListCACertificatesWithFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCACertificatesWithFilter,
                    request_deserializer=crypto_dot_v1_dot_crypto__pb2.ListCACertificatesRequest.FromString,
                    response_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificateList.SerializeToString,
            ),
            'GetCACertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCACertificate,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
            ),
            'GetCACertificateInstructions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCACertificateInstructions,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificateInstructions.SerializeToString,
            ),
            'CreateCACertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCACertificate,
                    request_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
                    response_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
            ),
            'CloneCACertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.CloneCACertificate,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
            ),
            'UpdateCACertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCACertificate,
                    request_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
                    response_serializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
            ),
            'DeleteCACertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCACertificate,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'SetDefaultCACertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDefaultCACertificate,
                    request_deserializer=crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.crypto.v1.CryptoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.crypto.v1.CryptoService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CryptoService(object):
    """CryptoService is the API used to configure various crypto objects.
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
            '/arangodb.cloud.crypto.v1.CryptoService/GetAPIVersion',
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
    def ListCACertificates(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/ListCACertificates',
            common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
            crypto_dot_v1_dot_crypto__pb2.CACertificateList.FromString,
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
    def ListCACertificatesWithFilter(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/ListCACertificatesWithFilter',
            crypto_dot_v1_dot_crypto__pb2.ListCACertificatesRequest.SerializeToString,
            crypto_dot_v1_dot_crypto__pb2.CACertificateList.FromString,
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
    def GetCACertificate(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/GetCACertificate',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
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
    def GetCACertificateInstructions(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/GetCACertificateInstructions',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            crypto_dot_v1_dot_crypto__pb2.CACertificateInstructions.FromString,
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
    def CreateCACertificate(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/CreateCACertificate',
            crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
            crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
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
    def CloneCACertificate(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/CloneCACertificate',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
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
    def UpdateCACertificate(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/UpdateCACertificate',
            crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
            crypto_dot_v1_dot_crypto__pb2.CACertificate.FromString,
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
    def DeleteCACertificate(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/DeleteCACertificate',
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

    @staticmethod
    def SetDefaultCACertificate(request,
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
            '/arangodb.cloud.crypto.v1.CryptoService/SetDefaultCACertificate',
            crypto_dot_v1_dot_crypto__pb2.CACertificate.SerializeToString,
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
