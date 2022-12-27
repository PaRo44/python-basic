import asyncio
import aiohttp


USERS_DATA_URL = "http://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "http://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        data = await response.json()
        return data


async def fetch_api_data(session: aiohttp.ClientSession, urls_list: list[str]) -> list[dict]:
    tasks = []
    for url in urls_list:
        task = asyncio.create_task(fetch_json(session, url))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    return responses


async def get_api_data():
    async with aiohttp.ClientSession() as session:
        return await fetch_api_data(session, [USERS_DATA_URL, POSTS_DATA_URL])
