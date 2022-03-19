"""Little Sister's Vocabulary"""

def add_prefix_un(word):
    """Add a prefix to a word"""
    return 'un' + word
   

def make_word_groups(vocab_words):
    """Add prefixes to word groups"""
    prefix = vocab_words[0]
    return ' :: '.join([prefix + word if prefix != word else word for word in vocab_words])


def remove_suffix_ness(word):
    """Remove a suffix from a word"""
    suffix = word[-4:]
    nword = word.replace(suffix, "")
    if nword[-1] == 'i':
        return nword.replace('i', 'y')
    return nword


def adjective_to_verb(sentence, index):
    """Extract and transform a word"""
    nsentence = sentence.replace('.', "")
    separate = nsentence.split()
    return separate[index] + 'en'