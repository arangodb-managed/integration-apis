# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from data.v1 import data_pb2 as data_dot_v1_dot_data__pb2
from replication.v1 import replication_pb2 as replication_dot_v1_dot_replication__pb2

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
        + f' but the generated code in replication/v1/replication_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ReplicationServiceStub(object):
    """ReplicationService is the API used to replicate a deployment.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.replication.v1.ReplicationService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.CloneDeploymentFromBackup = channel.unary_unary(
                '/arangodb.cloud.replication.v1.ReplicationService/CloneDeploymentFromBackup',
                request_serializer=replication_dot_v1_dot_replication__pb2.CloneDeploymentFromBackupRequest.SerializeToString,
                response_deserializer=data_dot_v1_dot_data__pb2.Deployment.FromString,
                _registered_method=True)
        self.GetDeploymentReplication = channel.unary_unary(
                '/arangodb.cloud.replication.v1.ReplicationService/GetDeploymentReplication',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=replication_dot_v1_dot_replication__pb2.DeploymentReplication.FromString,
                _registered_method=True)
        self.UpdateDeploymentReplication = channel.unary_unary(
                '/arangodb.cloud.replication.v1.ReplicationService/UpdateDeploymentReplication',
                request_serializer=replication_dot_v1_dot_replication__pb2.DeploymentReplication.SerializeToString,
                response_deserializer=replication_dot_v1_dot_replication__pb2.DeploymentReplication.FromString,
                _registered_method=True)
        self.CreateDeploymentMigration = channel.unary_unary(
                '/arangodb.cloud.replication.v1.ReplicationService/CreateDeploymentMigration',
                request_serializer=replication_dot_v1_dot_replication__pb2.DeploymentMigration.SerializeToString,
                response_deserializer=replication_dot_v1_dot_replication__pb2.DeploymentMigration.FromString,
                _registered_method=True)
        self.GetDeploymentMigration = channel.unary_unary(
                '/arangodb.cloud.replication.v1.ReplicationService/GetDeploymentMigration',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=replication_dot_v1_dot_replication__pb2.DeploymentMigration.FromString,
                _registered_method=True)
        self.DeleteDeploymentMigration = channel.unary_unary(
                '/arangodb.cloud.replication.v1.ReplicationService/DeleteDeploymentMigration',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)


class ReplicationServiceServicer(object):
    """ReplicationService is the API used to replicate a deployment.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloneDeploymentFromBackup(self, request, context):
        """Takes a backup and creates a deployment from it. For all intents and purposes this new deployment
        will be the same as the deployment at that exact moment when the backup was taken from it. This means that
        the new deployment will be in the same project and use the same provider as the old deployment did. Optionally
        a different region can be provided using the region id field on the request. Furthermore, the new deployment
        will have the same server settings ( count, mode, replication factor ) as the old deployment did at the time
        of taking the backup. After the new deployment successfully started, the backup will be used to restore the
        data into the new deployment. The new deployment will have a different endpoint, and the password will also
        be reset for it. All other user settings will remain the same.
        The old deployment will not be touched.
        Required permissions:
        if project_id is specified
        - backup.backup.get on the backup specified by backup_id in request
        - replication.deployment.clone-from-backup on the project specified in request
        if project_id is not specified
        - replication.deployment.clone-from-backup on the backup specified by backup_id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeploymentReplication(self, request, context):
        """Get an existing DeploymentReplication using its deployment ID
        Required permissions:
        - replication.deploymentreplication.get
        [Deprecated] This method shouldn't be used anymore, the permission is removed from the system already to prevent usage.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDeploymentReplication(self, request, context):
        """Update an existing DeploymentReplication spec. If does not exist, this will create a new one.
        This call expects the complete entity with the updated fields.
        Required permissions:
        - replication.deploymentreplication.update
        [Deprecated] This method shouldn't be used anymore, the permission is removed from the system already to prevent usage.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDeploymentMigration(self, request, context):
        """Create a new deployment migration.
        Note: currently migration is supported only for Deployments with 'free' model.
        Required permissions:
        - replication.deploymentmigration.create on the specified deployment ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeploymentMigration(self, request, context):
        """Get info about the deployment migration for a deployment identified by the given ID.
        Required permissions:
        - replication.deploymentmigration.get on the specified deployment ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDeploymentMigration(self, request, context):
        """Delete an existing DeploymentMigration.
        A DeploymentMigration may be deleted only if it is in COMPLETE or FAILED state.
        Required permissions:
        - replication.deploymentmigration.delete on the specified deployment ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReplicationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'CloneDeploymentFromBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.CloneDeploymentFromBackup,
                    request_deserializer=replication_dot_v1_dot_replication__pb2.CloneDeploymentFromBackupRequest.FromString,
                    response_serializer=data_dot_v1_dot_data__pb2.Deployment.SerializeToString,
            ),
            'GetDeploymentReplication': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeploymentReplication,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=replication_dot_v1_dot_replication__pb2.DeploymentReplication.SerializeToString,
            ),
            'UpdateDeploymentReplication': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDeploymentReplication,
                    request_deserializer=replication_dot_v1_dot_replication__pb2.DeploymentReplication.FromString,
                    response_serializer=replication_dot_v1_dot_replication__pb2.DeploymentReplication.SerializeToString,
            ),
            'CreateDeploymentMigration': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDeploymentMigration,
                    request_deserializer=replication_dot_v1_dot_replication__pb2.DeploymentMigration.FromString,
                    response_serializer=replication_dot_v1_dot_replication__pb2.DeploymentMigration.SerializeToString,
            ),
            'GetDeploymentMigration': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeploymentMigration,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=replication_dot_v1_dot_replication__pb2.DeploymentMigration.SerializeToString,
            ),
            'DeleteDeploymentMigration': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDeploymentMigration,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.replication.v1.ReplicationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.replication.v1.ReplicationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ReplicationService(object):
    """ReplicationService is the API used to replicate a deployment.
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
            '/arangodb.cloud.replication.v1.ReplicationService/GetAPIVersion',
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
    def CloneDeploymentFromBackup(request,
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
            '/arangodb.cloud.replication.v1.ReplicationService/CloneDeploymentFromBackup',
            replication_dot_v1_dot_replication__pb2.CloneDeploymentFromBackupRequest.SerializeToString,
            data_dot_v1_dot_data__pb2.Deployment.FromString,
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
    def GetDeploymentReplication(request,
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
            '/arangodb.cloud.replication.v1.ReplicationService/GetDeploymentReplication',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            replication_dot_v1_dot_replication__pb2.DeploymentReplication.FromString,
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
    def UpdateDeploymentReplication(request,
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
            '/arangodb.cloud.replication.v1.ReplicationService/UpdateDeploymentReplication',
            replication_dot_v1_dot_replication__pb2.DeploymentReplication.SerializeToString,
            replication_dot_v1_dot_replication__pb2.DeploymentReplication.FromString,
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
    def CreateDeploymentMigration(request,
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
            '/arangodb.cloud.replication.v1.ReplicationService/CreateDeploymentMigration',
            replication_dot_v1_dot_replication__pb2.DeploymentMigration.SerializeToString,
            replication_dot_v1_dot_replication__pb2.DeploymentMigration.FromString,
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
    def GetDeploymentMigration(request,
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
            '/arangodb.cloud.replication.v1.ReplicationService/GetDeploymentMigration',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            replication_dot_v1_dot_replication__pb2.DeploymentMigration.FromString,
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
    def DeleteDeploymentMigration(request,
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
            '/arangodb.cloud.replication.v1.ReplicationService/DeleteDeploymentMigration',
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
