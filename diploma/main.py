import tkinter as tk
from class_BD import BD

bd_people = BD()

# Створюємо головне вікно
root = tk.Tk()
root.title("БД Persons")
root.geometry("400x300")
root['bg'] = "blue"


# Кнопка "Загрузити дані з файлу"
load_button = tk.Button(root, text="Загрузити дані з файлу", command=bd_people.load_from_file)
load_button.pack(pady=10)

# Кнопка "Додати особу в базу"
add_button = tk.Button(root, text="Додати особу в базу", command=bd_people.enter_person)
add_button.pack(pady=10)

# Кнопка "Знайти людину"
find_button = tk.Button(root, text="Знайти людину", command=bd_people.define_lookup)
find_button.pack(pady=10)
#
# Кнопка "Зберігти дані в файл"
save_file_button = tk.Button(root, text="Зберігти дані в файл", command=bd_people.save_file)
save_file_button.pack(pady=10)


root.mainloop()


