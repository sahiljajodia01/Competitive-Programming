def simplifyPath(A):
    if A == '/../' or A == '/./' or A == '/..' or A == '/.':
        return '/'

    A = A.split('/')
    
    if A[-1] == '':
        A = A[:-1]

    A = [a for a in A if a != '.' and a != '']
    A.insert(0, '')
    s = []
    for i in A:
        if i.isalpha() or i == '':
            s.append(i)
        elif i == '..' and len(s) != 1:
            s.pop()

    s = '/'.join(s)
    print(s)


simplifyPath("/a/./b/../../c/")
simplifyPath("/home/")
simplifyPath("/../")
simplifyPath("/.././ima/zkj/epp/oes/rak/lcq/ceo/mkq/././hdm/vom/../syw/iwc/rlf/lcd/./fsx")
simplifyPath("/home//foo/")

    
