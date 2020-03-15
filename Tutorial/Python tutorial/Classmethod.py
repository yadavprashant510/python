"""Learning of class in python
    for creating class we have to write class keyword then name of class"""


class Student:
    per_rise = 1.05
    college = 'Guru Nanak'

    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + '.' + last + '@eclerx.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        return self.marks * 1.05


std_1 = Student('Prashant', 'Yadav', 95)
std_2 = Student('Vishal', 'Yadav', 85)

print('Email=', std_1.email)
print('Marks=', std_1.marks)
print(std_1.college)
print(std_2.apply_raise())
print(std_1.fullname())
print('Email=', std_2.email)
print(std_2.fullname())
