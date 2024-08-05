punctuation_symbols = r''' !"#$%&'()*+,-./:;<=>?@[\]_^`{|}~'''
punctuation_symbols_list = [i for i in punctuation_symbols]

user_variable = input('Input your sentence: ')
user_variable = user_variable.title()
hashtag = "#" + ''.join([i for i in user_variable if i not in punctuation_symbols_list])

if len(hashtag) > 140:
    hashtag = hashtag[0:140]

print(f'The hashtag is created: {hashtag}')



