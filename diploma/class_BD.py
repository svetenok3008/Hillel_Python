from class_person import Person
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class BD(set):

    file_path = '''C:\\_Sveta\\UDEMY\\Python_lessons\\Hillel\\Hillel_Python_Course_01\\Hillel_Python\\diploma\\persons.xlsx'''

    def load_from_file(self):
        df = pd.read_excel(self.file_path)

        for _, row in df.iterrows():
            person = Person(
                first_name=row['first_name'],
                last_name=row['last_name'] if pd.notna(row['last_name']) else None,
                surname=row['surname'] if pd.notna(row['surname']) else None,
                gender=row['gender'] if pd.notna(row['gender']) else None,
                birthday=row['birthday'] if pd.notna(row['birthday']) else None,
                deathday=row['deathday'] if pd.notna(row['deathday']) else None
            )
            self.add(person)
        return tk.messagebox.showinfo("Дані успішно завантажені з файлу!")

    def save_file(self):

        person_list = [
            {
                "first_name": person.first_name,
                "last_name": person.last_name,
                "surname": person.surname,
                "gender": person.gender,
                "birthday": person.birthday,
                "deathday": person.deathday
            }
            for person in self
        ]

        df = pd.DataFrame(person_list, columns=["first_name", "last_name", "surname", "gender", "birthday", "deathday"])
        df.to_excel(self.file_path, index=False)
        return tk.messagebox.showinfo("Дані успішно збережено в файл!")

    def enter_person(self):

        # нове вікно для введення даних
        enter_window = tk.Tk()
        enter_window.title("Додати особу")
        enter_window.geometry("600x300")
        enter_window['bg'] = 'grey'

        # Поля для вводу даних
        tk.Label(enter_window, text="Ім'я:").pack()
        first_name_entry = tk.Entry(enter_window)
        first_name_entry.pack()

        tk.Label(enter_window, text="Прізвище:").pack()
        last_name_entry = tk.Entry(enter_window)
        last_name_entry.pack()

        tk.Label(enter_window, text="По батькові:").pack()
        surname_entry = tk.Entry(enter_window)
        surname_entry.pack()

        tk.Label(enter_window, text="Стать:").pack()
        gender_entry = tk.Entry(enter_window)
        gender_entry.pack()

        tk.Label(enter_window, text="Дата народження (DD-MM-YYYY):").pack()
        birthday_entry = tk.Entry(enter_window)
        birthday_entry.pack()

        tk.Label(enter_window, text="Дата смерті (якщо є, DD-MM-YYYY):").pack()
        deathday_entry = tk.Entry(enter_window)
        deathday_entry.pack()

        def add_person():
            # приведення до формату дати:
            birthday_dt_format = datetime.strptime(birthday_entry.get().replace(' ', '-').replace('/', '-').replace('.', '-'), '%d-%m-%Y')
            if deathday_entry.get():
                deathday_dt_format = datetime.strptime(
                    deathday_entry.get().replace(' ', '-').replace('/', '-').replace('.', '-'), '%d-%m-%Y')
            else:
                deathday_dt_format = None

            new_person = Person(
                first_name=first_name_entry.get(),
                last_name=last_name_entry.get(),
                surname=surname_entry.get(),
                gender=gender_entry.get(),
                birthday=birthday_dt_format,
                deathday=deathday_dt_format
            )
            self.add(new_person)

            return messagebox.showinfo("Додано", f"Додано особу: {new_person.first_name} {new_person.last_name}")

        submit_button = tk.Button(enter_window, text="Відправити", command=add_person)
        submit_button.pack()

    def find_person(self, lookup_name):
        persons_found = []
        persons_found_txt = ''

        for person in self:
            if person.find_by_name(lookup_name) is not None:
                persons_found_txt = persons_found_txt + person.find_by_name(lookup_name) + '\n'
                persons_found.append(person)

        return tk.messagebox.showinfo("Знайдено", f"Знайдено: {persons_found_txt}")

    def define_lookup(self):

        lookup_window = tk.Tk()
        lookup_window.title("Знайти особу та розрахувати вік")
        lookup_window.geometry("300x300")

        # Поля для вводу даних
        tk.Label(lookup_window, text="Введіть частину ім'я або прізвища:").pack()
        lookup_entry = tk.Entry(lookup_window)
        lookup_entry.pack()

        def find_person():

            lookup_text = lookup_entry.get()
            persons_found_txt = ''

            for person in self:
                if person.find_by_name(lookup_text) is not None:
                    persons_found_txt = persons_found_txt + person.find_by_name(lookup_text) + '\n'

            return tk.messagebox.showinfo("Знайдено", f"Знайдено: {persons_found_txt}")

        lookup_button = tk.Button(lookup_window, text="Шукати", command=find_person)
        lookup_button.pack()

        def count_age():

            lookup_text = lookup_entry.get()
            result_age_txt = ''
            for person in self:
                if person.find_by_name(lookup_text) is not None:
                    result_age_txt = result_age_txt + str(person) + '. Вік: ' + person.age() + '\n'

            return tk.messagebox.showinfo("Розраховано вік", f"{result_age_txt}")

        count_age_button = tk.Button(lookup_window, text="Розрахувати вік", command=count_age)
        count_age_button.pack()
