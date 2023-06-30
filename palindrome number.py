def isPalindrome(number):
    number = str(number)
    palindrome = False
    for i in range(len(number)):
        if(number[i] != number[len(number) - i - 1]):
            palindrome = False
            return False
        else:
            palindrome = True
    return palindrome
print(isPalindrome(1000021))