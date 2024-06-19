def add(nhw, nsl):
  return nhw + nsl

def subtract(nhw, nsl):
  return nhw - nsl

def multiply(nhw, nsl):
  return nhw * nsl

def divide(nhw, nsl):
  try:
    return (nhw / nsl)
  except ZeroDivisionError:
     return "Cannot divide by 0"

def get_num(text):
  try:
     return int(input(f"\n{text}"))
  except ValueError:
     return "Please enter a valid integer"

def get_selection():
  selection = int(input("\nSelect your calculator function: \
                      \n1.Addition\
                      \n2.Subtraction\
                      \n3.Multiplication\
                      \n4.Division\n\n"))
  if selection not in (1, 2, 3, 4):
    raise ValueError
  return selection

