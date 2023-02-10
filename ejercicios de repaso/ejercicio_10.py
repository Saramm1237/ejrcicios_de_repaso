def fac(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fac(n-1)

print(f'3! = {fac(3)}')
print(f'0! = {fac(0)}')