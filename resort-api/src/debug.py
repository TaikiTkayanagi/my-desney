
from src import app
import asyncio


async def main():
	print(await app.land_waiting())


asyncio.run(main())