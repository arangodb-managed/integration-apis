from common.v1 import common_pb2 as _common_pb2
from github.com.golang.protobuf.ptypes.timestamp import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IsPrivateEndpointServiceFeatureAvailableRequest(_message.Message):
    __slots__ = ["deployment_id", "organization_id", "region_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    organization_id: str
    region_id: str
    def __init__(self, deployment_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class IsPrivateEndpointServiceFeatureAvailableResult(_message.Message):
    __slots__ = ["available", "message"]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    available: bool
    message: str
    def __init__(self, available: bool = ..., message: _Optional[str] = ...) -> None: ...

class PrivateEndpointService(_message.Message):
    __slots__ = ["aks", "alternate_dns_names", "aws", "created_at", "deleted_at", "deployment_id", "description", "gcp", "id", "is_deleted", "name", "status", "url"]
    class Aks(_message.Message):
        __slots__ = ["client_subscription_ids"]
        CLIENT_SUBSCRIPTION_IDS_FIELD_NUMBER: _ClassVar[int]
        client_subscription_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, client_subscription_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class AksPrivateEndpointConnectionStatus(_message.Message):
        __slots__ = ["description", "id", "name", "state"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        description: str
        id: str
        name: str
        state: str
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., state: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class AksStatus(_message.Message):
        __slots__ = ["alias", "private_endpoint_connections"]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        alias: str
        private_endpoint_connections: _containers.RepeatedCompositeFieldContainer[PrivateEndpointService.AksPrivateEndpointConnectionStatus]
        def __init__(self, alias: _Optional[str] = ..., private_endpoint_connections: _Optional[_Iterable[_Union[PrivateEndpointService.AksPrivateEndpointConnectionStatus, _Mapping]]] = ...) -> None: ...
    class Aws(_message.Message):
        __slots__ = ["aws_principals"]
        AWS_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
        aws_principals: _containers.RepeatedCompositeFieldContainer[PrivateEndpointService.AwsPrincipals]
        def __init__(self, aws_principals: _Optional[_Iterable[_Union[PrivateEndpointService.AwsPrincipals, _Mapping]]] = ...) -> None: ...
    class AwsPrincipals(_message.Message):
        __slots__ = ["account_id", "role_names", "user_names"]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        ROLE_NAMES_FIELD_NUMBER: _ClassVar[int]
        USER_NAMES_FIELD_NUMBER: _ClassVar[int]
        account_id: str
        role_names: _containers.RepeatedScalarFieldContainer[str]
        user_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, account_id: _Optional[str] = ..., user_names: _Optional[_Iterable[str]] = ..., role_names: _Optional[_Iterable[str]] = ...) -> None: ...
    class AwsPrivateEndpointConnectionStatus(_message.Message):
        __slots__ = ["created_at", "id", "owner", "state"]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        OWNER_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        created_at: _timestamp_pb2.Timestamp
        id: str
        owner: str
        state: str
        def __init__(self, owner: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class AwsStatus(_message.Message):
        __slots__ = ["availability_zones", "private_endpoint_connections", "service_name"]
        AVAILABILITY_ZONES_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        availability_zones: _containers.RepeatedScalarFieldContainer[str]
        private_endpoint_connections: _containers.RepeatedCompositeFieldContainer[PrivateEndpointService.AwsPrivateEndpointConnectionStatus]
        service_name: str
        def __init__(self, service_name: _Optional[str] = ..., availability_zones: _Optional[_Iterable[str]] = ..., private_endpoint_connections: _Optional[_Iterable[_Union[PrivateEndpointService.AwsPrivateEndpointConnectionStatus, _Mapping]]] = ...) -> None: ...
    class Gcp(_message.Message):
        __slots__ = ["projects"]
        PROJECTS_FIELD_NUMBER: _ClassVar[int]
        projects: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, projects: _Optional[_Iterable[str]] = ...) -> None: ...
    class GcpPrivateEndpointConnectionStatus(_message.Message):
        __slots__ = ["id", "name", "state"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        state: str
        def __init__(self, name: _Optional[str] = ..., state: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class GcpStatus(_message.Message):
        __slots__ = ["private_endpoint_connections", "service_attachment"]
        PRIVATE_ENDPOINT_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        private_endpoint_connections: _containers.RepeatedCompositeFieldContainer[PrivateEndpointService.GcpPrivateEndpointConnectionStatus]
        service_attachment: str
        def __init__(self, service_attachment: _Optional[str] = ..., private_endpoint_connections: _Optional[_Iterable[_Union[PrivateEndpointService.GcpPrivateEndpointConnectionStatus, _Mapping]]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["aks", "aws", "gcp", "message", "needs_attention", "ready", "ready_at"]
        AKS_FIELD_NUMBER: _ClassVar[int]
        AWS_FIELD_NUMBER: _ClassVar[int]
        GCP_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NEEDS_ATTENTION_FIELD_NUMBER: _ClassVar[int]
        READY_AT_FIELD_NUMBER: _ClassVar[int]
        READY_FIELD_NUMBER: _ClassVar[int]
        aks: PrivateEndpointService.AksStatus
        aws: PrivateEndpointService.AwsStatus
        gcp: PrivateEndpointService.GcpStatus
        message: str
        needs_attention: bool
        ready: bool
        ready_at: _timestamp_pb2.Timestamp
        def __init__(self, ready: bool = ..., ready_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., needs_attention: bool = ..., message: _Optional[str] = ..., aks: _Optional[_Union[PrivateEndpointService.AksStatus, _Mapping]] = ..., aws: _Optional[_Union[PrivateEndpointService.AwsStatus, _Mapping]] = ..., gcp: _Optional[_Union[PrivateEndpointService.GcpStatus, _Mapping]] = ...) -> None: ...
    AKS_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_DNS_NAMES_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GCP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    aks: PrivateEndpointService.Aks
    alternate_dns_names: _containers.RepeatedScalarFieldContainer[str]
    aws: PrivateEndpointService.Aws
    created_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    deployment_id: str
    description: str
    gcp: PrivateEndpointService.Gcp
    id: str
    is_deleted: bool
    name: str
    status: PrivateEndpointService.Status
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., deployment_id: _Optional[str] = ..., alternate_dns_names: _Optional[_Iterable[str]] = ..., aks: _Optional[_Union[PrivateEndpointService.Aks, _Mapping]] = ..., aws: _Optional[_Union[PrivateEndpointService.Aws, _Mapping]] = ..., gcp: _Optional[_Union[PrivateEndpointService.Gcp, _Mapping]] = ..., status: _Optional[_Union[PrivateEndpointService.Status, _Mapping]] = ...) -> None: ...
