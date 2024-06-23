def mergeAlternately(word1: str, word2: str) -> str:
    ptr1, ptr2 = 0, 0
    answer = ""
    limit = max(len(word1), len(word2))
    for i in range(max(len(word1), len(word2))):
        if i > len(word1)-1:
            answer += word2[i:]
            return answer
        elif i > len(word2)-1:
            answer += word1[i:]
            return answer
        print(i)
        answer += word1[i]
        answer += word2[i]
    return answer

a = "abcd"
b = "pq"

print(mergeAlternately(a, b))