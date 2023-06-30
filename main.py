def is_that_polindrome(string):
    if string.lower() == string.lower()[::-1]:
        return True

    return False


if __name__ == '__main__':
    print(is_that_polindrome('testString'))