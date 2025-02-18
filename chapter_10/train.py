from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(150,6000)}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")

t=Train(345678)
t.book("Sealdah","Kumedpur")
t.getFare("Sealdah","Kumedpur")
t.getStatus()