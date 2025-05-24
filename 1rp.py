def count_jewels(J, S):
    jewels = set(J) 
    count = sum(1 for stone in S if stone in jewels)  

J = "abbbbbbbbbA"
S = "aAAaaaaaaabbbb"
result = count_jewels(J, S)
print(result)  