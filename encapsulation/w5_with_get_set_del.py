class Employee:

    def __init__(
        self,
        name: str,
        salary: float,
    ) -> None:
        self.name = name
        self.__salary = salary

    # def del_the_salary(self):
    #     print("this salary is going to delete")
    #     del self.__salary

    @property
    def salary(self):
        """Getter method to get the salary of the user"""
        return self.__salary

    
    @property
    def salary(self):
        """This is where it will check if i have the salary is avaialble or not"""
        try:
            return self.__salary
        except AttributeError:
            return "Salary has been deleted you cannot get 🛑"


    @salary.setter
    def salary(self, amount: float):
        """This is for the change of the salary of the employee
        This is like the setter of this"""
        if amount < 0:
            raise ValueError("Salary Cannot be Negative ")
        self.__salary = amount

    @salary.deleter
    def salary(self):
        """Deleter method to delete salary"""
        print("This salary is going to be deleted!")
        del self.__salary


e1 = Employee("Rahul", 500)
print(e1.salary)
del e1.salary
print(e1.salary)
