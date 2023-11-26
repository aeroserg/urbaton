from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ["text", "first_name_from", "last_name_from"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FROM_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FROM_FIELD_NUMBER: _ClassVar[int]
    text: str
    first_name_from: str
    last_name_from: str
    def __init__(self, text: _Optional[str] = ..., first_name_from: _Optional[str] = ..., last_name_from: _Optional[str] = ...) -> None: ...

class SendMessageRequest(_message.Message):
    __slots__ = ["text", "login_from", "id_to"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LOGIN_FROM_FIELD_NUMBER: _ClassVar[int]
    ID_TO_FIELD_NUMBER: _ClassVar[int]
    text: str
    login_from: str
    id_to: int
    def __init__(self, text: _Optional[str] = ..., login_from: _Optional[str] = ..., id_to: _Optional[int] = ...) -> None: ...

class SendMessageResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetMessageRequest(_message.Message):
    __slots__ = ["login"]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    login: str
    def __init__(self, login: _Optional[str] = ...) -> None: ...

class GetMessageResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    def __init__(self, messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ...) -> None: ...
