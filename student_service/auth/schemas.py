from pydantic import BaseModel


class RegisteredUser:
    phone_number: str
    link: str
