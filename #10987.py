import sys

vowel = ["a","e","i","o","u"]

str = input()
cnt = 0

for i in str:
    if i in vowel:
        cnt += 1
print(cnt)
