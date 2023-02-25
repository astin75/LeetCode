class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        output = c = 0
        for i in tokens:
            if i == "*":
                b = numbers.pop()
                a = numbers.pop()
                c = a * b
                output = c
                numbers.append(int(c))
            elif i == "+":
                b = numbers.pop()
                a = numbers.pop()
                c = a + b
                output = c
                numbers.append(int(c))
            elif i == "/":
                b = numbers.pop()
                a = numbers.pop()
                c = a / b
                output = c
                numbers.append(int(c))
            elif i == "-":
                b = numbers.pop()
                a = numbers.pop()
                c = a - b
                output = c
                numbers.append(int(c))                                    
            else:
                numbers.append(int(i))
                
        return numbers.pop()      
        