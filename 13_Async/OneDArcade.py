import asyncio

class Monster:
    def __init__(self, *spec):
        self.name, self.pos, self.delay, self.strength = spec
        self.alive = True

    async def run(self, episode_start: asyncio.Barrier, episode_end: asyncio.Barrier):
        event_count = 0
        while True:
            await episode_start.wait()
            event_count += 1
            if event_count % self.delay == 0:
                self.pos += 1
            await episode_end.wait()

async def game(monsters, episode_start, episode_end, epochs):
    # alive_monsters = monsters[:]
    alives = len(monsters)
    deads = 0
    for _ in range(epochs):
        await episode_start.wait()
        # await asyncio.sleep(0)
        await episode_end.wait()

        poses = list(map(lambda x: x.pos, monsters))
        fight_pos = min(poses)
        max_pos = max(poses)
        while fight_pos <= max_pos:
            fighters = [x for x in monsters if x.strength and x.pos == fight_pos][:2]
            if len(fighters) == 2:
                fighter1, fighter2 = fighters

                damage = min(fighter1.strength, fighter2.strength)
                fighter1.strength -= damage
                fighter2.strength -= damage
                if fighter2.strength == 0:
                    # fighter2.alive = False
                    alives -= 1
                    deads += 1
                if fighter1.strength == 0:
                    # fighter1.alive = False
                    alives -= 1
                    deads += 1
                break
            else:
                fight_pos += 1
        else:
            continue

        
        # alive_monsters = [monster for monster in monsters if monster.strength]
        if alives == 1:
            break
        if alives == 0:
            return "All dead"

    if all(monster.strength for monster in monsters):
        return "All flee"
    return ", ".join(monster.name for monster in monsters if monster.strength)

# async def main(*specs):
#     monsters = [Monster(*spec) for spec in specs]
#     animate, freeze = asyncio.Barrier(len(monsters) + 1), asyncio.Barrier(len(monsters) + 1)
#     squad = [asyncio.create_task(m.run(animate, freeze)) for m in monsters]
#     result = await game(monsters, animate, freeze, 1000)
#     _ = [m.cancel() for m in squad]
#     return result


# from random import randint, seed
# seed(1337)
# N, M = 100, 100
# squad = [(f"({i})", 1+i*2, randint(2, 6), randint(1, M)) for i in range(N)]
# squad[0] = "Killer", 1, 1, N*M
# print(asyncio.run(main(*squad)))
