"""
Store decoded packets for processing later.
"""

import asyncio
from datetime import datetime
from io import TextIOBase
from os import rename,system

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 30003  # The port used by the server

async def test():
    reader, _ = await asyncio.open_connection(HOST, PORT)
    prev_filename = None
    file: TextIOBase = None
    while True:
        message = (await reader.readline()).decode().strip()
        filename = "data/bst/"+datetime.now().strftime("%Y%m%d-%H")+".bst.temp"
        if prev_filename != filename:
            if file: 
                file.flush()
                file.close()
                file.__exit__()
                del(file)
                rename(prev_filename, ".".join(prev_filename.split(".")[:-1]))
                system(f"gzip -9 {'.'.join(prev_filename.split('.')[:-1])}")
            file = open(filename, "w")
            prev_filename = filename
        file.write(f"{message}\n")
                
asyncio.run(test())
