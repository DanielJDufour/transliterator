from mappings import mappings
from re import findall, IGNORECASE, MULTILINE, UNICODE 
flags = IGNORECASE|MULTILINE|UNICODE


# tries to transliterate if you give it some text as a hint
# if a word matches the pattern in the text it returns the word
# if not, it returns an empty list
def get_transliterations_from_text(string, from_, to_, text):
    print "starting get_transliterations_from_text with", [string], "from", from_, "to", to_
    length_of_string = len(string)
    pattern_as_string = get_transliteration_as_pattern(string, from_, to_)
    transliterations = set()
    for found in findall(pattern_as_string, text, flags=flags):
        if len(found) > 0.6 * len(string):
            transliterations.add(found)
    transliterations = list(transliterations)
    print "finishing get_transliterations_from_text with", transliterations
    return transliterations

# PROBLEM: when word has too many optionally missed things
# should probably make it so word length has to be at least a certain length

def get_transliteration_as_pattern(string, from_, to_):
    print '\nstarting get_transliteration_as_pattern with', [string], "from ", from_, "to", to_

    if isinstance(string, str):
        string = string.decode("utf-8")

    words = string.lower().split()
    from_ = from_.lower()
    to_ = to_.lower()

    char_to_variations = mappings[from_.lower() + "_to_" + to_.lower()]
    print "char_to_variations is", char_to_variations
    pattern_as_string = ""
    for index_of_word, word in enumerate(words):
        if index_of_word != 0:
            pattern_as_string += '(?:' + '|'.join(char_to_variations[" "]) + ')' # adds space
        #pattern_as_string += u"(?<=\\b)"
        for char in word:
            if char in char_to_variations:
                pattern_as_string += '(?:' + '|'.join(char_to_variations[char]) + ')'
            else:
                #pattern_as_string += '(.*)'
                pattern_as_string += char
        #pattern_as_string += u"(?=\\b)"
        pattern_as_string += u"(?<=[^ ]{2})"

    if from_=="arabic" and to_=="english":
        # sometimes n doesn't appear in arabic, so put it on the end just in case
        pattern_as_string += "(|n)"

    print "pattern_as_string = ", [pattern_as_string]
    return pattern_as_string

gtap = get_transliteration_as_pattern
