# WAP to create a class Train which has method to book a ticket, get status(no. of seats) and get fare information of train running under indian railways.
import random
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} ")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running successfully.")

    def getFare(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} is {random.randint(222,5555)}")


t = Train(12356)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")