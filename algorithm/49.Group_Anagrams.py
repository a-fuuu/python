import collections

'''
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
'''

def group_anagrams(word_array : list)->list:
    anagram = collections.defaultdict(list)
    for word in word_array:
        anagram[''.join(sorted(word))].append(word)
    return list(anagram.values())

if __name__ == '__main__':
    lst = ['ate', 'tae', 'eat', 'tot', 'tto']
    print(group_anagrams(lst))