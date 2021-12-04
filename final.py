# Bryan Kobashi
# Assignment 10.1
# This script creates a class for employees, then individual employees are created as subclasses. The class variable gets set to
# the company wide raise amount. Each individual employee's yearly salary is calculated by getting the raise amount, then doing 
# calculations with each employee's individualized salary and yearly bonuses. A second class list variable is created to represent the cutoff
# amount for days needed to receive a promotion, or to receive a termination warning for missed days. Yay capitalism! This class variable
# is accessed with a get-set method. If the employee's data variable, missed_days, is greater than the upper bound, the warning method returns true.
# If it it is lower than the lower bound, the promotion method returns true.

class Employee():
    def __init__(self, identifier, ratio, earnings, bounds, days_worked):
    
        # Set employee identifier class variable   
        self.__identifier = self.set_id(identifier)

        # Set raise ratio class variable
        self.__raise_ratio = self.set_ratio(ratio)

        # Set raise/warning bounds class variable.
        self.__bounds = self.set_bounds(bounds)

        # Set earnings class variable
        self.__earnings = self.set_earnings(earnings)

        self.__days = self.set_days(days_worked)

        # Set salary class variable
        self.__sal = self.calculate_new_salary()

        # Set standing class variable
        self.__stand = self.employee_standing()

    # Set method for days worked   
    def set_days(self, days_worked):
        self.__days = days_worked
        return self.__days

    # Get method for days worked   
    def get_days(self):
        return self.__days

    # Set method for earnings
    def set_earnings(self, earnings):
        self.__earns = earnings
        return self.__earns
    
    # Get method for earnings
    def get_earnings(self):
        return self.__earns

    # Set method for id   
    def set_id(self, identifier):
        self.__id = identifier
        return self.__id

    # Get method for id   
    def get_id(self):
        return self.__id

    # Set ratio method. Determines what to return based on ratio argument.
    def set_ratio(self, ratio):
        
        self.__raise_ratio = ratio
        return self.__raise_ratio

    # Get raise ratio method        
    def get_ratio(self):
        return(self.__raise_ratio)

    # Set performance boundaries method
    def set_bounds(self, bounds):
        # Argument must be a list of length 2
        if type(bounds) != list or len(bounds) !=2:
            self.__bounds = ("You must enter a list of 2 numbers. The first number indicates the lower bound for days worked, and the second represents the upper bound.")
            return self.__bounds
        else:
            self.__bounds = bounds
            return self.__bounds

    # Get performance boundaries method    
    def get_bounds(self):
        return self.__bounds
    
    # Calculate salary method   
    def calculate_new_salary(self):
        # Salary is the raise ratio times the yearly earnings
        self.__salary = self.__raise_ratio * self.__earns
        self.__salary = int(self.__salary)
        return self.__salary

    # Calculate employee standing method  
    def employee_standing(self):
        # If days worked are less than the lower boundary
        if self.__days < self.__bounds[0]:
            # Create warning message
            self.__standing = "Not eligible"
            return self.__standing
        # OTOH, if the days worked is more than he higher bound, create congratulation message.
        elif self.__days > self.__bounds[1]:
            self.__standing = "Eligible"
            return self.__standing
        else:
            self.__standing = "Conditionally eligible"
            return self.__standing
    
    # Create a string containing all important employee info that can be accessed via a string magic method.   
    def __str__(self):
        self.__final = f"Name: {self.__id} \t New Salary: ${self.__sal} \t  Days worked: {self.__days} days. \t Bonus eligibility: {self.__standing} \n"
        return self.__final


def main():
    #Create empty list
    listA = []

    # Create employee objects, then append them to a list
    Jeff = Employee("Jeff", 0.9, 100000, [255, 270], 271)
    listA.append(Jeff)
    Gregory = Employee("Gregory", 0.9, 89000, [255, 270], 244)
    listA.append(Gregory)
    Sally = Employee("Sally", 1.6, 60000, [255, 270], 264)
    listA.append(Sally)
    Boing = Employee("Boing", 1.2, 120000, [255, 270], 222)
    listA.append(Boing)

    # Create an empty string...
    endstring = ""

    # Then append the magic method of each employee object in listA to it.
    for i in listA:
        endstring += str(i)

    # Lastly, write the endstring to a txt file.   
    f = open("output.txt", 'w')
    f.write(endstring)
    f.close

if __name__ == "__main__":
    main()