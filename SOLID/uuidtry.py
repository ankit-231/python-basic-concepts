import random

a = random.getrandbits(124)

b = hex(a)

c = b[2:]



def count_string(string: str) -> int:
    return len(string)

print(count_string(c))
print(c)

print("custom uuid4", f"{c[:8]}-{c[8:12]}-4{c[12:15]}-{c[15:19]}-{c[19:]}")

import uuid

print(uuid.uuid4())