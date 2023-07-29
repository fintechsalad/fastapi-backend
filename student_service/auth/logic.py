import pyotp

from config import AUTH_SECRET_KEY


class Auth:

    def __init__(self):
        self.phone_num = None
        self.totp = None

    async def register(self, phone_num):
        if not phone_num:
            return 'Enter correct phone number'
        else:
            self.phone_num = phone_num
            link = pyotp.totp.TOTP(AUTH_SECRET_KEY).provisioning_uri(name=self.phone_num, issuer_name='Secure app')
            self.totp = pyotp.TOTP(AUTH_SECRET_KEY)
            return link

    async def login(self, code):
        if self.totp is None:
            return 'You are not registered yet'
        elif self.totp.now() != code:
            print(self.totp.now())
            return 'Wrong qr_code'
        return True
