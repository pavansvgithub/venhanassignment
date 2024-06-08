class Employee:
    employee_count = 0 
    def __init__(self,employee_id,name):
        self.employee_id = employee_id
        self.name = name 
        Employee.employee_count_increase()
 
    @classmethod 
    def employee_count_increase(cls):
        cls.employee_count += 1 
    @classmethod 
    def get_employee_count(cls):
        return cls.employee_count 
    @staticmethod 
    def is_employee_id_valid(employee_id):
        return isinstance(employee_id, str) and employee_id.isdigit() 

employee1 = Employee("123","Bobes") 

print(Employee.get_employee_count())
print(Employee.is_employee_id_valid("12345"))
print(Employee.is_employee_id_valid("123A5"))

employee2 = Employee("456","Alice")
print(Employee.get_employee_count())