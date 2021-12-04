# vigilant-octo-system

***Readme**** 

Github Link:  

Employee class: This class is used to calculate employee salaries and bonus eligibility. The employee class does this by taking in arguments for employee names, current salary, salary raise ratio, day amount bounds, and the number of days worked.  It then adds the important employee information to a single formatted string which is accessible via string magic method. 

 

Self.__identifier: This class variable is the name of the employee. 

 

Self.__raise_ratio: This class variable sets the percent change for the employee’s yearly salary 

 

Self.__bounds: This class variable sets the boundaries which determine bonus eligibility. This variable consists of a two element list. The first element is the lower bound for bonus eligibility, and the second element is the higher bound. 

 

Self.__earnings: This class variable represents the employee’s current yearly salary. 

 

set_id/get_id: This set of methods creates a private identity data variable and allows access to it, respectively. The set method takes in self and identifier, and the get method only takes in self. 

 

set_ratio/get_ratio: This set of method creates a private raise ratio data variable and allows access to it, respectively. The set method takes in self and ratio, and the get method only takes in self. 

 

set_bounds/get_bounds: This set of methods creates a private boundary data variable, and allows access to it, respectively. The set method takes in self and bounds, and the get method only takes in self. 

 

set_days/get_days: This set of methods creates a private days data variable, and allows access to it, respectively. The set method takes in self and days, and the get method only takes in self. 

 

set_earnings/get_earnings: This set of methods creates a private earnings data variable, and allows access to it, respectively. The set method takes in self and earnings, and the get method only takes in self. 

 

 

Calculate_new_salary: This method calculates the new salary for the employee object. This method only takes in self as an argument. The new salary is calculated by multiplying the employees current salary by the raise ratio. 

 

Employee_standing: This method determines employee eligibility for a bonus. It takes in self as an argument. It then determines eligibility by comparing the amount of days worked to the class bounds variable. If the number of days worked is below the lower bound, then the employee is deemed ineligible. If the number of days is above the higher bound, the employee is deemed eligible. Lastly, if the number of days exists between the two bounds, then the employee is deemed conditionally eligible. 

 

__str__: This string method puts all the employee information into a single formatted string. This allows this string to be accessed via calling the string magic method. 

 

Demo program: This program creates four different employee objects. The names of these objects are appended to a list. This list is then iterated through, and the string magic method of each object is appended to a string. This string consists of a line for each employee which shows the employee name, new salary, days worked, and bonus eligibility. Lastly, this string is written to a new file called Employee_Info.txt.  

 

Program instructions: There are no additional files or procedures required for this script. To run it, simply access via your terminal or run it through your ide.  

 

 

 

 

 

 

 
