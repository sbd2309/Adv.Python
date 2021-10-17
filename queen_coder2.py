n = int(input())
lseries = [0, 0]
leven = []
lodd = []
for i in range(2, 50, 2):
    leven.append(i)

for i in range(1, 50, 2):
    lodd.append(i)

count = 0
# print(lodd)
# print(leven)
while count < len(leven):
    lseries.append(leven[count])
    lseries.append(lodd[count])
    count += 1

# print(lseries)
print(lseries[n - 1])
