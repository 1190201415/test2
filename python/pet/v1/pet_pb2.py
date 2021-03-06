# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pet/v1/pet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pet/v1/pet.proto',
  package='pet.v1',
  syntax='proto3',
  serialized_options=b'Z\006pet/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10pet/v1/pet.proto\x12\x06pet.v1\x1a\x1agoogle/type/1.proto\"\x92\x01\n\x03Pet\x12*\n\x08pet_type\x18\x01 \x01(\x0e\x32\x0f.pet.v1.PetTypeR\x07petType\x12\x15\n\x06pet_id\x18\x02 \x01(\tR\x05petId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x34\n\ncreated_at\x18\x04 \x01(\x0b\x32\x15.google.type.DateTimeR\tcreatedAt\"&\n\rGetPetRequest\x12\x15\n\x06pet_id\x18\x01 \x01(\tR\x05petId\"/\n\x0eGetPetResponse\x12\x1d\n\x03pet\x18\x01 \x01(\x0b\x32\x0b.pet.v1.PetR\x03pet\"O\n\rPutPetRequest\x12*\n\x08pet_type\x18\x01 \x01(\x0e\x32\x0f.pet.v1.PetTypeR\x07petType\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"/\n\x0ePutPetResponse\x12\x1d\n\x03pet\x18\x01 \x01(\x0b\x32\x0b.pet.v1.PetR\x03pet\")\n\x10\x44\x65letePetRequest\x12\x15\n\x06pet_id\x18\x01 \x01(\tR\x05petId\"\x13\n\x11\x44\x65letePetResponse*q\n\x07PetType\x12\x18\n\x14PET_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPET_TYPE_CAT\x10\x01\x12\x10\n\x0cPET_TYPE_DOG\x10\x02\x12\x12\n\x0ePET_TYPE_SNAKE\x10\x03\x12\x14\n\x10PET_TYPE_HAMSTER\x10\x04\x32\xcb\x01\n\x0fPetStoreService\x12\x39\n\x06GetPet\x12\x15.pet.v1.GetPetRequest\x1a\x16.pet.v1.GetPetResponse\"\x00\x12\x39\n\x06PutPet\x12\x15.pet.v1.PutPetRequest\x1a\x16.pet.v1.PutPetResponse\"\x00\x12\x42\n\tDeletePet\x12\x18.pet.v1.DeletePetRequest\x1a\x19.pet.v1.DeletePetResponse\"\x00\x42\x08Z\x06pet/v1b\x06proto3'
  ,
  dependencies=[google_dot_type_dot_datetime__pb2.DESCRIPTOR,])

_PETTYPE = _descriptor.EnumDescriptor(
  name='PetType',
  full_name='pet.v1.PetType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PET_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PET_TYPE_CAT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PET_TYPE_DOG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PET_TYPE_SNAKE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PET_TYPE_HAMSTER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=488,
  serialized_end=601,
)
_sym_db.RegisterEnumDescriptor(_PETTYPE)

PetType = enum_type_wrapper.EnumTypeWrapper(_PETTYPE)
PET_TYPE_UNSPECIFIED = 0
PET_TYPE_CAT = 1
PET_TYPE_DOG = 2
PET_TYPE_SNAKE = 3
PET_TYPE_HAMSTER = 4



_PET = _descriptor.Descriptor(
  name='Pet',
  full_name='pet.v1.Pet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pet_type', full_name='pet.v1.Pet.pet_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='petType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pet_id', full_name='pet.v1.Pet.pet_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='petId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='pet.v1.Pet.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='pet.v1.Pet.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createdAt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=57,
  serialized_end=203,
)


_GETPETREQUEST = _descriptor.Descriptor(
  name='GetPetRequest',
  full_name='pet.v1.GetPetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pet_id', full_name='pet.v1.GetPetRequest.pet_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='petId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=205,
  serialized_end=243,
)


_GETPETRESPONSE = _descriptor.Descriptor(
  name='GetPetResponse',
  full_name='pet.v1.GetPetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pet', full_name='pet.v1.GetPetResponse.pet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=245,
  serialized_end=292,
)


_PUTPETREQUEST = _descriptor.Descriptor(
  name='PutPetRequest',
  full_name='pet.v1.PutPetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pet_type', full_name='pet.v1.PutPetRequest.pet_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='petType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='pet.v1.PutPetRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=294,
  serialized_end=373,
)


_PUTPETRESPONSE = _descriptor.Descriptor(
  name='PutPetResponse',
  full_name='pet.v1.PutPetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pet', full_name='pet.v1.PutPetResponse.pet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=375,
  serialized_end=422,
)


_DELETEPETREQUEST = _descriptor.Descriptor(
  name='DeletePetRequest',
  full_name='pet.v1.DeletePetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pet_id', full_name='pet.v1.DeletePetRequest.pet_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='petId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=424,
  serialized_end=465,
)


_DELETEPETRESPONSE = _descriptor.Descriptor(
  name='DeletePetResponse',
  full_name='pet.v1.DeletePetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=467,
  serialized_end=486,
)

_PET.fields_by_name['pet_type'].enum_type = _PETTYPE
_PET.fields_by_name['created_at'].message_type = google_dot_type_dot_datetime__pb2._DATETIME
_GETPETRESPONSE.fields_by_name['pet'].message_type = _PET
_PUTPETREQUEST.fields_by_name['pet_type'].enum_type = _PETTYPE
_PUTPETRESPONSE.fields_by_name['pet'].message_type = _PET
DESCRIPTOR.message_types_by_name['Pet'] = _PET
DESCRIPTOR.message_types_by_name['GetPetRequest'] = _GETPETREQUEST
DESCRIPTOR.message_types_by_name['GetPetResponse'] = _GETPETRESPONSE
DESCRIPTOR.message_types_by_name['PutPetRequest'] = _PUTPETREQUEST
DESCRIPTOR.message_types_by_name['PutPetResponse'] = _PUTPETRESPONSE
DESCRIPTOR.message_types_by_name['DeletePetRequest'] = _DELETEPETREQUEST
DESCRIPTOR.message_types_by_name['DeletePetResponse'] = _DELETEPETRESPONSE
DESCRIPTOR.enum_types_by_name['PetType'] = _PETTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pet = _reflection.GeneratedProtocolMessageType('Pet', (_message.Message,), {
  'DESCRIPTOR' : _PET,
  '__module__' : 'pet.v1.pet_pb2'
  # @@protoc_insertion_point(class_scope:pet.v1.Pet)
  })
_sym_db.RegisterMessage(Pet)

GetPetRequest = _reflection.GeneratedProtocolMessageType('GetPetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPETREQUEST,
  '__module__' : 'pet.v1.pet_pb2'
  # @@protoc_insertion_point(class_scope:pet.v1.GetPetRequest)
  })
_sym_db.RegisterMessage(GetPetRequest)

GetPetResponse = _reflection.GeneratedProtocolMessageType('GetPetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPETRESPONSE,
  '__module__' : 'pet.v1.pet_pb2'
  # @@protoc_insertion_point(class_scope:pet.v1.GetPetResponse)
  })
_sym_db.RegisterMessage(GetPetResponse)

PutPetRequest = _reflection.GeneratedProtocolMessageType('PutPetRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTPETREQUEST,
  '__module__' : 'pet.v1.pet_pb2'
  # @@protoc_insertion_point(class_scope:pet.v1.PutPetRequest)
  })
_sym_db.RegisterMessage(PutPetRequest)

PutPetResponse = _reflection.GeneratedProtocolMessageType('PutPetResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTPETRESPONSE,
  '__module__' : 'pet.v1.pet_pb2'
  # @@protoc_insertion_point(class_scope:pet.v1.PutPetResponse)
  })
_sym_db.RegisterMessage(PutPetResponse)

DeletePetRequest = _reflection.GeneratedProtocolMessageType('DeletePetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPETREQUEST,
  '__module__' : 'pet.v1.pet_pb2'
  # @@protoc_insertion_point(class_scope:pet.v1.DeletePetRequest)
  })
_sym_db.RegisterMessage(DeletePetRequest)

DeletePetResponse = _reflection.GeneratedProtocolMessageType('DeletePetResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPETRESPONSE,
  '__module__' : 'pet.v1.pet_pb2'
  # @@protoc_insertion_point(class_scope:pet.v1.DeletePetResponse)
  })
_sym_db.RegisterMessage(DeletePetResponse)


DESCRIPTOR._options = None

_PETSTORESERVICE = _descriptor.ServiceDescriptor(
  name='PetStoreService',
  full_name='pet.v1.PetStoreService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=604,
  serialized_end=807,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPet',
    full_name='pet.v1.PetStoreService.GetPet',
    index=0,
    containing_service=None,
    input_type=_GETPETREQUEST,
    output_type=_GETPETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PutPet',
    full_name='pet.v1.PetStoreService.PutPet',
    index=1,
    containing_service=None,
    input_type=_PUTPETREQUEST,
    output_type=_PUTPETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeletePet',
    full_name='pet.v1.PetStoreService.DeletePet',
    index=2,
    containing_service=None,
    input_type=_DELETEPETREQUEST,
    output_type=_DELETEPETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PETSTORESERVICE)

DESCRIPTOR.services_by_name['PetStoreService'] = _PETSTORESERVICE

# @@protoc_insertion_point(module_scope)
