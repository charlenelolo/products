# 確認檔案室否在電腦中
import os # operating system
products = []
if os.path.isfile('products.csv'):
	print('找到檔案')
	with open('products.csv','r',encoding = 'utf-8') as f:
		for line in f:
			if '商品, 價格' in line:
				continue                      # for loop 跳到下一回合
			name, price = line.strip().split(',')   # .strip()去掉換行符號(\n)
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')

# 請使用者輸入產品價格資訊
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


# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])


# 寫入csv, 且用世界通用的編碼寫入
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')