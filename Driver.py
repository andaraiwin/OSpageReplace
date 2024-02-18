import random
from typing import List


def gen_dataset(size: int) -> List[str]:
    data = []
    for i in range(size):
        data.append(str(random.randint(0, 10)))
    return data
