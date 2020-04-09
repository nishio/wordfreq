#!/usr/bin/env python3
import doctest
import sys
import re
from collections import Counter
RE_IDENTIFIER = re.compile("[a-zA-Z_][a-zA-Z0-9-_]+")


def split_words(s):
    """
    >>> split_words("abc-def")
    ['abc', 'def']
    >>> split_words("abcDef")
    ['abc', 'def']
    >>> split_words("AbcDefAbc")
    ['abc', 'def', 'abc']
    >>> split_words("split_words")
    ['split', 'words']
    """
    return [x.lower()
            for x in re.findall("[A-Z]*[a-z]+(?=[A-Z-_]|$)", s)]


def main():
    count = Counter()
    for line in sys.stdin:
        count.update(re.findall(RE_IDENTIFIER, line))

    print("identifier ranking")
    for ident, value in count.most_common(100):
        print("%s\t%s" % (ident, value))

    wordCount = Counter()
    for ident in count:
        value = count[ident]
        words = split_words(ident)
        wordCount.update({w: value for w in words})

    print("\nword ranking")
    for ident, value in wordCount.most_common(100):
        print("%s\t%s" % (ident, value))


if __name__ == "__main__":
    # doctest.testmod()
    main()
