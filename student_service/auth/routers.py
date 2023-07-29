from fastapi import APIRouter
from auth.logic import Auth
from logic import DB

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)
user = Auth()
# session = DB()


@router.post('/register/')
async def register_user(number: str) -> dict:
    link = await user.register(number)
    data = {'phone_number': number, 'link': link}
    # await session.do_insert(data)
    return data


@router.get('/login/')
async def login_user(code: str) -> None:
    return await user.login(code)
