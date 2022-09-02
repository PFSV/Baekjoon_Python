import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
third = sys.stdin.readline().strip()

resis_value = {
    "black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,
    "blue":6,"violet":7,"grey":8,"white":9
}

result = (10*resis_value[first] + resis_value[second]) * 10**(resis_value[third])

print(result)