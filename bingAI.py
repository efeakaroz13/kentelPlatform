import asyncio

from sydney import SydneyClient


async def generate(prompt):
    async with SydneyClient() as sydney:
        out = ""
        async for response in sydney.ask_stream(prompt):
                out +=response 

        return out 



if __name__ == "__main__":
    asyncio.run(generate(prompt="what is torque?"))