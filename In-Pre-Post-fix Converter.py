# stack implementation
class Stack:
    def __init__(self):
        self.items = []
  
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if (self.size() == 0):
            raise "Nothing to remove since stack is empty!"
        else:
            return self.items.pop()
    
    def top(self):
      return self.items[-1]

    def isEmpty(self):
      if self.size() == 0:
        return True

    def display(self):
        print(self.items)
        return

    def size(self):
        return len(self.items)
    
# checks if character is an operand
def isOperand(char):
  if char.isalpha():
    return True

# checks if character is an operator
def isOperator(char):
  if char in "+-/*^":
    return True

# checks if op1 has higher precedence than op2
def hasHigherPrecedence(op1, op2):
  precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
  try: 
    prec_op1 = precedence[op1]
    prec_op2 = precedence[op2]
    
    if prec_op1 >= prec_op2:
      return True
    return False

  except KeyError:
    return False

# reverses the expression; used in infix to prefix
def reverse(expression):
  result = ""
  for i in range(len(expression)-1, -1, -1):
    if expression[i] == '(':
      result += ')'
    elif expression[i] == ')':
      result += '('
    else:
      result += expression[i]

  return result

# checks if the expression inputted is valid
def ifValid(expression):
  open_par = close_par = 0
  operator_together = operand_together = False
  
  try:
    for i in range(len(expression)):
      if expression[i] == '(':
        open_par += 1
      elif expression[i] == ')':
        close_par += 1

      if isOperator(expression[i]):
        if isOperator(expression[i+1]):
          operator_together = True

      if isOperand(expression[i]):
        if isOperand(expression[i+1]):
          operand_together = True
  except IndexError:
    pass

  if (open_par == close_par) and (not operator_together) and (not operand_together):
    return True
  return False

class Infix:
    def __init__(self, expression:str):
        self.expression = expression
    
    def toPrefix(self):
        expression = reverse(self.expression)
        if not ifValid(expression):
            return "The expression is invalid. Cannot convert infix to prefix!"

        stack = Stack()
        result = ""
        
        for i in range(len(expression)):
            if isOperand(expression[i]):
                result += expression[i]

            elif isOperator(expression[i]):
                if stack.isEmpty():
                    stack.push(expression[i])
                
                elif hasHigherPrecedence(expression[i], stack.top()):
                    stack.push(expression[i])

                elif hasHigherPrecedence(stack.top(), expression[i]):
                    result += stack.top()
                    stack.pop()
                    stack.push(expression[i])

                else:
                    stack.push(expression[i])

            elif expression[i] == '(':
                stack.push(expression[i]) 

            elif expression[i] == ')':
                while not stack.isEmpty() and stack.top() != '(':
                    result += stack.top()
                    stack.pop()
                stack.pop() # pops the opening parenthesis
            
        while not stack.isEmpty():
            result += stack.top()
            stack.pop()

        return reverse(result)


    def toPostfix(self):
        expression = self.expression
        if not ifValid(expression):
            return "The expression is invalid. Cannot convert infix to postfix!"

        stack = Stack()
        result = ""

        for i in range(len(expression)): 
            if isOperand(expression[i]): 
                result += expression[i]

            elif isOperator(expression[i]):
                while not stack.isEmpty() and hasHigherPrecedence(stack.top(), expression[i]) and stack.top() != '(':
                    result += stack.top()
                    stack.pop()
                
                stack.push(expression[i])

            elif expression[i] == '(':
                stack.push(expression[i]) 

            elif expression[i] == ')':
                while not stack.isEmpty() and stack.top() != '(':
                    result += stack.top()
                    stack.pop()
                stack.pop() # pops the opening parenthesis

        while not stack.isEmpty():
            result += stack.top()
            stack.pop()
        
        return result

        
class Prefix:
    def __init__(self, expression:str):
        self.expression = expression
    
    def toInfix(self):
        expression = reverse(self.expression)
        stack = Stack()
        result = ""

        for i in range(len(expression)):
            if isOperand(expression[i]):
                stack.push(expression[i])

            elif isOperator(expression[i]):
                op1 = stack.top()
                stack.pop()
                op2 = stack.top()
                stack.pop()
                exp = f"{op1}{op2}{expression[i]}"
                stack.push(exp)
            
        while not stack.isEmpty():
            result += stack.top()
            stack.pop()

        return result

    def toPostfix(self):
        expression = reverse(self.expression)
        stack = Stack()
        result = ""

        for i in range(len(expression)):
            if isOperand(expression[i]):
                stack.push(expression[i])

            elif isOperator(expression[i]):
                op1 = stack.top()
                stack.pop()
                op2 = stack.top()
                stack.pop()
                exp = f"{op1}{op2}{expression[i]}"
                stack.push(exp)
            
        while not stack.isEmpty():
            result += stack.top()
            stack.pop()

        return result


class Postfix:
    def __init__(self):
        pass
    
    def toInfix(self):
        pass

    def toPrefix(self):
        pass


def main():

    print("Select input expression: \n (1) Infix\n (2) Prefix\n (3) Postfix\n")
    type_expression = input("Type the number of chosen expression: ")
    # input_expression = input(f"Enter your infix expression: ")

    if type_expression == "1":
        input_expression = input(f"Enter your infix expression: ")
        _expression = Infix(input_expression)
        print()
        print("Infix:", input_expression)
        print("Prefix:", _expression.toPrefix())
        print("Postfix:", _expression.toPostfix())
        print() 

    elif type_expression == "2":
        input_expression = input(f"Enter your prefix expression: ")
        _expression = Prefix(input_expression)
        print()
        print("Prefix:", input_expression)
        print("Infix:", _expression.toPostfix())
        print("Postfix:", _expression.toPostfix())
        print() 

    elif type_expression == "3":
        input_expression = input(f"Enter your postfix expression: ")
        expression = Postfix(input_expression) 
    
    else:
        return "Invalid type of expression! Please try again! :("



    # expression = input("Type in your input: ")
    # input_expression = "6 2 3 + - 3 8 2 / + * 2 ^ 3 +"

    expression = input_expression.split()
    # print(input_expression.split())


def test():
    type_expression = "2"
    input_expression = "++A*BCD"

    if type_expression == "1":
        _expression = Infix(input_expression) 
        print("Infix:", input_expression)
        print("Prefix:", _expression.toPrefix())
        print("Postfix:", _expression.toPostfix())

    elif type_expression == "2":
        _expression = Prefix(input_expression)
        print("Prefix:", input_expression)
        print("Infix:", _expression.toPostfix())
        print("Postfix:", _expression.toPostfix())

    elif type_expression == "3":
        expression = Postfix(input_expression)
        print("Postfix:", input_expression) 
        print("Infix:", _expression.toInfix())
        print("Prefix:",  _expression.toPrefix())
        
        
    
    else:
        return "Invalid type of expression! Please try again! :("


if __name__ == "__main__":
    test()
    # main()