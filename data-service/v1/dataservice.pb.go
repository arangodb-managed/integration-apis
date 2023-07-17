// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: dataservice.proto

package v1

import (
	context "context"
	fmt "fmt"
	v1 "github.com/arangodb-managed/apis/common/v1"
	v11 "github.com/arangodb-managed/apis/data/v1"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

func init() { proto.RegisterFile("dataservice.proto", fileDescriptor_2a4d2d62adc5d541) }

var fileDescriptor_2a4d2d62adc5d541 = []byte{
	// 237 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x5c, 0x8f, 0xb1, 0x4a, 0xc6, 0x30,
	0x10, 0xc7, 0xed, 0xe2, 0x50, 0x27, 0x3b, 0x38, 0x14, 0xe9, 0xe2, 0xe4, 0xd0, 0x84, 0xe8, 0xea,
	0xa4, 0x05, 0x71, 0x51, 0xd0, 0xcd, 0xed, 0xda, 0x1c, 0x35, 0xd0, 0xe6, 0x4a, 0x72, 0x5f, 0xc0,
	0xd1, 0xb7, 0xf0, 0x91, 0x1c, 0x7d, 0x04, 0xa9, 0x2f, 0x22, 0x69, 0x3e, 0xf9, 0x4a, 0xa7, 0x84,
	0xe3, 0x7f, 0xbf, 0xfb, 0xff, 0xf2, 0x53, 0x0d, 0x0c, 0x1e, 0x5d, 0x30, 0x1d, 0x8a, 0xc9, 0x11,
	0x53, 0x71, 0x09, 0x0e, 0x6c, 0x4f, 0xba, 0x15, 0xdd, 0x40, 0x3b, 0x2d, 0x8c, 0x65, 0xec, 0x1d,
	0xb0, 0x21, 0x2b, 0xd6, 0xe9, 0xa0, 0xca, 0xb3, 0x8e, 0xc6, 0x91, 0xac, 0x0c, 0x4a, 0xa6, 0x5f,
	0x42, 0x94, 0x45, 0xcc, 0xc5, 0x69, 0x7c, 0xd3, 0xec, 0xea, 0x23, 0xcb, 0x4f, 0x1a, 0x60, 0x78,
	0x49, 0xeb, 0x85, 0xcb, 0xcf, 0xef, 0x91, 0x1b, 0x9c, 0x06, 0x7a, 0x1f, 0xd1, 0xf2, 0x33, 0x11,
	0xdf, 0x39, 0xd4, 0x68, 0xd9, 0xc0, 0xe0, 0x8b, 0x0b, 0xb1, 0xe9, 0xb1, 0xbf, 0x10, 0x94, 0x78,
	0x68, 0x9e, 0xa6, 0x58, 0xc7, 0x97, 0xf5, 0x36, 0xb4, 0x1c, 0x0c, 0x4a, 0x1c, 0xb8, 0x2b, 0xe6,
	0xed, 0xe3, 0xd7, 0x5c, 0x65, 0xdf, 0x73, 0x95, 0xfd, 0xcc, 0x55, 0xf6, 0xf9, 0x5b, 0x1d, 0xbd,
	0xde, 0xf4, 0x86, 0xdf, 0x76, 0x6d, 0x84, 0xcb, 0x7f, 0x54, 0x3d, 0x82, 0x85, 0x1e, 0xb5, 0x5c,
	0x99, 0xd7, 0x30, 0x19, 0xbf, 0xe8, 0xd4, 0x7b, 0x7f, 0x19, 0x54, 0x7b, 0xbc, 0xa8, 0x5d, 0xff,
	0x05, 0x00, 0x00, 0xff, 0xff, 0x2e, 0xf8, 0x30, 0xb3, 0x46, 0x01, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// DataServiceClient is the client API for DataService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type DataServiceClient interface {
	// Fetch the credentials for the root user of the deployment with given ID.
	// Required permissions:
	// - dataservice.deployment.get-root-credentials on the given deployment.
	GetDeploymentRootCredentials(ctx context.Context, in *v1.IDOptions, opts ...grpc.CallOption) (*v11.DeploymentCredentials, error)
}

type dataServiceClient struct {
	cc *grpc.ClientConn
}

func NewDataServiceClient(cc *grpc.ClientConn) DataServiceClient {
	return &dataServiceClient{cc}
}

func (c *dataServiceClient) GetDeploymentRootCredentials(ctx context.Context, in *v1.IDOptions, opts ...grpc.CallOption) (*v11.DeploymentCredentials, error) {
	out := new(v11.DeploymentCredentials)
	err := c.cc.Invoke(ctx, "/arangodb.cloud.integration.dataservice.v1.DataService/GetDeploymentRootCredentials", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DataServiceServer is the server API for DataService service.
type DataServiceServer interface {
	// Fetch the credentials for the root user of the deployment with given ID.
	// Required permissions:
	// - dataservice.deployment.get-root-credentials on the given deployment.
	GetDeploymentRootCredentials(context.Context, *v1.IDOptions) (*v11.DeploymentCredentials, error)
}

// UnimplementedDataServiceServer can be embedded to have forward compatible implementations.
type UnimplementedDataServiceServer struct {
}

func (*UnimplementedDataServiceServer) GetDeploymentRootCredentials(ctx context.Context, req *v1.IDOptions) (*v11.DeploymentCredentials, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetDeploymentRootCredentials not implemented")
}

func RegisterDataServiceServer(s *grpc.Server, srv DataServiceServer) {
	s.RegisterService(&_DataService_serviceDesc, srv)
}

func _DataService_GetDeploymentRootCredentials_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.IDOptions)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DataServiceServer).GetDeploymentRootCredentials(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/arangodb.cloud.integration.dataservice.v1.DataService/GetDeploymentRootCredentials",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DataServiceServer).GetDeploymentRootCredentials(ctx, req.(*v1.IDOptions))
	}
	return interceptor(ctx, in, info, handler)
}

var _DataService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "arangodb.cloud.integration.dataservice.v1.DataService",
	HandlerType: (*DataServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetDeploymentRootCredentials",
			Handler:    _DataService_GetDeploymentRootCredentials_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "dataservice.proto",
}
