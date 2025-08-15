import random
from typing import List, Optional

def number_generate(n: int = 10, low:int = 1, high: int = 20, 
                    seed:Optional[int] = None) -> List[int]:
    if seed is not None:
        random.seed(seed)
        return [random.randint(low, high) for  _ in range(n)]


def below_10_list(nums: List[int]) -> List[int]:
    return list(filter(lambda x:x<10, nums))


def under_10_fil(nums: List[int]) -> List[int]:
    return list(filter(lambda x:x <10, nums))

if __name__ == "__main__":
    number = number_generate(seed=42)

    print(f"Numbers: {number}")
    print(f"Below 10 List Comprehension : {below_10_list(number)}")
    print(f"Below 10 filter: {under_10_fil(number)}")

    
