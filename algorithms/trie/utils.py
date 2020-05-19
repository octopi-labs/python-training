def bin_to_nibbles(s):
    """convert string s to nibbles (half-bytes)
    >>> bin_to_nibbles("")
    []
    >>> bin_to_nibbles("h")
    [6, 8]
    >>> bin_to_nibbles("he")
    [6, 8, 6, 5]
    >>> bin_to_nibbles("hello")
    [6, 8, 6, 5, 6, 12, 6, 12, 6, 15]
    """
    res = []
    for x in s:
        intrm = divmod(ord(x), 16)
        print(x, intrm)
        res += intrm
    return res



if __name__ == "__main__":
    test = bin_to_nibbles("A")
    print(test)
    test = bin_to_nibbles("Apple")
    print(test)
    test = bin_to_nibbles("apple")
    print(test)


