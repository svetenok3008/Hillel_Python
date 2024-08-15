import string


def is_palindrome(text):
    text_updated = [i.lower() for i in text if i not in string.punctuation + ' ']
    return text_updated == text_updated[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
