def compress(string):
    count = 1
    returnstring = ''
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        if (string[i] != string[i-1]) or (i == len(string)-1):
            returnstring += string[i-1]
            if count > 1:
                returnstring += str(count)
            count = 1
    return returnstring

print(compress('dccaaabbbbbcccccc')) #dc2a3b5c6
print(compress('aaaallammmhhh')) #a4l2am3h3