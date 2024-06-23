def isCircularSentence(sentence: str) -> bool:
    startPtr = sentence[0] == sentence[-1]
    for i in range(len(sentence)):
        if sentence[i] == " ":
            if sentence[i-1] != sentence[i+1]:
                return False
    return True if startPtr else False

sentence = "eetcode"

print(isCircularSentence(sentence))