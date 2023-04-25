def is_pangram(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in s.lower():
        if i in a:
            a = a.replace(i, '')
    if len(a) == 0:
        return True
    else:
        return False