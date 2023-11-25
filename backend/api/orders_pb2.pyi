from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EducationOrderParent(_message.Message):
    __slots__ = ["first_name", "last_name", "email", "phone_number", "school_id"]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SCHOOL_ID_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    phone_number: str
    school_id: int
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., school_id: _Optional[int] = ...) -> None: ...

class EducationOrderStudent(_message.Message):
    __slots__ = ["first_name", "last_name", "email", "phone_number", "school_id"]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SCHOOL_ID_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    phone_number: str
    school_id: int
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., school_id: _Optional[int] = ...) -> None: ...

class EducationOrderRequest(_message.Message):
    __slots__ = ["parent_order", "student_order"]
    PARENT_ORDER_FIELD_NUMBER: _ClassVar[int]
    STUDENT_ORDER_FIELD_NUMBER: _ClassVar[int]
    parent_order: _containers.RepeatedCompositeFieldContainer[EducationOrderParent]
    student_order: _containers.RepeatedCompositeFieldContainer[EducationOrderStudent]
    def __init__(self, parent_order: _Optional[_Iterable[_Union[EducationOrderParent, _Mapping]]] = ..., student_order: _Optional[_Iterable[_Union[EducationOrderStudent, _Mapping]]] = ...) -> None: ...

class EducationOrderResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
