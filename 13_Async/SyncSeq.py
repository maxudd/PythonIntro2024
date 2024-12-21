import asyncio
import random

class Seq:
    _counter = 0
    _events = {}  

    def __init__(self, name):
        self.name = name
        self._id = Seq._counter  
        Seq._counter += 1
        Seq._events[self._id] = asyncio.Event()  
        if self._id == 0:
            Seq._events[self._id].set()  

    async def run(self):
        await Seq._events[self._id].wait()  
        print(self.name)  
        if (next_id := self._id + 1) in Seq._events:
            Seq._events[next_id].set()  
        return self.name
            
# async def main(*names):
#     seq = [Seq(name) for name in names]
#     seq.sort(key=lambda x: x.name % 17)
#     shnames = [s.name for s in seq]
#     result = await asyncio.gather(*(s.run() for s in seq))
#     print(names != shnames == result)


# asyncio.run(main(*range(100, 2000)))