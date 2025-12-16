
from src import app
import asyncio


async def main():
	print(await app.attractions_waiting("sea","2025-12-16 12:10"))


asyncio.run(main())