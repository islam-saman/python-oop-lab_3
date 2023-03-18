class Person:
    moods = ("happy", "tired", "lazy")    
    def __init__(self, name):
        self.__name = name
        self.__mood = "Happy"
        self.__money = 0
        self.__healthRate
    
    def getName(self):
        return self.__name


    # There is no need for setter here since it will depend on sleep and work
    # def setHealthRate(self, healthRate):
    #     if healthRate >= 0 and healthRate <= 100:
    #         self.__healthRate = healthRate
    #     else:
    #         return "Health rate must be between 0 and 100"
    

    def getHealthRate(self, healthRate):
        return self.__healthRate

    # There is no need for setter here since it will depend on number of meals given by eat
    # def setMood(self, mood):
    #     if mood in Person.moods:
    #         self.__mood = mood
    #     else:
    #         return "Acceptable moods are happy, tired, lazy"

    def getMood(self, mood):
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
        super(Employee, self). init (name)
        self.__salary
        self.__car = Car()
        self.__email
        self.__distanceToWork = None

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
            self.__mood = "happy"

        elif workHours > 8:
            self.__mood = "tired"

        else:
            self.__mood = "lazy"

    def drive(self, velocity):
        self.__car.run(self.__distanceToWork, velocity)       

    def refuel():
        print("Can refuel")

    def send_mail():
        print("Can send Email")



class Car:
    def __init__(self):
        self.name = None
        self.__fuelRate = None
        self.__velocity = None

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
        

    def stop():
        print("stop the car")

# There is a still a lot of work to do.
# sorry for being late, I had some problem lately 
# thank you for your understanding