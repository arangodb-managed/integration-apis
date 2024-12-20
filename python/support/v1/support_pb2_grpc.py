# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from support.v1 import support_pb2 as support_dot_v1_dot_support__pb2

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
        + f' but the generated code in support/v1/support_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SupportServiceStub(object):
    """SupportService is the API used to query for support.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.support.v1.SupportService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.ListPlans = channel.unary_unary(
                '/arangodb.cloud.support.v1.SupportService/ListPlans',
                request_serializer=support_dot_v1_dot_support__pb2.ListPlansRequest.SerializeToString,
                response_deserializer=support_dot_v1_dot_support__pb2.PlanList.FromString,
                _registered_method=True)
        self.GetPlan = channel.unary_unary(
                '/arangodb.cloud.support.v1.SupportService/GetPlan',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=support_dot_v1_dot_support__pb2.Plan.FromString,
                _registered_method=True)
        self.ListFaqGroups = channel.unary_unary(
                '/arangodb.cloud.support.v1.SupportService/ListFaqGroups',
                request_serializer=common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
                response_deserializer=support_dot_v1_dot_support__pb2.FaqGroupList.FromString,
                _registered_method=True)
        self.ListFaqGroupEntries = channel.unary_unary(
                '/arangodb.cloud.support.v1.SupportService/ListFaqGroupEntries',
                request_serializer=common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
                response_deserializer=support_dot_v1_dot_support__pb2.FaqGroupEntryList.FromString,
                _registered_method=True)
        self.CreateSupportRequest = channel.unary_unary(
                '/arangodb.cloud.support.v1.SupportService/CreateSupportRequest',
                request_serializer=support_dot_v1_dot_support__pb2.SupportRequest.SerializeToString,
                response_deserializer=support_dot_v1_dot_support__pb2.SupportRequest.FromString,
                _registered_method=True)


class SupportServiceServicer(object):
    """SupportService is the API used to query for support.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPlans(self, request, context):
        """Fetch all support plans that are supported by the ArangoDB cloud.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlan(self, request, context):
        """Fetch a support plan by its id.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFaqGroups(self, request, context):
        """Fetch all FAQ groups.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFaqGroupEntries(self, request, context):
        """Fetch all FAQ group entries of the FAQ group identified by the given context ID.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSupportRequest(self, request, context):
        """Submit a support request.
        Required permissions:
        - resourcemanager.organization.get (if organization id is set)
        - resourcemanager.project.get (if project id is set)
        - data.deployment.get (if deployment id is set)
        - None (if no ids are set)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SupportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'ListPlans': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPlans,
                    request_deserializer=support_dot_v1_dot_support__pb2.ListPlansRequest.FromString,
                    response_serializer=support_dot_v1_dot_support__pb2.PlanList.SerializeToString,
            ),
            'GetPlan': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlan,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=support_dot_v1_dot_support__pb2.Plan.SerializeToString,
            ),
            'ListFaqGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFaqGroups,
                    request_deserializer=common_dot_v1_dot_common__pb2.ListOptions.FromString,
                    response_serializer=support_dot_v1_dot_support__pb2.FaqGroupList.SerializeToString,
            ),
            'ListFaqGroupEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFaqGroupEntries,
                    request_deserializer=common_dot_v1_dot_common__pb2.ListOptions.FromString,
                    response_serializer=support_dot_v1_dot_support__pb2.FaqGroupEntryList.SerializeToString,
            ),
            'CreateSupportRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSupportRequest,
                    request_deserializer=support_dot_v1_dot_support__pb2.SupportRequest.FromString,
                    response_serializer=support_dot_v1_dot_support__pb2.SupportRequest.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.support.v1.SupportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.support.v1.SupportService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SupportService(object):
    """SupportService is the API used to query for support.
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
            '/arangodb.cloud.support.v1.SupportService/GetAPIVersion',
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
    def ListPlans(request,
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
            '/arangodb.cloud.support.v1.SupportService/ListPlans',
            support_dot_v1_dot_support__pb2.ListPlansRequest.SerializeToString,
            support_dot_v1_dot_support__pb2.PlanList.FromString,
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
    def GetPlan(request,
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
            '/arangodb.cloud.support.v1.SupportService/GetPlan',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            support_dot_v1_dot_support__pb2.Plan.FromString,
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
    def ListFaqGroups(request,
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
            '/arangodb.cloud.support.v1.SupportService/ListFaqGroups',
            common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
            support_dot_v1_dot_support__pb2.FaqGroupList.FromString,
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
    def ListFaqGroupEntries(request,
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
            '/arangodb.cloud.support.v1.SupportService/ListFaqGroupEntries',
            common_dot_v1_dot_common__pb2.ListOptions.SerializeToString,
            support_dot_v1_dot_support__pb2.FaqGroupEntryList.FromString,
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
    def CreateSupportRequest(request,
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
            '/arangodb.cloud.support.v1.SupportService/CreateSupportRequest',
            support_dot_v1_dot_support__pb2.SupportRequest.SerializeToString,
            support_dot_v1_dot_support__pb2.SupportRequest.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
