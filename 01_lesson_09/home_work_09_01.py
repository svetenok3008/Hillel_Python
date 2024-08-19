import string


def clean_punctuation(text: str) -> str:
    """This function removes punctuation from the text.
    :param text: text where we are removing punctuation from.
    """
    punctuation_list = [i for i in string.punctuation]
    return ''.join(list(filter(lambda x: x not in punctuation_list, text)))


def popular_words(text: str, words: list) -> dict:
    """This function defined how many times each word in the list met in the text,
    :param text: Text where we are looking for the words from the list,
    :param words: List of words to be found,
    :return: Dict where key is word, value is count of word's met"""

    result = dict()
    text_list = clean_punctuation(text.lower()).split()
    for word in words:
        count_word = text_list.count(str(word).lower())
        result[word] = count_word
    return result


assert popular_words('''When I was One I had just begun  I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
