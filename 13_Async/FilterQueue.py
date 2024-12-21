"""
Вас здесь не стояло!

https://uneex.org/LecturesCMC/PythonIntro2024/Homework_FilterQueue
"""

import asyncio


class FilterQueue(asyncio.Queue):
    def __init__(self, maxsize=0):
        super().__init__(maxsize)

    @property
    def window(self):
        return None if self.empty() else self._queue[0]

    def __contains__(self, filter):
        for q in self._queue:
            if filter(q):
                return True
        return False

    def later(self):
        first = self.get_nowait()
        return self.put_nowait(first)

    async def get(self, filter=lambda a: False):
        if filter in self:
            while True:
                if filter(self.window):
                    return await super().get()
                else:
                    self.later()
        return await super().get()

# async def putter(n, queue):
#     for i in range(n):
#         await queue.put(i)

# async def getter(n, queue, filter):
#     for i in range(n):
#         await asyncio.sleep(0.03)
#         yield await queue.get(filter)

# async def main():
#     queue = FilterQueue(10)
#     asyncio.create_task(putter(20, queue))
#     async for res in getter(20, queue, lambda n: n % 2):
#         print(res)

# asyncio.run(main())
