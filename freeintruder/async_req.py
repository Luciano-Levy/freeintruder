import asyncio

from aiohttp import ClientSession

def main(total_reqs,max_concurrent,delay):    
    
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(total_reqs,max_concurrent,delay))
    loop.run_until_complete(future)

async def bound_fetch(sem, req, session,delay):
    # Getter function with semaphore.
    async with sem:
        asyncio.sleep(delay)
        await fetch(req, session)

async def fetch(req,session):
    
    req["ssl"] = req.pop("verify")
    if req["auth"] == ():
        req["auth"] = None
    async with session.request(**req) as response:
        response = await response.read()
        print(response)

async def run(requests,concurrent,delay):
    tasks = []
    sem = asyncio.Semaphore(concurrent)
    
    async with ClientSession() as session:
        for req in requests:
            task = asyncio.ensure_future(bound_fetch(sem,req,session,delay))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses

