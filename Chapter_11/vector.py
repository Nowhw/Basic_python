class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    
    def __mul__(self,other):
        result=vector(self.x*other.x,self.y*other.y,self.z*other.z)
        return result
    
    def __str__(self):
        return f"vector({self.x}i+{self.y}j+{self.z}k)"
    

a=vector(1,2,3)
b=vector(4,5,6)
c=vector(7,8,9)

print(a+b)
print(a*b)

print(a+c)
print(a*c)