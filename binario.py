def binary(n):
  return bin(n)[2:]


def decimal(n):
  a = 0
  b = 0
  while b != n:
    b = int(binary(a))
    if b == n:
      return a
    else :
      a = a + 1
