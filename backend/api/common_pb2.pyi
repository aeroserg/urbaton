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

class EducationYear(_message.Message):
    __slots__ = ["education_year"]
    EDUCATION_YEAR_FIELD_NUMBER: _ClassVar[int]
    education_year: int
    def __init__(self, education_year: _Optional[int] = ...) -> None: ...

class Students(_message.Message):
    __slots__ = ["first_name", "last_name", "id"]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    id: int
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class Classes(_message.Message):
    __slots__ = ["class_name", "students"]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    STUDENTS_FIELD_NUMBER: _ClassVar[int]
    class_name: str
    students: _containers.RepeatedCompositeFieldContainer[Students]
    def __init__(self, class_name: _Optional[str] = ..., students: _Optional[_Iterable[_Union[Students, _Mapping]]] = ...) -> None: ...

class GradeFullInfo(_message.Message):
    __slots__ = ["grade", "classes"]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    grade: int
    classes: _containers.RepeatedCompositeFieldContainer[Classes]
    def __init__(self, grade: _Optional[int] = ..., classes: _Optional[_Iterable[_Union[Classes, _Mapping]]] = ...) -> None: ...

class Grades(_message.Message):
    __slots__ = ["grade_full_info"]
    GRADE_FULL_INFO_FIELD_NUMBER: _ClassVar[int]
    grade_full_info: _containers.RepeatedCompositeFieldContainer[GradeFullInfo]
    def __init__(self, grade_full_info: _Optional[_Iterable[_Union[GradeFullInfo, _Mapping]]] = ...) -> None: ...

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

class GetEducationYearRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetEducationYearResponse(_message.Message):
    __slots__ = ["education_years"]
    EDUCATION_YEARS_FIELD_NUMBER: _ClassVar[int]
    education_years: _containers.RepeatedCompositeFieldContainer[EducationYear]
    def __init__(self, education_years: _Optional[_Iterable[_Union[EducationYear, _Mapping]]] = ...) -> None: ...

class GetStudentsRequest(_message.Message):
    __slots__ = ["login"]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    login: str
    def __init__(self, login: _Optional[str] = ...) -> None: ...

class GetStudentsResponse(_message.Message):
    __slots__ = ["grades"]
    GRADES_FIELD_NUMBER: _ClassVar[int]
    grades: _containers.RepeatedCompositeFieldContainer[Grades]
    def __init__(self, grades: _Optional[_Iterable[_Union[Grades, _Mapping]]] = ...) -> None: ...
