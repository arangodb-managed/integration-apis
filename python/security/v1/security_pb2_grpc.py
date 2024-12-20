# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from security.v1 import security_pb2 as security_dot_v1_dot_security__pb2

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
        + f' but the generated code in security/v1/security_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SecurityServiceStub(object):
    """SecurityService is the API used to access security entities.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.ListIPAllowlists = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/ListIPAllowlists',
                request_serializer=common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
                response_deserializer=security_dot_v1_dot_security__pb2.IPAllowlistList.FromString,
                _registered_method=True)
        self.GetIPAllowlist = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/GetIPAllowlist',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=security_dot_v1_dot_security__pb2.IPAllowlist.FromString,
                _registered_method=True)
        self.CreateIPAllowlist = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/CreateIPAllowlist',
                request_serializer=security_dot_v1_dot_security__pb2.IPAllowlist.SerializeToString,
                response_deserializer=security_dot_v1_dot_security__pb2.IPAllowlist.FromString,
                _registered_method=True)
        self.UpdateIPAllowlist = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/UpdateIPAllowlist',
                request_serializer=security_dot_v1_dot_security__pb2.IPAllowlist.SerializeToString,
                response_deserializer=security_dot_v1_dot_security__pb2.IPAllowlist.FromString,
                _registered_method=True)
        self.DeleteIPAllowlist = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/DeleteIPAllowlist',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)
        self.ListIAMProviders = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/ListIAMProviders',
                request_serializer=common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
                response_deserializer=security_dot_v1_dot_security__pb2.IAMProviderList.FromString,
                _registered_method=True)
        self.GetIAMProvider = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/GetIAMProvider',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=security_dot_v1_dot_security__pb2.IAMProvider.FromString,
                _registered_method=True)
        self.CreateIAMProvider = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/CreateIAMProvider',
                request_serializer=security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
                response_deserializer=security_dot_v1_dot_security__pb2.IAMProvider.FromString,
                _registered_method=True)
        self.UpdateIAMProvider = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/UpdateIAMProvider',
                request_serializer=security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
                response_deserializer=security_dot_v1_dot_security__pb2.IAMProvider.FromString,
                _registered_method=True)
        self.DeleteIAMProvider = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/DeleteIAMProvider',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)
        self.SetDefaultIAMProvider = channel.unary_unary(
                '/arangodb.cloud.security.v1.SecurityService/SetDefaultIAMProvider',
                request_serializer=security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)


class SecurityServiceServicer(object):
    """SecurityService is the API used to access security entities.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListIPAllowlists(self, request, context):
        """Fetch all IP allowlists that belong to the project identified by the given
        context ID.
        Required permissions:
        - security.ipallowlist.list on the project identified by the given context ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIPAllowlist(self, request, context):
        """Fetch an IP allowlist by its id.
        Required permissions:
        - security.ipallowlist.get on the IP allowlist
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateIPAllowlist(self, request, context):
        """Create a new IP allowlist
        Required permissions:
        - security.ipallowlist.create on the project that owns the IP allowlist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateIPAllowlist(self, request, context):
        """Update an IP allowlist
        Required permissions:
        - security.ipallowlist.update on the IP allowlist
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIPAllowlist(self, request, context):
        """Delete an IP allowlist.
        Note that IP allowlists are initially only marked for deletion.
        Once all their dependent deployments are removed, the allowlist is removed.
        Required permissions:
        - security.ipallowlist.delete on the IP allowlist
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListIAMProviders(self, request, context):
        """Fetch all IAM providers that belong to the project identified by the given
        context ID.
        Required permissions:
        - security.iamprovider.list on the project identified by the given context ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIAMProvider(self, request, context):
        """Fetch an IAM provider by its id.
        Required permissions:
        - security.iamprovider.get on the IAM provider
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateIAMProvider(self, request, context):
        """Create a new IAM provider
        Required permissions:
        - security.iamprovider.create on the project that owns the IAM provider.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateIAMProvider(self, request, context):
        """Update an IAM provider
        Required permissions:
        - security.iamprovider.update on the IAM provider
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIAMProvider(self, request, context):
        """Delete an IAM provider.
        Note that IAM providers are initially only marked for deletion.
        Once all their dependent deployments are removed, the provider is removed.
        Required permissions:
        - security.iamprovider.delete on the IP whitelist
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDefaultIAMProvider(self, request, context):
        """Mark the given IAM provider as default for its containing project.
        Required permissions:
        - security.iamprovider.set-default on the project that owns the provider.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecurityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'ListIPAllowlists': grpc.unary_unary_rpc_method_handler(
                    servicer.ListIPAllowlists,
                    request_deserializer=common_dot_v1_dot_common__pb2.ListOptions.FromString,
                    response_serializer=security_dot_v1_dot_security__pb2.IPAllowlistList.SerializeToString,
            ),
            'GetIPAllowlist': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIPAllowlist,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=security_dot_v1_dot_security__pb2.IPAllowlist.SerializeToString,
            ),
            'CreateIPAllowlist': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateIPAllowlist,
                    request_deserializer=security_dot_v1_dot_security__pb2.IPAllowlist.FromString,
                    response_serializer=security_dot_v1_dot_security__pb2.IPAllowlist.SerializeToString,
            ),
            'UpdateIPAllowlist': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateIPAllowlist,
                    request_deserializer=security_dot_v1_dot_security__pb2.IPAllowlist.FromString,
                    response_serializer=security_dot_v1_dot_security__pb2.IPAllowlist.SerializeToString,
            ),
            'DeleteIPAllowlist': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteIPAllowlist,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'ListIAMProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.ListIAMProviders,
                    request_deserializer=common_dot_v1_dot_common__pb2.ListOptions.FromString,
                    response_serializer=security_dot_v1_dot_security__pb2.IAMProviderList.SerializeToString,
            ),
            'GetIAMProvider': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIAMProvider,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
            ),
            'CreateIAMProvider': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateIAMProvider,
                    request_deserializer=security_dot_v1_dot_security__pb2.IAMProvider.FromString,
                    response_serializer=security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
            ),
            'UpdateIAMProvider': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateIAMProvider,
                    request_deserializer=security_dot_v1_dot_security__pb2.IAMProvider.FromString,
                    response_serializer=security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
            ),
            'DeleteIAMProvider': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteIAMProvider,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'SetDefaultIAMProvider': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDefaultIAMProvider,
                    request_deserializer=security_dot_v1_dot_security__pb2.IAMProvider.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.security.v1.SecurityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.security.v1.SecurityService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SecurityService(object):
    """SecurityService is the API used to access security entities.
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
            '/arangodb.cloud.security.v1.SecurityService/GetAPIVersion',
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
    def ListIPAllowlists(request,
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
            '/arangodb.cloud.security.v1.SecurityService/ListIPAllowlists',
            common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
            security_dot_v1_dot_security__pb2.IPAllowlistList.FromString,
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
    def GetIPAllowlist(request,
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
            '/arangodb.cloud.security.v1.SecurityService/GetIPAllowlist',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            security_dot_v1_dot_security__pb2.IPAllowlist.FromString,
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
    def CreateIPAllowlist(request,
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
            '/arangodb.cloud.security.v1.SecurityService/CreateIPAllowlist',
            security_dot_v1_dot_security__pb2.IPAllowlist.SerializeToString,
            security_dot_v1_dot_security__pb2.IPAllowlist.FromString,
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
    def UpdateIPAllowlist(request,
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
            '/arangodb.cloud.security.v1.SecurityService/UpdateIPAllowlist',
            security_dot_v1_dot_security__pb2.IPAllowlist.SerializeToString,
            security_dot_v1_dot_security__pb2.IPAllowlist.FromString,
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
    def DeleteIPAllowlist(request,
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
            '/arangodb.cloud.security.v1.SecurityService/DeleteIPAllowlist',
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
    def ListIAMProviders(request,
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
            '/arangodb.cloud.security.v1.SecurityService/ListIAMProviders',
            common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
            security_dot_v1_dot_security__pb2.IAMProviderList.FromString,
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
    def GetIAMProvider(request,
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
            '/arangodb.cloud.security.v1.SecurityService/GetIAMProvider',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            security_dot_v1_dot_security__pb2.IAMProvider.FromString,
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
    def CreateIAMProvider(request,
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
            '/arangodb.cloud.security.v1.SecurityService/CreateIAMProvider',
            security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
            security_dot_v1_dot_security__pb2.IAMProvider.FromString,
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
    def UpdateIAMProvider(request,
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
            '/arangodb.cloud.security.v1.SecurityService/UpdateIAMProvider',
            security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
            security_dot_v1_dot_security__pb2.IAMProvider.FromString,
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
    def DeleteIAMProvider(request,
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
            '/arangodb.cloud.security.v1.SecurityService/DeleteIAMProvider',
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
    def SetDefaultIAMProvider(request,
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
            '/arangodb.cloud.security.v1.SecurityService/SetDefaultIAMProvider',
            security_dot_v1_dot_security__pb2.IAMProvider.SerializeToString,
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
