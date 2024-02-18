import random
from typing import List

def gen_dataset(size: int) -> List[int]:
    data: List[int] = []
    for _ in range(size):
        rand = random.uniform(0, 1)
        if rand < 0.7:
            data.append(int(random.randint(0, 4)))
        else:
            data.append(int(random.randint(5, 7)))
    return data


def gen_uniform_dataset(size: int) -> List[str]:
    data = []
    for _ in range(size):
        rand = random.uniform(0, 1)
        if rand < 0.7:
            data.append("small")
        else:
            data.append("big")
    return data
