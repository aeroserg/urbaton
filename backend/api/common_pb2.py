# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\"X\n\x06School\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\"\x1b\n\x05\x43lass\x12\x12\n\nclass_name\x18\x01 \x01(\t\"\'\n\rEducationYear\x12\x16\n\x0e\x65\x64ucation_year\x18\x01 \x01(\x05\"=\n\x08Students\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\":\n\x07\x43lasses\x12\x12\n\nclass_name\x18\x01 \x01(\t\x12\x1b\n\x08students\x18\x02 \x03(\x0b\x32\t.Students\"9\n\rGradeFullInfo\x12\r\n\x05grade\x18\x01 \x01(\x05\x12\x19\n\x07\x63lasses\x18\x02 \x03(\x0b\x32\x08.Classes\"1\n\x06Grades\x12\'\n\x0fgrade_full_info\x18\x01 \x03(\x0b\x32\x0e.GradeFullInfo\"\x10\n\x0eSchoolsRequest\"+\n\x0fSchoolsResponse\x12\x18\n\x07schools\x18\x01 \x03(\x0b\x32\x07.School\"\x11\n\x0fGetClassRequest\"+\n\x10GetClassResponse\x12\x17\n\x07\x63lasses\x18\x01 \x03(\x0b\x32\x06.Class\"\x19\n\x17GetEducationYearRequest\"C\n\x18GetEducationYearResponse\x12\'\n\x0f\x65\x64ucation_years\x18\x01 \x03(\x0b\x32\x0e.EducationYear\"#\n\x12GetStudentsRequest\x12\r\n\x05login\x18\x01 \x01(\t\".\n\x13GetStudentsResponse\x12\x17\n\x06grades\x18\x01 \x03(\x0b\x32\x07.Grades2\xf1\x01\n\rCommonService\x12,\n\x07Schools\x12\x0f.SchoolsRequest\x1a\x10.SchoolsResponse\x12/\n\x08GetClass\x12\x10.GetClassRequest\x1a\x11.GetClassResponse\x12G\n\x10GetEducationYear\x12\x18.GetEducationYearRequest\x1a\x19.GetEducationYearResponse\x12\x38\n\x0bGetStudents\x12\x13.GetStudentsRequest\x1a\x14.GetStudentsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SCHOOL']._serialized_start=16
  _globals['_SCHOOL']._serialized_end=104
  _globals['_CLASS']._serialized_start=106
  _globals['_CLASS']._serialized_end=133
  _globals['_EDUCATIONYEAR']._serialized_start=135
  _globals['_EDUCATIONYEAR']._serialized_end=174
  _globals['_STUDENTS']._serialized_start=176
  _globals['_STUDENTS']._serialized_end=237
  _globals['_CLASSES']._serialized_start=239
  _globals['_CLASSES']._serialized_end=297
  _globals['_GRADEFULLINFO']._serialized_start=299
  _globals['_GRADEFULLINFO']._serialized_end=356
  _globals['_GRADES']._serialized_start=358
  _globals['_GRADES']._serialized_end=407
  _globals['_SCHOOLSREQUEST']._serialized_start=409
  _globals['_SCHOOLSREQUEST']._serialized_end=425
  _globals['_SCHOOLSRESPONSE']._serialized_start=427
  _globals['_SCHOOLSRESPONSE']._serialized_end=470
  _globals['_GETCLASSREQUEST']._serialized_start=472
  _globals['_GETCLASSREQUEST']._serialized_end=489
  _globals['_GETCLASSRESPONSE']._serialized_start=491
  _globals['_GETCLASSRESPONSE']._serialized_end=534
  _globals['_GETEDUCATIONYEARREQUEST']._serialized_start=536
  _globals['_GETEDUCATIONYEARREQUEST']._serialized_end=561
  _globals['_GETEDUCATIONYEARRESPONSE']._serialized_start=563
  _globals['_GETEDUCATIONYEARRESPONSE']._serialized_end=630
  _globals['_GETSTUDENTSREQUEST']._serialized_start=632
  _globals['_GETSTUDENTSREQUEST']._serialized_end=667
  _globals['_GETSTUDENTSRESPONSE']._serialized_start=669
  _globals['_GETSTUDENTSRESPONSE']._serialized_end=715
  _globals['_COMMONSERVICE']._serialized_start=718
  _globals['_COMMONSERVICE']._serialized_end=959
# @@protoc_insertion_point(module_scope)
