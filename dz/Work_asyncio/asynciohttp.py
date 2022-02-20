import asyncio
import aiohttp
from asyncio import tasks
from pip import main
import httpx
import time

### id =1
urls = ['https://jsonplaceholder.typicode.com/users/1/posts', 
        'https://jsonplaceholder.typicode.com/users/1/todos',
        'https://jsonplaceholder.typicode.com/users/1/albums',
        'https://jsonplaceholder.typicode.com/posts/1/comments',
        'https://jsonplaceholder.typicode.com/albums/1/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 2
urls = ['https://jsonplaceholder.typicode.com/users/2/posts', 
        'https://jsonplaceholder.typicode.com/users/2/todos',
        'https://jsonplaceholder.typicode.com/users/2/albums',
        'https://jsonplaceholder.typicode.com/posts/2/comments',
        'https://jsonplaceholder.typicode.com/albums/2/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 3
urls = ['https://jsonplaceholder.typicode.com/users/3/posts', 
        'https://jsonplaceholder.typicode.com/users/3/todos',
        'https://jsonplaceholder.typicode.com/users/3/albums',
        'https://jsonplaceholder.typicode.com/posts/3/comments',
        'https://jsonplaceholder.typicode.com/albums/3/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 4
urls = ['https://jsonplaceholder.typicode.com/users/4/posts', 
        'https://jsonplaceholder.typicode.com/users/4/todos',
        'https://jsonplaceholder.typicode.com/users/4/albums',
        'https://jsonplaceholder.typicode.com/posts/4/comments',
        'https://jsonplaceholder.typicode.com/albums/4/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 5
urls = ['https://jsonplaceholder.typicode.com/users/5/posts', 
        'https://jsonplaceholder.typicode.com/users/5/todos',
        'https://jsonplaceholder.typicode.com/users/5/albums',
        'https://jsonplaceholder.typicode.com/posts/5/comments',
        'https://jsonplaceholder.typicode.com/albums/5/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 6
urls = ['https://jsonplaceholder.typicode.com/users/6/posts', 
        'https://jsonplaceholder.typicode.com/users/6/todos',
        'https://jsonplaceholder.typicode.com/users/6/albums',
        'https://jsonplaceholder.typicode.com/posts/6/comments',
        'https://jsonplaceholder.typicode.com/albums/6/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 7
urls = ['https://jsonplaceholder.typicode.com/users/7/posts', 
        'https://jsonplaceholder.typicode.com/users/7/todos',
        'https://jsonplaceholder.typicode.com/users/7/albums',
        'https://jsonplaceholder.typicode.com/posts/7/comments',
        'https://jsonplaceholder.typicode.com/albums/7/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 8
urls = ['https://jsonplaceholder.typicode.com/users/8/posts', 
        'https://jsonplaceholder.typicode.com/users/8/todos',
        'https://jsonplaceholder.typicode.com/users/8/albums',
        'https://jsonplaceholder.typicode.com/posts/8/comments',
        'https://jsonplaceholder.typicode.com/albums/8/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 9
urls = ['https://jsonplaceholder.typicode.com/users/9/posts', 
        'https://jsonplaceholder.typicode.com/users/9/todos',
        'https://jsonplaceholder.typicode.com/users/9/albums',
        'https://jsonplaceholder.typicode.com/posts/9/comments',
        'https://jsonplaceholder.typicode.com/albums/9/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

###id = 10
urls = ['https://jsonplaceholder.typicode.com/users/10/posts', 
        'https://jsonplaceholder.typicode.com/users/10/todos',
        'https://jsonplaceholder.typicode.com/users/10/albums',
        'https://jsonplaceholder.typicode.com/posts/10/comments',
        'https://jsonplaceholder.typicode.com/albums/10/photos']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))