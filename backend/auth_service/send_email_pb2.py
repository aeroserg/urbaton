# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_email.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10send_email.proto\"N\n\x10SendEmailRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x18\n\x10\x65mail_address_to\x18\x03 \x01(\t\"$\n\x11SendEmailResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x46\n\x10SendEmailService\x12\x32\n\tSendEmail\x12\x11.SendEmailRequest\x1a\x12.SendEmailResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'send_email_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SENDEMAILREQUEST']._serialized_start=20
  _globals['_SENDEMAILREQUEST']._serialized_end=98
  _globals['_SENDEMAILRESPONSE']._serialized_start=100
  _globals['_SENDEMAILRESPONSE']._serialized_end=136
  _globals['_SENDEMAILSERVICE']._serialized_start=138
  _globals['_SENDEMAILSERVICE']._serialized_end=208
# @@protoc_insertion_point(module_scope)
