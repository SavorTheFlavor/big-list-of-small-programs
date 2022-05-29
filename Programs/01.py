def vowels(string):
    count = 0
    for letter in string:
        if letter in 'aeiouAEIOU':
            count += 1
    print(f'There are {count} vowels in \"{string}\"')

vowels('I\'m case insensitive')