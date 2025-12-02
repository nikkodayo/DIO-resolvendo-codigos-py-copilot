def palindromeIndex(s):
    if s is None or len(s) < 2:
        return -1

    ss = list(s)
    l, r = 0, len(ss) - 1

    def is_palindrome(l, r):
        if l > r:
            return False
        while l < r:
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1
        return True

    if is_palindrome(l, r):
        return -1

    while l < r:
        if ss[l] != ss[r]:
            if is_palindrome(l + 1, r):
                return l
            if is_palindrome(l, r - 1):
                return r
        l += 1
        r -= 1

    return -1
