import asyncio
import aiohttp
import time

urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]

async def fetch(session, url):
    async with session.get(url) as response:
        return response.status

async def crawler():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

start = time.time()
print(asyncio.run(crawler()))
print("Time:", time.time() - start)
