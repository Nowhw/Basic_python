class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j")

class threeDvector(twoDvector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    
    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")


a=twoDvector(7,8)
a.show()
b=threeDvector(3,7,9)
b.show()