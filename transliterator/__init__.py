from mappings import mappings

def get_transliteration_as_pattern(string, from_, to_):
    print '\nstarting get_transliteration_as_pattern with', [string], "from ", from_, "to", to_

    if isinstance(string, str):
        string = string.decode("utf-8")

    string = string.lower()
    from_ = from_.lower()
    to_ = to_.lower()

    char_to_variations = mappings[from_.lower() + "_to_" + to_.lower()]
    print "char_to_variations is", char_to_variations
    pattern_as_string = ""
    for index, char in enumerate(string):
        if char in char_to_variations:
            pattern_as_string += '(?:' + '|'.join(char_to_variations[char]) + ')'
        else:
            #pattern_as_string += '(.*)'
            pattern_as_string += char

    if from_=="arabic" and to_=="english":
        # sometimes n doesn't appear in arabic, so put it on the end just in case
        pattern_as_string += "(|n)"

    print "pattern_as_string = ", [pattern_as_string]
    return pattern_as_string

gtap = get_transliteration_as_pattern
