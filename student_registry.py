class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        try:
            if len(new_name) >= 3 and new_name.isalpha() and new_name.istitle():
                self._name = new_name
        except:
            return self._name

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 11 and new_age < 18:
            self._age = new_age
        
    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        if new_grade == "9th" or new_grade == "10th" or new_grade == "11th" or new_grade == "12th":
            self._grade = new_grade

    def __str__(self):
        return f'Name: {self._name}, Age: {self._age}, Grade: {self._grade}'
    
    def advance (self):
        return f'{self._name} has advanced to the 13th grade'
    
    def subject(self, sub):
        return f'{self._name} is studying {sub}'
    

Bob = Student('Bob', 15, '9th')
Jessica = Student('Jessica', 17, '11th')

print(Bob.get_name)
print(Bob.get_age)
print(Bob.get_grade)
Bob.set_name = "Charlie"
print(Bob.get_name)