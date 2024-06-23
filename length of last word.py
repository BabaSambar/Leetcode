def lengthOfLastWord(s:str) -> int:
    string = s.split(" ")
    i = -1
    while True:
        if string[i] != '':
            return len(string[i])
        else:
            i -= 1


print(lengthOfLastWord("Hellow World awda  wIDAd  wawwwfh  r "))