from datetime import datetime
# import pandas as pd

# class CheckDate:
#     def __init__(self):
#         self.value = None
#
#     def __set__(self, instance, value):
#         if value and value <= datetime.now():
#             self.value = value
#         else:
#             raise ValueError(f"Invalid date: {value}")
#
#     def __get__(self, instance, owner):
#         return self.value


class Person:

    def __init__(self, first_name, last_name=None, surname=None, gender=None, birthday=None, deathday=None):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.gender = gender
        self.birthday = birthday
        self.deathday = deathday

    def __str__(self):
        birthday_gender_str = {'male': 'Народився', 'female': 'Народилася'}
        deathday_gender_str = {'male': 'Помер', 'female': 'Померла'}
        return f"{self.first_name} {self.surname} {self.last_name} ({self.gender}), {birthday_gender_str[self.gender]}  {str(self.birthday)}, {deathday_gender_str[self.gender]}  {str(self.deathday)}"

    def __eq__(self, other):
        return (self.first_name,  self.last_name, self.surname, self.birthday) == (other.first_name, other.last_name, other.surname, other.birthday)

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.surname, self.birthday))

    def find_by_name(self, lookup_text):
        """This function is looking for a person by any part of name. As a result, the function returns an object of the class 'Person'.
        :param lookup_text: text by which the searching happened.
        """
        if lookup_text.lower() in (self.first_name + (self.last_name if self.last_name is not None else '') + (self.surname if self.surname is not None else '')).lower():
            return str(self)

    def age(self):

        if self.deathday:
            target_date = self.deathday
        else:
            target_date = datetime.now()

        diff_year = target_date.year - self.birthday.year
        diff_month = target_date.month - self.birthday.month
        diff_day = target_date.day - self.birthday.day

        if diff_month < 0:
            age = diff_year - 1
        elif diff_month == 0:
            if diff_day < 0:
                age = diff_year - 1
        else:
            age = diff_year
        return str(age)
