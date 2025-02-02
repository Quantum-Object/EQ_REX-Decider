from NFA import NFA

N=NFA(3,{1: [('a', 2),('a',4)],2: [('a', 2),('a',4)]},[2])
N.show()
