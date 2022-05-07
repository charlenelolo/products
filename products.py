# 請使用者輸入產品價格資訊
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	# p = []
	# p.append(name)
	# p.append(price)
	products.append([name, price])
print(products)


# 看每一個價格
for p in products:
	print(p[0], '的價格是', p[1])


# 寫入text
with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

# 寫入csv
with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')