def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    x = len(s)
    if (x % 2 == 0):
        middle = x//2
        return s[middle-1:middle+1]
    else:
        middle=x//2
        return s[middle]
print(main("Nurbek"))
