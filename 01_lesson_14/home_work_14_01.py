class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}.\nGender: {self.gender}\nAge: {self.age}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}, Record book number: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.students_in_group = 0

    def add_student(self, student):
        if self.students_in_group + 1 > 10:
            raise ValueError(f'Не вдалося додати {str(student)}\nВ группі вже є 10 студентів!')
        else:
            self.group.add(student)
            self.students_in_group += 1

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)
            self.students_in_group -= 1
        else:
            return 'No, error!'

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ';\n'.join([str(student) for student in gr.group])
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'Bob', 'Green', 'AN146')
st4 = Student('Female', 26, 'Britney', 'Fox', 'AN147')
st5 = Student('Female', 25, 'Lara', 'Mhehel', 'AN148')
st6 = Student('Male', 21, 'Alex', 'Rondon', 'AN149')
st7 = Student('Male', 32, 'Rey', 'Smith', 'AN150')
st8 = Student('Female', 22, 'Victoria', 'Zinger', 'AN151')
st9 = Student('Male', 23, 'Steven', 'King', 'AN152')
st10 = Student('Male', 26, 'Piter', 'Scott', 'AN153')
st11 = Student('Male', 25, 'Robert', 'Covalley', 'AN154')

gr = Group('PD1')

try:
    gr.add_student(st1)
except ValueError as message:
    print(message)

try:
    gr.add_student(st2)
except ValueError as message:
    print(message)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
print(gr.delete_student('Taylor'))  # No error!

try:
    gr.add_student(st2)
except ValueError as message:
    print(message)

try:
    gr.add_student(st3)
except ValueError as message:
    print(message)

try:
    gr.add_student(st4)
except ValueError as message:
    print(message)

try:
    gr.add_student(st5)
except ValueError as message:
    print(message)

try:
    gr.add_student(st6)
except ValueError as message:
    print(message)

try:
    gr.add_student(st7)
except ValueError as message:
    print(message)

try:
    gr.add_student(st8)
except ValueError as message:
    print(message)

try:
    gr.add_student(st9)
except ValueError as message:
    print(message)

try:
    gr.add_student(st10)
except ValueError as message:
    print(message)

try:
    gr.add_student(st11)
except ValueError as message:
    print(message)
