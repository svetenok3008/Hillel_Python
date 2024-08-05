import string

not_allowed_symbols = string.punctuation + ' '
not_allowed_symbols_list = [i for i in not_allowed_symbols if i != "_"]

user_variable = input('Input your variable: ')
reserved_list = [
    "False",
    "True",
    "None",
    "and",
    "with",
    "as",
    "assert",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "yield"]

count_ = user_variable.count('_')

if user_variable in reserved_list:
    result = False
    print("This is wrong name for variable: reserved word has been used. Please rename.")
elif user_variable[0].isdigit():
    result = False
    print('You variable starts with number. This is wrong.')
elif len(user_variable) == count_:
    result = False
    print("This is wrong name for variable: more then one \'_\' used. Please rename.")
elif any(i in not_allowed_symbols_list for i in user_variable):
    result = False
    print('Wrong symbol is present. Please rename.')
elif not user_variable.islower():
    result = False
    print('There is capital later present. Please rename.')
else:
    result = True
print(f'Is the name of variable correct? This is {result}.')
