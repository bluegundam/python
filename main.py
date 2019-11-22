def get_sum(a, b):
  return(int(a) + int(b))

def get_difference(a, b):
  return(int(a) - int(b))

def get_product(a, b):
  return(int(a) * int(b))

def get_quotient(a, b):
  return(int(a) / int(b))

def get_floored_quotient(a, b):
  return(int(a) // int(b))

def get_reminder(a, b):
  return(int(a) % int(b))

def get_pow(a, b):
  return(int(a) ** int(b))

def get_msg(c, d , calc_val, method):
  return f"{method} of {c} and {d} = {calc_val}\n"

arg1=2
arg2="10"

result = get_sum(b=arg2, a=arg1)
msg = get_msg(c=arg1, d=arg2, calc_val=result, method="get_sum")
print(msg)

result = get_difference(b=arg2, a=arg1)
msg = get_msg(c=arg1, d=arg2, calc_val=result, method="get_difference")
print(msg)

result = get_product(b=arg2, a=arg1)
msg = get_msg(c=arg1, d=arg2, calc_val=result, method="get_product")
print(msg)

result = get_quotient(b=arg2, a=arg1)
msg = get_msg(c=arg1, d=arg2, calc_val=result, method="get_quotient")
print(msg)

result = get_floored_quotient(b=arg2, a=arg1)
msg = get_msg(c=arg1, d=arg2, calc_val=result, method="get_floored_quotient")
print(msg)

result = get_reminder(b=arg2, a=arg1)
msg = get_msg(c=arg1, d=arg2, calc_val=result, method="get_reminder")
print(msg)

result = get_pow(b=arg2, a=arg1)
msg = get_msg(c=arg1, d=arg2, calc_val=result, method="get_pow")
print(msg)
