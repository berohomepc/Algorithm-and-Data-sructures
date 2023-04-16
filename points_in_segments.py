def bubble_sort(array):

	n = len(array)
	swap_flag = False

	for i in range(0, n):
		for j in range(0, n-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				swap_flag = True
		if not swap_flag:
			return array
	return array


def partition(array, l, r):

    pivot = array[r]
    end_border = l - 1

    for i in range(l, r):
        if array[i] <= pivot:
            end_border = end_border + 1
            array[end_border], array[i] = array[i], array[end_border]
    array[end_border + 1], array[r] = array[r], array[end_border + 1]
    return i + 1
 
def quick_sort(array, l, r):
    if l < r:
        pi = partition(array, l, r)
        quick_sort(array, l, pi - 1)
        quick_sort(array, pi + 1, r)
 


n, m = map(int, input().split())

X = [] # массив с началами отрезками
Y = [] # массив с концами отрезков

for i in range(n):
	x, y = map(int, input().split())
	X.append(x)
	Y.append(y)

# массив точек
points = list(map(int, input().split()))

# сортим для удобного поиска  
quick_sort(X, 0, n - 1)
quick_sort(Y, 0, n - 1)

# бин.поиск количества отрезков, начинающихся до или в заданной точке 
def f1(a):
	ans = -1
	l = 0
	r = n - 1
	while l <= r:
		mid = (l + r) // 2
		if X[mid] <= a:
			l = mid + 1
			ans = mid
		else:
			r = mid - 1
	return ans + 1

# бин.поиск количества отрезков, заканчивающихся до заданной точки 
def f2(a):
	ans = -1
	l = 0
	r = n - 1
	while l <= r:
		mid = (l + r) // 2
		if Y[mid] < a:
			l = mid + 1
			ans = mid
		else:
			r = mid - 1
	return ans + 1


ans = list()

#
for i in points:
	N = f1(i)
	M = f2(i)
	ans.append(str(N-M)) # количество отрезков в точке = количеству отрезков, начало которых левее точки и конец не левее 

print(" ".join(ans))