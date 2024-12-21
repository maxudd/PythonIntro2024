"""
Одномерная аркада

https://uneex.org/LecturesCMC/PythonIntro2024/Homework_OneDArcade
"""

import asyncio


class Monster:
    def __init__(self, *spec):
        self.name, self.pos, self.delay, self.strength = spec

    async def run(self, episode_start, episode_end):
        event_count = 0
        while True:
            await episode_start.wait()
            event_count += 1
            if event_count % self.delay == 0:
                self.pos += 1
            await episode_end.wait()


async def game(monsters, episode_start, episode_end, epochs):
    alives = len(monsters)
    deads = 0
    for _ in range(epochs):
        await episode_start.wait()
        await episode_end.wait()

        poses = list(map(lambda x: x.pos, monsters))
        fight_pos = min(poses)
        max_pos = max(poses)
        while fight_pos <= max_pos:
            fighters = [x for x in
                        monsters if x.strength and x.pos == fight_pos][:2]
            if len(fighters) == 2:
                fighter1, fighter2 = fighters

                damage = min(fighter1.strength, fighter2.strength)
                fighter1.strength -= damage
                fighter2.strength -= damage
                if fighter2.strength == 0:
                    alives -= 1
                    deads += 1
                if fighter1.strength == 0:
                    alives -= 1
                    deads += 1
                break
            else:
                fight_pos += 1
        else:
            continue

        if alives == 1:
            break
        if alives == 0:
            return "All dead"

    if all(monster.strength for monster in monsters):
        return "All flee"
    return ", ".join(monster.name for monster in monsters if monster.strength)
