# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parking.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='parking.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rparking.proto\"8\n\x0fuserDetailsPark\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x15\n\x05\x63\x61rId\x18\x02 \x01(\x0b\x32\x06.carId\"\x1c\n\x08location\x12\x10\n\x08location\x18\x01 \x01(\t\"\x16\n\x05\x63\x61rId\x12\r\n\x05\x63\x61rId\x18\x01 \x01(\t\"W\n\x11userDetailsUnPark\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x15\n\x05\x63\x61rId\x18\x02 \x01(\x0b\x32\x06.carId\x12\x1b\n\x08location\x18\x03 \x01(\x0b\x32\t.location\"\x17\n\x08response\x12\x0b\n\x03Msg\x18\x01 \x01(\t2W\n\x07userApi\x12#\n\x04park\x12\x10.userDetailsPark\x1a\t.location\x12\'\n\x06unPark\x12\x12.userDetailsUnPark\x1a\t.responseb\x06proto3')
)




_USERDETAILSPARK = _descriptor.Descriptor(
  name='userDetailsPark',
  full_name='userDetailsPark',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='userDetailsPark.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='carId', full_name='userDetailsPark.carId', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=73,
)


_LOCATION = _descriptor.Descriptor(
  name='location',
  full_name='location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='location.location', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=103,
)


_CARID = _descriptor.Descriptor(
  name='carId',
  full_name='carId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='carId', full_name='carId.carId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=127,
)


_USERDETAILSUNPARK = _descriptor.Descriptor(
  name='userDetailsUnPark',
  full_name='userDetailsUnPark',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='userDetailsUnPark.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='carId', full_name='userDetailsUnPark.carId', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='userDetailsUnPark.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=216,
)


_RESPONSE = _descriptor.Descriptor(
  name='response',
  full_name='response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Msg', full_name='response.Msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=241,
)

_USERDETAILSPARK.fields_by_name['carId'].message_type = _CARID
_USERDETAILSUNPARK.fields_by_name['carId'].message_type = _CARID
_USERDETAILSUNPARK.fields_by_name['location'].message_type = _LOCATION
DESCRIPTOR.message_types_by_name['userDetailsPark'] = _USERDETAILSPARK
DESCRIPTOR.message_types_by_name['location'] = _LOCATION
DESCRIPTOR.message_types_by_name['carId'] = _CARID
DESCRIPTOR.message_types_by_name['userDetailsUnPark'] = _USERDETAILSUNPARK
DESCRIPTOR.message_types_by_name['response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

userDetailsPark = _reflection.GeneratedProtocolMessageType('userDetailsPark', (_message.Message,), {
  'DESCRIPTOR' : _USERDETAILSPARK,
  '__module__' : 'parking_pb2'
  # @@protoc_insertion_point(class_scope:userDetailsPark)
  })
_sym_db.RegisterMessage(userDetailsPark)

location = _reflection.GeneratedProtocolMessageType('location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'parking_pb2'
  # @@protoc_insertion_point(class_scope:location)
  })
_sym_db.RegisterMessage(location)

carId = _reflection.GeneratedProtocolMessageType('carId', (_message.Message,), {
  'DESCRIPTOR' : _CARID,
  '__module__' : 'parking_pb2'
  # @@protoc_insertion_point(class_scope:carId)
  })
_sym_db.RegisterMessage(carId)

userDetailsUnPark = _reflection.GeneratedProtocolMessageType('userDetailsUnPark', (_message.Message,), {
  'DESCRIPTOR' : _USERDETAILSUNPARK,
  '__module__' : 'parking_pb2'
  # @@protoc_insertion_point(class_scope:userDetailsUnPark)
  })
_sym_db.RegisterMessage(userDetailsUnPark)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'parking_pb2'
  # @@protoc_insertion_point(class_scope:response)
  })
_sym_db.RegisterMessage(response)



_USERAPI = _descriptor.ServiceDescriptor(
  name='userApi',
  full_name='userApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=243,
  serialized_end=330,
  methods=[
  _descriptor.MethodDescriptor(
    name='park',
    full_name='userApi.park',
    index=0,
    containing_service=None,
    input_type=_USERDETAILSPARK,
    output_type=_LOCATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='unPark',
    full_name='userApi.unPark',
    index=1,
    containing_service=None,
    input_type=_USERDETAILSUNPARK,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERAPI)

DESCRIPTOR.services_by_name['userApi'] = _USERAPI

# @@protoc_insertion_point(module_scope)
