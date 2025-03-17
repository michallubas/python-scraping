# TASK1
some_list = ['milk', 'catalog', 'c+', 'python', 'cat', 'dog']


# find occurrences
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


# TASK2 / not finished
import re
nutrition = 'Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, Cuivre (3b405, 3b406) : 2,2 mg,Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603,3b605, 3b606) : 11 mg –Clinoptilolited’origine sédimentaire : 2 g. Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %.'

pattern = r'\S+\s*\S+ : \d+\S*'

# all matches
matches = re.findall(pattern, nutrition)

for match in matches:
    print(f"Found match: {match}")
