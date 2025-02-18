class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=programmer("Aasim",10000,732125)
print(p.company,p.name,p.salary,p.pin)
r=programmer("Abhishek",10000,700025)
print(r.company,r.name,r.salary,r.pin)