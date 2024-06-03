class Student:
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code

        def greet_student(self):
            greeting = f"Hello{self.first_name},welcome to {self.school}.Your code is {self.code}"
            return greeting

        def greet_student_year_of_birth(self):
            born_year = f"Hello{self.first_name},you were in the year {self.age}-2024" 
            return born_year

        def display_initial(self):
            initials = f"Hello {self.first_name[0]}.{self.last_name[0]} welcome to {self.school}" 
            return initials

        def display_full_name(self):
            fullname = f"Hello {self.first_name}{self.last_name} welcome to {self.school}" 
            return fullname

        

    
    