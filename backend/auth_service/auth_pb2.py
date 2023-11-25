# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\"/\n\x0cLoginRequest\x12\x10\n\x08password\x18\x01 \x01(\t\x12\r\n\x05login\x18\x02 \x01(\t\"4\n\rLoginResponse\x12\x0f\n\x07role_id\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\"\x1e\n\rHeaderRequest\x12\r\n\x05login\x18\x01 \x01(\t\"4\n\x0eHeaderResponse\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\t\"\x85\x01\n\x13RegisterUserRequest\x12\x14\n\x0c\x63urrent_user\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\"H\n\x14RegisterUserResponse\x12\x14\n\x0cuser_created\x18\x01 \x01(\x08\x12\x1a\n\x12\x65mail_send_to_user\x18\x02 \x01(\x08\"q\n\x15RegisterSchoolRequest\x12\x14\n\x0c\x63urrent_user\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\"N\n\x16RegisterSchoolResponse\x12\x16\n\x0eschool_created\x18\x01 \x01(\x08\x12\x1c\n\x14\x65mail_send_to_school\x18\x02 \x01(\x08\x32\xe0\x01\n\x0b\x41uthService\x12&\n\x05Login\x12\r.LoginRequest\x1a\x0e.LoginResponse\x12)\n\x06Header\x12\x0e.HeaderRequest\x1a\x0f.HeaderResponse\x12;\n\x0cRegisterUser\x12\x14.RegisterUserRequest\x1a\x15.RegisterUserResponse\x12\x41\n\x0eRegisterSchool\x12\x16.RegisterSchoolRequest\x1a\x17.RegisterSchoolResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LOGINREQUEST']._serialized_start=14
  _globals['_LOGINREQUEST']._serialized_end=61
  _globals['_LOGINRESPONSE']._serialized_start=63
  _globals['_LOGINRESPONSE']._serialized_end=115
  _globals['_HEADERREQUEST']._serialized_start=117
  _globals['_HEADERREQUEST']._serialized_end=147
  _globals['_HEADERRESPONSE']._serialized_start=149
  _globals['_HEADERRESPONSE']._serialized_end=201
  _globals['_REGISTERUSERREQUEST']._serialized_start=204
  _globals['_REGISTERUSERREQUEST']._serialized_end=337
  _globals['_REGISTERUSERRESPONSE']._serialized_start=339
  _globals['_REGISTERUSERRESPONSE']._serialized_end=411
  _globals['_REGISTERSCHOOLREQUEST']._serialized_start=413
  _globals['_REGISTERSCHOOLREQUEST']._serialized_end=526
  _globals['_REGISTERSCHOOLRESPONSE']._serialized_start=528
  _globals['_REGISTERSCHOOLRESPONSE']._serialized_end=606
  _globals['_AUTHSERVICE']._serialized_start=609
  _globals['_AUTHSERVICE']._serialized_end=833
# @@protoc_insertion_point(module_scope)
