def correct_sentence(user_str):
    user_str = (user_str.replace(user_str[0], user_str[0].upper(), 1))
    if user_str[-1] != '.':
        user_str = user_str + '.'
    return user_str


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
