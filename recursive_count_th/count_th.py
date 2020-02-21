'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Case 1:
    # if the length of word is less than 2 return 0
    if len(word) < 2:
        return 0
    # Case 2: "th" is in the slice([:2] means take from the beginning of the word and before the position 2)
    elif word[:2] == 'th':
        # Sum 1 and continue searching
        # Send as a word the rest of the string (take from position 2 until the end of the word)
        return 1 + count_th(word[1:])
    # Case 3: "th is not in the slice"
    else:
        return count_th(word[1:])
