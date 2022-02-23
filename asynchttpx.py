import asyncio
from asyncio import tasks
import httpx
import time
import json

start_time = time.time()
all_data = []

async def users():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://jsonplaceholder.typicode.com/users')
        print(r.text)

async def post():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://jsonplaceholder.typicode.com/posts')
        print(r.text)

async def todos():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://jsonplaceholder.typicode.com/todos')
        print(r.text)

async def albums():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://jsonplaceholder.typicode.com/albums')
        print(r.text)

async def comments():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://jsonplaceholder.typicode.com/comments')
        print(r.text)

async def photos():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://jsonplaceholder.typicode.com/photos')
        print(r.text)

asyncio.run(users())
asyncio.run(post())
asyncio.run(todos())
asyncio.run(albums())
asyncio.run(comments())
asyncio.run(photos())

end_time = time.time() - start_time
print(f'\n Execution time: {end_time} seconds')