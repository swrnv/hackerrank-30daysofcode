import sys

s = input().strip()
try:
    k=int(s)
    print(s)
except BaseException as error:
    print('Bad String')