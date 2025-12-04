# https://adventofcode.com/2025/day/1
from input_fetcher import fetch_input

def secret_entrance(input):
    pos = 50
    count = 0
    
    for line in input.splitlines():
        dir = line[0]
        num = int(line[1:])
        
        mod = 1 if dir == "R" else -1
        
        pos += (num * mod)
        
        if pos % 100 == 0:
            count += 1
            
    return count

ans = secret_entrance(fetch_input(1))
print(ans)
