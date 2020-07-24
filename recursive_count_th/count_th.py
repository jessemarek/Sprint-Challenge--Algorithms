'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur
within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    pattern = 'th'
    # base case
    # word has no `th` occurances
    if 'th' not in word:
        return 0

    # how do we get closer to the base case?
    else:
        # split the str into an array removing the
        # first occurence of our pattern
        word = word.split(pattern, 1)
        word.pop(0)
        # return 1 for the occurence of the pattern + result
        # of next recusrsive pass.
        # on each recursive call pass the remaining bits
        # of the word we haven't checked yet
        # convert the list back into a string and call function recusrively
        return 1 + count_th(str(word))
