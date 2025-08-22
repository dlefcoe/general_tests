import asyncio



async def periodic_second():
    while True:
        print('periodic second')
        await asyncio.sleep(0.75) #you can put 900 seconds = 15mins


async def periodic():
    while True:
        print('periodic')
        await asyncio.sleep(1) #you can put 900 seconds = 15mins
        print('doing more bits of the code')

def stop():
    task_1.cancel()
    task_2.cancel()
    print('both tasks stopped')

loop = asyncio.get_event_loop()
loop.call_later(5, stop) #increase end time as per your requirement
task_1 = loop.create_task(periodic())
task_2 = loop.create_task(periodic_second())

print('hello world')

try:
    loop.run_until_complete(task_1)
    loop.run_until_complete(task_2)

except asyncio.CancelledError:
    pass



