from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class School(_message.Message):
    __slots__ = ["id", "name", "email", "phone_number", "address"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    phone_number: str
    address: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class Class(_message.Message):
    __slots__ = ["class_name"]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    class_name: str
    def __init__(self, class_name: _Optional[str] = ...) -> None: ...

class SchoolsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SchoolsResponse(_message.Message):
    __slots__ = ["schools"]
    SCHOOLS_FIELD_NUMBER: _ClassVar[int]
    schools: _containers.RepeatedCompositeFieldContainer[School]
    def __init__(self, schools: _Optional[_Iterable[_Union[School, _Mapping]]] = ...) -> None: ...

class GetClassRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetClassResponse(_message.Message):
    __slots__ = ["classes"]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    classes: _containers.RepeatedCompositeFieldContainer[Class]
    def __init__(self, classes: _Optional[_Iterable[_Union[Class, _Mapping]]] = ...) -> None: ...
