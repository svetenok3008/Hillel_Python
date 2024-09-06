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

    def __eq__(self, other):
        return str(self) == f"Person: {other.first_name} {other.last_name}, Gender: {other.gender}, Age: {other.age}, Record book number: {other.record_book}"

    def __hash__(self):
      return hash(str(self))


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
        all_students = ';\n'.join([str(student) for student in self.group])
        return f'Number:{self.number}\n{all_students} '