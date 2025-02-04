from REX import REX
from NFA import NFA

r=REX("ab*")
print(r.RPN())

N=(r.to_NFA())
N.show()
print(N.A_NFA("abbba"))
