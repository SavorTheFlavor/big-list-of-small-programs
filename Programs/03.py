import random

flips = 1000
flip_outcomes = {
    "Heads x2" : 0,
    "Heads + Tails" : 0,
    "Tails x2" : 0
}
num_dict = {
    0 : "Heads x2",
    1 : "Heads + Tails",
    2 : "Tails x2"
}

for flip in range(flips):
    outcome = random.randint(0,1) + random.randint(0,1)
    flip_outcomes[num_dict[outcome]] += 1

print(f'''
{flips} Outcomes of 2 coin flips
    -------------------------
    | Heads x2 : {format(flip_outcomes["Heads x2"] / flips * 100, '.1f')}%      |
    | Heads + Tails : {format(flip_outcomes["Heads + Tails"] / flips * 100, '.1f')}% |
    | Tails x2 : {format(flip_outcomes["Tails x2"] / flips * 100, '.1f')} %     |
    -------------------------
''')