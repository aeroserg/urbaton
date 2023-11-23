from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendEmailRequest(_message.Message):
    __slots__ = ["message", "subject", "email_address_to"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_TO_FIELD_NUMBER: _ClassVar[int]
    message: str
    subject: str
    email_address_to: str
    def __init__(self, message: _Optional[str] = ..., subject: _Optional[str] = ..., email_address_to: _Optional[str] = ...) -> None: ...

class SendEmailResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
