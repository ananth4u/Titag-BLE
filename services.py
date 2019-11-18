import asyncio
import platform

from bleak import BleakClient


async def print_services(mac_addr: str, loop: asyncio.AbstractEventLoop):
    async with BleakClient(mac_addr, loop=loop) as client:
        svcs = await client.get_services()
        print("Services:", svcs)


mac_addr = (
    "54:6c:0e:00:00:78:f0:01"
    if platform.system() != "Darwin"
    else "F0B466FF-9095-4A72-980F-81395EBD3E4D"
)
loop = asyncio.get_event_loop()
loop.run_until_complete(print_services(mac_addr, loop))