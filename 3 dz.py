import random

class calculator:
    def __init__(self, *nums):
        self.numbers = nums
        self.result = self._calculate()

    def _calculate(self):
        result = self.numbers[0]
        
        for num in self.numbers[1:]:
            operation = random.choice(['+', '-', '*', '/'])
            
            if operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/' and num != 0: 
                result /= num
        
        return result

    def __str__(self):
        return f"Результат: {self.result}"


oop = calculator(10, 5, 3)
print(oop) 