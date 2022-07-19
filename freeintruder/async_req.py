import asyncio

from aiohttp import ClientSession

def main(total_reqs,max_concurrent,delay,redir):    
    
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(total_reqs,max_concurrent,delay,redir))
    res = loop.run_until_complete(future)
    return res
    
async def bound_fetch(sem, req, session,delay,redir):
    # Getter function with semaphore.
    async with sem:
        await asyncio.sleep(delay)
        return await fetch(req, session,redir)

async def fetch(req,session,redir):
    
    req["req"]["ssl"] = req["req"].pop("verify")
    if req["req"]["auth"] == ():
        req["req"]["auth"] = None
    async with session.request(**req["req"],allow_redirects=redir) as response:
        response_body = await response.read()
        
        return {"res":response_body,"status":response.status,"payload":req["payload"],"position":req["position"]}
        
async def run(requests,concurrent,delay,redir):
    tasks = []
    sem = asyncio.Semaphore(concurrent)
    
    async with ClientSession() as session:
        for req in requests:
            task = asyncio.ensure_future(bound_fetch(sem,req,session,delay,redir))
            
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        
        return responses
    
