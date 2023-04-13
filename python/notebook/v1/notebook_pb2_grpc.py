# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from notebook.v1 import notebook_pb2 as notebook_dot_v1_dot_notebook__pb2


class NotebookServiceStub(object):
    """Notebook service is used to manage notebooks.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                )
        self.GetNotebook = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/GetNotebook',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=notebook_dot_v1_dot_notebook__pb2.Notebook.FromString,
                )
        self.CreateNotebook = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/CreateNotebook',
                request_serializer=notebook_dot_v1_dot_notebook__pb2.Notebook.SerializeToString,
                response_deserializer=notebook_dot_v1_dot_notebook__pb2.Notebook.FromString,
                )
        self.DeleteNotebook = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/DeleteNotebook',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                )
        self.UpdateNotebook = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/UpdateNotebook',
                request_serializer=notebook_dot_v1_dot_notebook__pb2.Notebook.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                )
        self.ListNotebooks = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/ListNotebooks',
                request_serializer=notebook_dot_v1_dot_notebook__pb2.ListNotebooksRequest.SerializeToString,
                response_deserializer=notebook_dot_v1_dot_notebook__pb2.NotebookList.FromString,
                )
        self.ListNotebookModels = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/ListNotebookModels',
                request_serializer=notebook_dot_v1_dot_notebook__pb2.ListNotebookModelsRequest.SerializeToString,
                response_deserializer=notebook_dot_v1_dot_notebook__pb2.NotebookModelList.FromString,
                )
        self.PauseNotebook = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/PauseNotebook',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                )
        self.ResumeNotebook = channel.unary_unary(
                '/arangodb.cloud.notebook.v1.NotebookService/ResumeNotebook',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                )


class NotebookServiceServicer(object):
    """Notebook service is used to manage notebooks.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None (authenticated only)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNotebook(self, request, context):
        """Get a Notebook using its ID.
        Required permissions:
        - notebook.notebook.get on the notebook
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNotebook(self, request, context):
        """Create a new Notebook by specifying its configuration.
        Required permissions:
        - notebook.notebook.create on the deployment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNotebook(self, request, context):
        """Delete an existing notebook using its ID.
        This initially marks the notebook for deletion. It is deleted from CP once all its child resources are deleted.
        Required permissions:
        - notebook.notebook.delete on the notebook
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNotebook(self, request, context):
        """Update an existing notebook. Returns updated Notebook.
        Required permissions:
        - notebook.notebook.update on the notebook
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNotebooks(self, request, context):
        """List all notebooks for the deployments identified by the given deployment identifier.
        Required permissions:
        - notebook.notebook.list on the deployment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNotebookModels(self, request, context):
        """List all notebook models available in the context of the given deployment.
        Required permissions:
        - notebook.model.list globally
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseNotebook(self, request, context):
        """Pauses a running notebook identified by the given id.
        Required permissions:
        - notebook.notebook.pause on the notebook
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResumeNotebook(self, request, context):
        """Resumes a paused notebook identified by the given id.
        When ResumeNotebook is invoked on a notebook that has is_paused not set, an PreconditionFailed error is returned.
        Required permissions:
        - notebook.notebook.resume on the notebook
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotebookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'GetNotebook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNotebook,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=notebook_dot_v1_dot_notebook__pb2.Notebook.SerializeToString,
            ),
            'CreateNotebook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNotebook,
                    request_deserializer=notebook_dot_v1_dot_notebook__pb2.Notebook.FromString,
                    response_serializer=notebook_dot_v1_dot_notebook__pb2.Notebook.SerializeToString,
            ),
            'DeleteNotebook': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNotebook,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'UpdateNotebook': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNotebook,
                    request_deserializer=notebook_dot_v1_dot_notebook__pb2.Notebook.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'ListNotebooks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNotebooks,
                    request_deserializer=notebook_dot_v1_dot_notebook__pb2.ListNotebooksRequest.FromString,
                    response_serializer=notebook_dot_v1_dot_notebook__pb2.NotebookList.SerializeToString,
            ),
            'ListNotebookModels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNotebookModels,
                    request_deserializer=notebook_dot_v1_dot_notebook__pb2.ListNotebookModelsRequest.FromString,
                    response_serializer=notebook_dot_v1_dot_notebook__pb2.NotebookModelList.SerializeToString,
            ),
            'PauseNotebook': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseNotebook,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'ResumeNotebook': grpc.unary_unary_rpc_method_handler(
                    servicer.ResumeNotebook,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.notebook.v1.NotebookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NotebookService(object):
    """Notebook service is used to manage notebooks.
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
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/GetAPIVersion',
            common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            common_dot_v1_dot_common__pb2.Version.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNotebook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/GetNotebook',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            notebook_dot_v1_dot_notebook__pb2.Notebook.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNotebook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/CreateNotebook',
            notebook_dot_v1_dot_notebook__pb2.Notebook.SerializeToString,
            notebook_dot_v1_dot_notebook__pb2.Notebook.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNotebook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/DeleteNotebook',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            common_dot_v1_dot_common__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNotebook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/UpdateNotebook',
            notebook_dot_v1_dot_notebook__pb2.Notebook.SerializeToString,
            common_dot_v1_dot_common__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNotebooks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/ListNotebooks',
            notebook_dot_v1_dot_notebook__pb2.ListNotebooksRequest.SerializeToString,
            notebook_dot_v1_dot_notebook__pb2.NotebookList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNotebookModels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/ListNotebookModels',
            notebook_dot_v1_dot_notebook__pb2.ListNotebookModelsRequest.SerializeToString,
            notebook_dot_v1_dot_notebook__pb2.NotebookModelList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PauseNotebook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/PauseNotebook',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            common_dot_v1_dot_common__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResumeNotebook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/arangodb.cloud.notebook.v1.NotebookService/ResumeNotebook',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            common_dot_v1_dot_common__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
