substr = input()
string = input()
n = len(string)
m = len(substr)
idx = []
cnt = 0

#проверям меньше ли подстрока строки в которой мы пытаемся найти ее
if m > n:
	print("substring longer than string")
	exit(0)

#создаем массив степеней seed'a (простого числа желательно)
def ppow(seed):
	global ppow
	ppow = [1]
	for i in range(1, max(n, m)):
		ppow.append((pow(seed, i)))

#хеш-функция
def hash(string):
	hash_array = []
	for i in range(len(string)):
		ch = string[i]
		curr = (ord(ch) - 96) * ppow[i]
		if i == 0:
			hash_array.append(curr)
			continue
		hash_array.append((curr + hash_array[i-1]))
	return hash_array

#вывод ответа
def get_ans():
	print(cnt)
	print(' '.join(idx))

ppow(37) #создали массив степеней простого числа 37
hash_string = hash(string) # записали строку в виде хеша
hash_substr = hash(substr)[-1] # здесь храним хеш нашей подстроки

# идем по нашей строке пока не найдем нашу подстроку
for i in range(n-m+1):
	cur_hash = hash_string[m+i-1]
	if i != 0:
		cur_hash = ((cur_hash - hash_string[i-1])) // ppow[i]
	# если находим, то добавляем ее индекс в idx и прибавляем к счётчику 1
	if cur_hash == hash_substr:
		cnt += 1
		idx.append(str(i+1))

# выводим ответ
get_ans()