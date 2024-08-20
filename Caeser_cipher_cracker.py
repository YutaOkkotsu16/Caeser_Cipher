import sys

lines = sys.stdin.readlines()

# Remove newline characters and process the input
for key in range(26):

    ref = {i :  chr(97 + i) for i in range(26)}
    rev_rev = {chr(97 + i) : i  for i in range(26)}


    # print(ref)
    # print(rev_rev)
    res = []


    for line in lines:
        for letter in line:
            if letter in rev_rev:
                temp = ref[(rev_rev[letter] + key)%26]
                res.append(temp)
            else:
                res.append(letter)


    print(''.join(res))

            
        

