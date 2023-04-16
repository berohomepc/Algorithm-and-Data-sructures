#postfix_calculator

class PostfixCalculator():
	def __init__(self):
		self.operators = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 4}
		self.infix_form = ""
		self.postfix_form = ""
		self.answer = None

	#конвертируем инфиксную форму в постфиксную 
	def __to_postfix(self, infix_expr):
		stack = list()
		postfix_expr = ""
		num = ""
		for i in range(len(infix_expr)):
			#парсим числа
			if (infix_expr[i].isdigit() or infix_expr[i] == "."):
				num += infix_expr[i]
			elif num != "" and not infix_expr[i].isdigit():
				postfix_expr += num + " "
				num = ""	

			#если встречаем левую скобку, заносим в стек
			if infix_expr[i] == "(":
				stack.append(infix_expr[i])

			#если встречаем правую скобку, выгружаем всё из стека до левой скобки
			elif infix_expr[i] == ")":
				while len(stack) > 0 and stack[-1] != "(":
						postfix_expr += stack.pop()
				#удаляем левую скобку
				stack.pop()

			#если встречаем оператор
			elif infix_expr[i] in self.operators:
				op = infix_expr[i]

				#проверяем является ли он унарным минусом, если да то заменяем его на '~'
				if op == '-' and (i == 0 or (i > 1 and (infix_expr[i-1] in self.operators))):
					op = '~'
				#выгружаем из стека все операторы, приоритет которых больше или равен текущему оператору
				while(len(stack) > 0 and (self.operators[stack[-1]] >= self.operators[op])):
					postfix_expr += stack.pop()	
				#добавляем текущий оператор в стек
				stack.append(op)

		#выгружаем остатки из стека
		for i in range(len(stack)):
			postfix_expr += stack.pop()
		return postfix_expr


	def __bin_solve(self, op, l, r):
 		if op == "+":
 			return l + r 
 		elif op == "-":
 			return l - r
 		elif op == "*":
 			return l * r
 		elif op == "/":
 			return l / r
 		elif op == "^":
 			return l ** r

 	#решаем полученное постфиксное выражение
	def __solve(self, postfix_expr):
		stack = list()
		num = ""

		for ch in postfix_expr:
			#парсим число и заносим его в стек
			if (ch.isdigit() or ch == "."):
				num += ch
			else:
				if len(num) > 0:
					stack.append(float(num))
					num = ""

			#если встречаем оператор, то смотрим
			if ch in self.operators:
				#если это унарный минус, то делаем операцию [0 - {вершина стека}]
				if ch == '~':
					second = stack.pop() if len(stack) > 0 else 0
					stack.append(self.__bin_solve('-', 0, second))
					print(f"{ch}{second} = {stack[-1]}")
					continue
				#если это не унарный минус, то заносим операнды в second и first из стека и проводим операцию {ch} 
				#и добавляем результат в стек
				second = stack.pop() if len(stack) > 0 else 0
				first = stack.pop() if len(stack) > 0 else 0
				stack.append(self.__bin_solve(ch, first, second))
		return stack

	
	def solver(self, infix_expr):
		self.infix_form = infix_expr
		self.postfix_form = self.__to_postfix(self.infix_form)
		self.answer = self.__solve(self.postfix_form)


calc = PostfixCalculator()
calc.solver("(-5+7)/32+0.15*(9^3-184)")
print(calc.postfix_form)
print(calc.answer)
