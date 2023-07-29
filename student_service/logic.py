import motor.motor_asyncio as motor


class DB:
    def __init__(self):
        self.client = motor.AsyncIOMotorClient('mongodb://mongodb:27017')
        self.document = None

    async def do_insert(self, value: dict):
        result = await self.client['test'].insert(value)
        self.document = value
        print('inserted: {}'.format(repr(result.inserted_id)))

    async def do_find(self, key):
        document = await self.client['test'].find_one(key)
        return document
