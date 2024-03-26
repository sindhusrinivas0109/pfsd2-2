#import random
"""
n = random.randbytes(4)# generates a random byte value
print(n)

print(random.randrange(1,50))

mylist = ("namjoon", "suga", "jhope", "jin")
mylist1 = {"jungkook", "jimin", "taehyung"} # set wont work for random.choice
mylist2 = ["enhypen","bangtan", "exo" ]
print(random.choice(mylist2))
print(random.shuffle(mylist2))# wont work for tuple and set """

import string
import random
S = 10
ran = ''.join(random.sample(string.ascii_uppercase + string.digits,k = S))
s1 = 4
ran1 = ''.join(random.sample(string.digits,k=6))
print(ran1)
print(ran)