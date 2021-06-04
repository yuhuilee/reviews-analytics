data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  #count = count + 1
		if count % 1000 == 0: # %用來求餘數，意旨當count/1000餘數為0
			print(len(data))
print("檔案讀取完了，總共有", len(data), "筆資料")

#算出這1000000筆留言的平均長度
sum_len = 0 #總留言長度
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d) 
print('留言的平均長度為', sum_len / len(data))	# 總長度/留言筆數1000000

