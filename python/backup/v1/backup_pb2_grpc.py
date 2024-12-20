# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from backup.v1 import backup_pb2 as backup_dot_v1_dot_backup__pb2
from common.v1 import common_pb2 as common_dot_v1_dot_common__pb2

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
        + f' but the generated code in backup/v1/backup_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BackupServiceStub(object):
    """BackupService is the API used to configure backup objects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAPIVersion = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/GetAPIVersion',
                request_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Version.FromString,
                _registered_method=True)
        self.IsBackupFeatureAvailable = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/IsBackupFeatureAvailable',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.YesOrNo.FromString,
                _registered_method=True)
        self.IsBackupUploadFeatureAvailable = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/IsBackupUploadFeatureAvailable',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.YesOrNo.FromString,
                _registered_method=True)
        self.IsMultiRegionBackupUploadFeatureAvailable = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/IsMultiRegionBackupUploadFeatureAvailable',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.YesOrNo.FromString,
                _registered_method=True)
        self.ListBackupPolicies = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/ListBackupPolicies',
                request_serializer=backup_dot_v1_dot_backup__pb2.ListBackupPoliciesRequest.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.BackupPolicyList.FromString,
                _registered_method=True)
        self.GetBackupPolicy = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/GetBackupPolicy',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.FromString,
                _registered_method=True)
        self.CreateBackupPolicy = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/CreateBackupPolicy',
                request_serializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.FromString,
                _registered_method=True)
        self.UpdateBackupPolicy = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/UpdateBackupPolicy',
                request_serializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.FromString,
                _registered_method=True)
        self.DeleteBackupPolicy = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/DeleteBackupPolicy',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)
        self.ListBackups = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/ListBackups',
                request_serializer=backup_dot_v1_dot_backup__pb2.ListBackupsRequest.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.BackupList.FromString,
                _registered_method=True)
        self.GetBackup = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/GetBackup',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.Backup.FromString,
                _registered_method=True)
        self.CreateBackup = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/CreateBackup',
                request_serializer=backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.Backup.FromString,
                _registered_method=True)
        self.UpdateBackup = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/UpdateBackup',
                request_serializer=backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.Backup.FromString,
                _registered_method=True)
        self.DownloadBackup = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/DownloadBackup',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)
        self.RestoreBackup = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/RestoreBackup',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)
        self.DeleteBackup = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/DeleteBackup',
                request_serializer=common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
                response_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                _registered_method=True)
        self.CopyBackup = channel.unary_unary(
                '/arangodb.cloud.backup.v1.BackupService/CopyBackup',
                request_serializer=backup_dot_v1_dot_backup__pb2.CopyBackupRequest.SerializeToString,
                response_deserializer=backup_dot_v1_dot_backup__pb2.Backup.FromString,
                _registered_method=True)


class BackupServiceServicer(object):
    """BackupService is the API used to configure backup objects.
    """

    def GetAPIVersion(self, request, context):
        """Get the current API version of this service.
        Required permissions:
        - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsBackupFeatureAvailable(self, request, context):
        """Checks if the backup feature is enabled and available for a specific deployment.
        Required permissions:
        - backup.feature.get on the deployment that is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsBackupUploadFeatureAvailable(self, request, context):
        """Checks if the backup upload feature is enabled for a specific deployment.
        Required permissions:
        - backup.feature.get on the deployment that is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsMultiRegionBackupUploadFeatureAvailable(self, request, context):
        """Checks if the multi region backup upload feature is enabled for a specific deployment.
        Required permissions:
        - backup.feature.get on the deployment that is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBackupPolicies(self, request, context):
        """Fetch all backup policies for a specific deployment.
        Required permissions:
        - backup.backuppolicy.list on the deployment that owns the backup policies and is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBackupPolicy(self, request, context):
        """Fetch a backup policy identified by the given ID.
        Required permissions:
        - backup.backuppolicy.get on the backup policy identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBackupPolicy(self, request, context):
        """Create a new backup policy
        Required permissions:
        -  backup.backuppolicy.create on the deployment that owns the backup policy and is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBackupPolicy(self, request, context):
        """Update a backup policy
        Required permissions:
        -  backup.backuppolicy.update on the backup policy identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBackupPolicy(self, request, context):
        """Delete a backup policy identified by the given ID.
        Note that the backup policy are initially only marked for deletion, no backups will be deleted with this operation.
        Once all their dependent backups are removed, the backup policy is removed.
        Required permissions:
        -  backup.backuppolicy.delete on the backup policy identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBackups(self, request, context):
        """Fetch all backups for a specific deployment.
        Required permissions:
        - backup.backup.list on the deployment that owns the backup and is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBackup(self, request, context):
        """Fetch a backup identified by the given ID.
        Required permissions:
        - backup.backup.get on the backup identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBackup(self, request, context):
        """Create a new manual backup
        Setting the backup_policy_id field in the backup is not allowed
        Required permissions:
        -  backup.backup.create on the deployment that owns the backup and is identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBackup(self, request, context):
        """Update a backup
        Required permissions:
        -  backup.backup.update on the backup identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadBackup(self, request, context):
        """Download a backup identified by the given ID from remote storage to the volumes of the servers of the deployment.
        This operation can only be executed on backups which have the same number of DB Servers in the backup and the current running cluster.
        If this backup was already downloaded, another download will be done.
        If the backup is still available on the cluster there is no need to explicitly download the backup before restoring.
        This function will return immediately.
        To track status, please invoke GetBackup and check the .status field inside the returned backup object
        Required permissions:
        -  backup.backup.download on the backup identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestoreBackup(self, request, context):
        """Restore (or recover) a backup identified by the given ID
        This operation can only be executed on backups where status.available is set and
        the mayor and minor version of the backup and the current running cluster are the same.
        This function will return immediately.
        To track status, please invoke GetDeployment on the data API and check the
        .status.restoring_backup and .status.restore_backup_status fields inside the returned deployment object
        Required permissions (both are needed):
        -  backup.backup.restore on the backup identified by the given ID.
        -  data.deployment.restore-backup on the deployment that owns this backup
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBackup(self, request, context):
        """Delete a backup identified by the given ID, after which removal of any remote storage of the backup is started.
        Note that the backup are initially only marked for deletion.
        Once all remote storage for the backup has been removed, the backup itself is removed.
        Required permissions:
        -  backup.backup.delete on the backup identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CopyBackup(self, request, context):
        """Copy a backup manually from source backup to a given region identifier.
        It is not allowed to copy backup that does not have upload flag set to true
        Required permissions:
        - backup.backup.copy on the backup identified by the given ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BackupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=common_dot_v1_dot_common__pb2.Empty.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Version.SerializeToString,
            ),
            'IsBackupFeatureAvailable': grpc.unary_unary_rpc_method_handler(
                    servicer.IsBackupFeatureAvailable,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.YesOrNo.SerializeToString,
            ),
            'IsBackupUploadFeatureAvailable': grpc.unary_unary_rpc_method_handler(
                    servicer.IsBackupUploadFeatureAvailable,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.YesOrNo.SerializeToString,
            ),
            'IsMultiRegionBackupUploadFeatureAvailable': grpc.unary_unary_rpc_method_handler(
                    servicer.IsMultiRegionBackupUploadFeatureAvailable,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.YesOrNo.SerializeToString,
            ),
            'ListBackupPolicies': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBackupPolicies,
                    request_deserializer=backup_dot_v1_dot_backup__pb2.ListBackupPoliciesRequest.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.BackupPolicyList.SerializeToString,
            ),
            'GetBackupPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBackupPolicy,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.SerializeToString,
            ),
            'CreateBackupPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBackupPolicy,
                    request_deserializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.SerializeToString,
            ),
            'UpdateBackupPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBackupPolicy,
                    request_deserializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.BackupPolicy.SerializeToString,
            ),
            'DeleteBackupPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBackupPolicy,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'ListBackups': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBackups,
                    request_deserializer=backup_dot_v1_dot_backup__pb2.ListBackupsRequest.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.BackupList.SerializeToString,
            ),
            'GetBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBackup,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
            ),
            'CreateBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBackup,
                    request_deserializer=backup_dot_v1_dot_backup__pb2.Backup.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
            ),
            'UpdateBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBackup,
                    request_deserializer=backup_dot_v1_dot_backup__pb2.Backup.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
            ),
            'DownloadBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadBackup,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'RestoreBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.RestoreBackup,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'DeleteBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBackup,
                    request_deserializer=common_dot_v1_dot_common__pb2.IDOptions.FromString,
                    response_serializer=common_dot_v1_dot_common__pb2.Empty.SerializeToString,
            ),
            'CopyBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.CopyBackup,
                    request_deserializer=backup_dot_v1_dot_backup__pb2.CopyBackupRequest.FromString,
                    response_serializer=backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'arangodb.cloud.backup.v1.BackupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('arangodb.cloud.backup.v1.BackupService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BackupService(object):
    """BackupService is the API used to configure backup objects.
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
            '/arangodb.cloud.backup.v1.BackupService/GetAPIVersion',
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
    def IsBackupFeatureAvailable(request,
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
            '/arangodb.cloud.backup.v1.BackupService/IsBackupFeatureAvailable',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            common_dot_v1_dot_common__pb2.YesOrNo.FromString,
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
    def IsBackupUploadFeatureAvailable(request,
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
            '/arangodb.cloud.backup.v1.BackupService/IsBackupUploadFeatureAvailable',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            common_dot_v1_dot_common__pb2.YesOrNo.FromString,
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
    def IsMultiRegionBackupUploadFeatureAvailable(request,
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
            '/arangodb.cloud.backup.v1.BackupService/IsMultiRegionBackupUploadFeatureAvailable',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            common_dot_v1_dot_common__pb2.YesOrNo.FromString,
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
    def ListBackupPolicies(request,
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
            '/arangodb.cloud.backup.v1.BackupService/ListBackupPolicies',
            backup_dot_v1_dot_backup__pb2.ListBackupPoliciesRequest.SerializeToString,
            backup_dot_v1_dot_backup__pb2.BackupPolicyList.FromString,
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
    def GetBackupPolicy(request,
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
            '/arangodb.cloud.backup.v1.BackupService/GetBackupPolicy',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            backup_dot_v1_dot_backup__pb2.BackupPolicy.FromString,
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
    def CreateBackupPolicy(request,
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
            '/arangodb.cloud.backup.v1.BackupService/CreateBackupPolicy',
            backup_dot_v1_dot_backup__pb2.BackupPolicy.SerializeToString,
            backup_dot_v1_dot_backup__pb2.BackupPolicy.FromString,
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
    def UpdateBackupPolicy(request,
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
            '/arangodb.cloud.backup.v1.BackupService/UpdateBackupPolicy',
            backup_dot_v1_dot_backup__pb2.BackupPolicy.SerializeToString,
            backup_dot_v1_dot_backup__pb2.BackupPolicy.FromString,
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
    def DeleteBackupPolicy(request,
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
            '/arangodb.cloud.backup.v1.BackupService/DeleteBackupPolicy',
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
    def ListBackups(request,
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
            '/arangodb.cloud.backup.v1.BackupService/ListBackups',
            backup_dot_v1_dot_backup__pb2.ListBackupsRequest.SerializeToString,
            backup_dot_v1_dot_backup__pb2.BackupList.FromString,
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
    def GetBackup(request,
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
            '/arangodb.cloud.backup.v1.BackupService/GetBackup',
            common_dot_v1_dot_common__pb2.IDOptions.SerializeToString,
            backup_dot_v1_dot_backup__pb2.Backup.FromString,
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
    def CreateBackup(request,
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
            '/arangodb.cloud.backup.v1.BackupService/CreateBackup',
            backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
            backup_dot_v1_dot_backup__pb2.Backup.FromString,
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
    def UpdateBackup(request,
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
            '/arangodb.cloud.backup.v1.BackupService/UpdateBackup',
            backup_dot_v1_dot_backup__pb2.Backup.SerializeToString,
            backup_dot_v1_dot_backup__pb2.Backup.FromString,
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
    def DownloadBackup(request,
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
            '/arangodb.cloud.backup.v1.BackupService/DownloadBackup',
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
    def RestoreBackup(request,
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
            '/arangodb.cloud.backup.v1.BackupService/RestoreBackup',
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
    def DeleteBackup(request,
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
            '/arangodb.cloud.backup.v1.BackupService/DeleteBackup',
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
    def CopyBackup(request,
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
            '/arangodb.cloud.backup.v1.BackupService/CopyBackup',
            backup_dot_v1_dot_backup__pb2.CopyBackupRequest.SerializeToString,
            backup_dot_v1_dot_backup__pb2.Backup.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
