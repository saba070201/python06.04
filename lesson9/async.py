import asyncio
import time
async def first():
    print('fs')
    await asyncio.sleep(3)
    print('fe')
async def second():
    print('ss')
    await asyncio.sleep(1)
    print('se')
async def main():
    t1=asyncio.create_task(first())
    t2=asyncio.create_task(second())
    await t1
    await t2
    
asyncio.get_event_loop().run_until_complete(main())