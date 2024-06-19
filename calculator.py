def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  try:
    return (n1 / n2)
  except ZeroDivisionError:
     return "Cannot divide by 0"

def get_num(text):
  try:
     return int(input(f"\n{text}"))
  except ValueError:
     return "Please enter a valid integer"

def get_selection():
  selection = int(input("\nSelect your calculator operations: \
                      \n1.Addition\
                      \n2.Subtraction\
                      \n3.Multiplication\
                      \n4.Division\n\n"))
  if selection not in (1, 2, 3, 4):
    raise ValueError
  return selection

