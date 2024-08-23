def first_word(text: str) -> str:
    """ Пошук першого слова """
    start = None
    for i in range(0, len(text)):
        if text[i] in ('.', ',', ' '):
            continue
        else:
            start = i
            break

    end = len(text)

    for n in range(start + 1, len(text)):
        if text[n] in ('.', ',', ' '):
            end = n
            break

    return text[start: end]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
