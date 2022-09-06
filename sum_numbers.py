j = 7
#j = j + 3 # 10 lesz
j += 3 # növeljük a j változó értékét 3-mal

# Add össze az első tíz egész számot!
# 1 + 2 + 3 + ... + 10
sum = 0
for i in range(1, 11):
    #sum += i
    sum = sum + i
print(sum)