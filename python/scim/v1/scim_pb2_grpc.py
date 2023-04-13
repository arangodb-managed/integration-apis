# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from scim.v1 import scim_pb2 as scim_dot_v1_dot_scim__pb2


class SCIMServiceStub(object):
    """Note: that this API slightly differs from other APIs, because it need to follow the SCIM conversions.
    Furthermore is on all those API calls (except GetAPIVersion), the authenticated user can be provided via a username/password header, 
    which need to contain an APIKey / Secret, which need to resolve to a single organization.

    SCIMService is the API used to expose the SCIM Provisioning API for SAML based SSO.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.resourcemanager.v1.SCIMService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                )
        self.ListUsers = channel.unary_unary(
                '/arangodb.cloud.resourcemanager.v1.SCIMService/ListUsers',
                request_serializer=scim_dot_v1_dot_scim__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=scim_dot_v1_dot_scim__pb2.ListUserResponse.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/arangodb.cloud.resourcemanager.v1.SCIMService/GetUser',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=scim_dot_v1_dot_scim__pb2.User.FromString,
                )
        self.AddUser = channel.unary_unary(
                '/arangodb.cloud.resourcemanager.v1.SCIMService/AddUser',
                request_serializer=scim_dot_v1_dot_scim__pb2.User.SerializeToString,
                response_deserializer=scim_dot_v1_dot_scim__pb2.User.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/arangodb.cloud.resourcemanager.v1.SCIMService/UpdateUser',
                request_serializer=scim_dot_v1_dot_scim__pb2.User.SerializeToString,
                response_deserializer=scim_dot_v1_dot_scim__pb2.User.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/arangodb.cloud.resourcemanager.v1.SCIMService/DeleteUser',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                )


class SCIMServiceServicer(object):
    """Note: that this API slightly differs from other APIs, because it need to follow the SCIM conversions.
    Furthermore is on all those API calls (except GetAPIVersion), the authenticated user can be provided via a username/password header, 
    which need to contain an APIKey / Secret, which need to resolve to a single organization.

    SCIMService is the API used to expose the SCIM Provisioning API for SAML based SSO.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None (authenticated only)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """List the users as per SCIM API requirements
        For an organization identifier inferred via API Key
        Required permissions:
        - scim.user.list on the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Get the organization member information based on user identifier as per SCIM API requirements
        Required permissions:
        - scim.user.get on the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """Invite the user to an organization
        that is inferred from API key
        Required permissions:
        - scim.user.add on the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Update the user information
        Required permissions:
        - scim.user.update on the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Delete the user from an organization
        Required permissions:
        - scim.user.delete on the organization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SCIMServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'ListUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=scim_dot_v1_dot_scim__pb2.ListUsersRequest.FromString,
                    response_serializer=scim_dot_v1_dot_scim__pb2.ListUserResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=scim_dot_v1_dot_scim__pb2.User.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=scim_dot_v1_dot_scim__pb2.User.FromString,
                    response_serializer=scim_dot_v1_dot_scim__pb2.User.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=scim_dot_v1_dot_scim__pb2.User.FromString,
                    response_serializer=scim_dot_v1_dot_scim__pb2.User.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.resourcemanager.v1.SCIMService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SCIMService(object):
    """Note: that this API slightly differs from other APIs, because it need to follow the SCIM conversions.
    Furthermore is on all those API calls (except GetAPIVersion), the authenticated user can be provided via a username/password header, 
    which need to contain an APIKey / Secret, which need to resolve to a single organization.

    SCIMService is the API used to expose the SCIM Provisioning API for SAML based SSO.
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
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.resourcemanager.v1.SCIMService/GetAPIVersion',
            common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            common_dot_v1_dot_common__pb2.Version.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.resourcemanager.v1.SCIMService/ListUsers',
            scim_dot_v1_dot_scim__pb2.ListUsersRequest.SerializeToString,
            scim_dot_v1_dot_scim__pb2.ListUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.resourcemanager.v1.SCIMService/GetUser',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            scim_dot_v1_dot_scim__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.resourcemanager.v1.SCIMService/AddUser',
            scim_dot_v1_dot_scim__pb2.User.SerializeToString,
            scim_dot_v1_dot_scim__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.resourcemanager.v1.SCIMService/UpdateUser',
            scim_dot_v1_dot_scim__pb2.User.SerializeToString,
            scim_dot_v1_dot_scim__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.resourcemanager.v1.SCIMService/DeleteUser',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            common_dot_v1_dot_common__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
