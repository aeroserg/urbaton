from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ["password", "login"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    password: str
    login: str
    def __init__(self, password: _Optional[str] = ..., login: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ["role_id", "first_name"]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    first_name: str
    def __init__(self, role_id: _Optional[str] = ..., first_name: _Optional[str] = ...) -> None: ...

class HeaderRequest(_message.Message):
    __slots__ = ["login"]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    login: str
    def __init__(self, login: _Optional[str] = ...) -> None: ...

class HeaderResponse(_message.Message):
    __slots__ = ["user_name", "role_id"]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    role_id: str
    def __init__(self, user_name: _Optional[str] = ..., role_id: _Optional[str] = ...) -> None: ...

class RegisterUserRequest(_message.Message):
    __slots__ = ["current_user", "first_name", "last_name", "email", "phone_number", "role"]
    CURRENT_USER_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    current_user: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    role: str
    def __init__(self, current_user: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class RegisterUserResponse(_message.Message):
    __slots__ = ["user_created", "email_send_to_user"]
    USER_CREATED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SEND_TO_USER_FIELD_NUMBER: _ClassVar[int]
    user_created: bool
    email_send_to_user: bool
    def __init__(self, user_created: bool = ..., email_send_to_user: bool = ...) -> None: ...

class RegisterSchoolRequest(_message.Message):
    __slots__ = ["current_user", "name", "email", "phone_number", "address"]
    CURRENT_USER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    current_user: str
    name: str
    email: str
    phone_number: str
    address: str
    def __init__(self, current_user: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class RegisterSchoolResponse(_message.Message):
    __slots__ = ["school_created", "email_send_to_school"]
    SCHOOL_CREATED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SEND_TO_SCHOOL_FIELD_NUMBER: _ClassVar[int]
    school_created: bool
    email_send_to_school: bool
    def __init__(self, school_created: bool = ..., email_send_to_school: bool = ...) -> None: ...
