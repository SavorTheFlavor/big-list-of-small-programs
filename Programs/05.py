import random

def int_to_timestamp(number: int = random.randint(1, 1000)):
    hh = number // 3600
    mm = (number - hh*3600)//60
    ss = ((number - hh*3600) - mm*60)
    return f"{hh}:{mm}:{ss}"

# example
int_to_timestamp()
print(int_to_timestamp())
print(int_to_timestamp(1000))