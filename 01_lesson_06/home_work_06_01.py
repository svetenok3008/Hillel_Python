import string

user_letters = input('Input two letters using delimiter "/": ')

all_letters = string.ascii_letters
new_str = all_letters[all_letters.find(user_letters[0]):all_letters.find(user_letters[-1]) + 1]
print(new_str)
