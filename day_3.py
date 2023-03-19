class Person:
    moods = ("happy", "tired", "lazy")    
    def __init__(self, name):
        self.__name = name
        self.__mood = "Happy"
        self.__money = 0
        self.__healthRate = 100
    
    def getName(self):
        return self.__name


    def setHealthRate(self, healthRate):
        if healthRate >= 0 and healthRate <= 100:
            self.__healthRate = healthRate
        else:
            return "Health rate must be between 0 and 100"
    

    def getHealthRate(self, healthRate):
        return self.__healthRate

    def setMood(self, mood):
        if mood in Person.moods:
            self.__mood = mood
        else:
            return "Acceptable moods are happy, tired, lazy"

    def getMood(self):
        return self.__mood

    def sleep(self, sleepHours):
        if sleepHours == 7:
            self.__mood = "happy"

        elif sleepHours < 7:
            self.__mood = "tired"

        else:
            self.__mood = "lazy"


    def eat(self, numOfMeals):
        if numOfMeals == 3:
            self.__healthRate = 100

        elif numOfMeals == 2:
            self.__healthRate = 75

        elif numOfMeals == 1:
            self.__healthRate = 50

    def buy(self, numOfItems):
        self.__money -= numOfItems * 10 


class Employee(Person):

    def __init__(self, name):
        super(Employee, self).__init__(name)
        self.__salary = 0
        self.__car = Car()
        self.__email = None
        self.__distanceToWork = 0

    # make setters and getters for salary so I can control the value
    def setSalary(self, salary):
        if salary >= 1000:
            self.__salary = salary
        else:
            print("Salary must be greater than 1000")

    def getSalary(self):
        return self.__salary
       
    def work(self, workHours):
        if workHours == 8:
            self.setMood("happy")

        elif workHours > 8:
            self.setMood("tired")

        else:
            self.setMood("lazy")

    def drive(self, velocity):
        self.__car.run(self.__distanceToWork, velocity)
        self.__distanceToWork -= 5       

    def refuel(self):
        fuelRate = self.__car.getFuelRate()
        self.__car.setFuelRate(fuelRate + 100)

    def send_mail():
        print("Can send Email")



class Car:
    def __init__(self):
        self.name = None
        self.__fuelRate = 0
        self.__velocity = 0

    # make setters and getters for salary so I can control the value
    def setFuelRate(self, fuelRate):
        if fuelRate >= 0 and fuelRate <= 100:
            self.__fuelRate = fuelRate
            return "Car fuelRate is now " + str(self.__fuelRate)

        else:
            return "Car fuel must be between 0 to 100"

    def getFuelRate(self):
        return self.__fuelRate


    # make setters and getters for salary so I can control the value
    def setVelocity(self, velocity):
        if velocity >= 0 and velocity <= 200:
            self.__velocity = velocity
            return "Car velocity is now " + str(self.__velocity)

        else:
            return "Car velocity must be between 0 to 100."

    def getVelocity(self):
        return self.__velocity


    def run(self, distance, velocity):
        self.__velocity = velocity
        self.__fuelRate -= 5
        if self.__fuelRate == 0:
            print("Remaining distance" + str(distance))
            Car.stop()
        

    def stop(self):
        self.__velocity = 0



class Office:
    def __init__(self, name):
        self.__name = name
        employee = []

    def getOfficeName(self):
        return self.__name
