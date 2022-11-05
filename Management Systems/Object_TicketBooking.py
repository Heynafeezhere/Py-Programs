#Railway ticket booking management system

class TicketBookingSystem(object):
    def __init__(self,maxTicket,lowerBerth,upperBerth,sideUpperBerth,sideLowerBerth) -> None:
        super().__init__()
        self.toExit = False
        self.maxTicket =  maxTicket
        self.lowerBerth = lowerBerth
        self.upperBerth = upperBerth
        self.sideUpperBerth = sideUpperBerth
        self.sideLowerBerth = sideLowerBerth
        self.bookedTickets = []
        while not self.toExit:
            print("Please select from the below option:-")
            print("1.Booking")
            print("2.Availability Check")
            print("3.Cancelation")
            print("4.Prepare Chart")
            print("5.Exit")
            choice = int(input())
            if choice==1:
                self.__bookTicket()
            elif choice==2:
                self.__availablity()
            elif choice==3:
                self.__cancelation()
            elif choice==4:
                self.__prepareChart()
            elif choice==5:
                self.toExit = True
            else:
                print("!!!!!Invalid Option!!!!!")

    def __bookTicket(self):
        if len(self.bookedTickets) >= self.maxTicket:
            print()
            print("No Seats are available!")
            print()
            return

        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        bp = int(input("Enter your preference[1.Lower/2.Upper/3.Side Upper/4.Side Lower]: ")) 
        newTicket = Ticket(name,age,self.berthPreference(bp))
        self.bookedTickets.append(newTicket)
        print()
        print(newTicket)
        print()
        print("Your Ticket has been Booked Succefully!")
        print()

    def __availablity(self):
        if len(self.bookedTickets) >= self.maxTicket:
            print()
            print("Booking not available!")
            print()
            return
        else:
            print()
            print(len(self.bookedTickets),"are available")
            print()
            return
    
    def __cancelation(self):
        ticketId = input("Enter the ticket Id: ").strip()
        tickedInd = -1
        bth = ""
        for i in range(len(self.bookedTickets)):
            if self.bookedTickets[i].getId() == ticketId:
                bth =  self.bookedTickets[i].getBirthPreference()
                tickedInd = i
                break
        if tickedInd==-1:
            print("No such ticket")
        else:
            self.bookedTickets.pop(tickedInd)
            print("Ticket with TicketId : {} has been cancelled successfully!!! ".format(ticketId))
            if bth == "Lower berth":
                self.lowerBerth+=1
            elif bth == "Upper berth":
                self.upperBerth+=1
            elif bth == "Side Upper berth":
                self.sideUpperBerth+=1
            else:
                self.sideLowerBerth+=1
    
    def __prepareChart(self):
        for i in range(len(self.bookedTickets)):
            print(i+1,") Ticket Id: ",self.bookedTickets[i].getId(),"  ","Name: ",self.bookedTickets[i].getName())
        self.toExit = True

    def berthPreference(self,bp):
        temp = True
        while temp == True:
            if bp==1 and self.lowerBerth>0:
                self.lowerBerth -=1
                temp = False
                return "Lower berth"
            elif bp==2 and self.upperBerth>0:
                self.upperBerth -=1
                temp = False
                return "Upper berth" 
            elif bp==3 and self.sideUpperBerth>0:
                self.sideUpperBerth -=1
                temp = False
                return "Side Upper berth"
            elif bp==4 and self.sideLowerBerth>0:
                self.sideLowerBerth -=1
                temp = False
                return "Side Lower berth"
            elif bp==5:
                bp=1    
            else:
                bp +=1



class Ticket(object):
    __nextId = 1
    def __init__(self,name,age,berthPreference) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.bP = berthPreference
        self.id = Ticket.__nextId
        Ticket.__nextId+=1

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getId(self):
        return "TK" + str(self.id)

    def getBirthPreference(self):
        return self.bP

    def __str__(self) -> str:
        return "Ticket Id: " + self.getId() + " " + "Passanger Name: " + self.getName() + " " + "Berth: " + self.getBirthPreference()
    

lowerBerth = int(input("Number of Lower berth: "))
upperBerth = int(input("Number of upper berth: ")) 
sideUpperBerth = int(input("Number of Side upper berth: "))
sideLowerBerth = int(input("Number of Side lower berth: "))
total = lowerBerth + upperBerth + sideUpperBerth + sideLowerBerth
a = TicketBookingSystem(total,lowerBerth,upperBerth,sideUpperBerth,sideLowerBerth)

