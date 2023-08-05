#WAP that creates a list of words by combining the words in two individual lists.
def combine_word_lists(list1, list2):

    combined_list = list1 + list2
    return combined_list

list1 = ['Hello', 'How', 'Are']
list2 = ['You', 'Today?']
combined_words = combine_word_lists(list1, list2)
print("Combined Words:", combined_words)
