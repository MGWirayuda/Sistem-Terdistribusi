import asyncio

async def sett():
    print("log1")
    await asyncio.sleep(2)
    print("log2")

async def main():
    await asyncio.gather(sett(),sett())

asyncio.run(main())