data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  #count = count + 1
		if count % 1000 == 0: # %用來求餘數，意旨當count/1000餘數為0
			print(len(data))
print(len(data))

print(data[0])
print('-------------')
print(data[1])
