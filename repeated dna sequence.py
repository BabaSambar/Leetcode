def findRepeatedDnaSequences(s: str) -> list[str]:
    repeatedList = set()
    word = s[:10]
    hashset = set()
    hashset.add(word)
    for i in range(10, len(s)):
        word += s[i]
        word = word[1:]
        print(word)
        if word in hashset:
            repeatedList.add(word)
        else:
            hashset.add(word)
    return list(repeatedList)

sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(sequence))


            


