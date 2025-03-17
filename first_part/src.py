# Your code here
some_list = ['milk', 'catalog', 'c+', 'python', 'cat', 'dog']


def count(search_word, _list):
    counter = 0
    for word in _list:
        if search_word in word:
            counter += 1
    return counter


def longest_word(some_list):
    longest_seq = {"word": '', "count": 0}

    for word in some_list:

        long_internal_seq = ''

        for letter in word:

            long_internal_seq += letter

            temp_counter = count(long_internal_seq, some_list)

            if any([len(long_internal_seq) > len(longest_seq["word"]), temp_counter > longest_seq["count"]]):
                longest_seq['word'] = long_internal_seq
                longest_seq['count'] = temp_counter

    return longest_seq["word"]
