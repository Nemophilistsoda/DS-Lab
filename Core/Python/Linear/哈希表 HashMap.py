nums = [1, 2, 3, 4, 5, 2, 5, 4]
hashmap = {}
for num in nums:
    if num in hashmap:
        hashmap[num] += 1
    else:
        hashmap[num] = 1
print(hashmap)

# 或者你也可以这样写
text = 'apple orange banana apple nanna'
another_hashmap = {}

for word in text.split():
    if word not in another_hashmap:
        another_hashmap[word] = 0
    another_hashmap[word] += 1

print(another_hashmap)