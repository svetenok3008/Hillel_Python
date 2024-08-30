import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    curr_position = 0
    new_text = ''

    while curr_position <= len(html):
        index_start = html.find('>', curr_position)
        index_end = html.find('<', index_start)
        if index_start != -1 and index_end != -1:
            curr_position = index_end + 1
        else:
            break
        text_to_add = html[index_start + 1: index_end].strip().strip('\n').strip('\t')
        if text_to_add not in ('', '\n+',  '\t+'):
            new_text = new_text + text_to_add + '\n'

    with open(result_file, 'w') as file:
        file.write(new_text)

    return new_text


print(delete_html_tags('draft.html'))
