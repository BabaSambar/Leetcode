def reverse(string):
    while "  " in string:
        string = string.replace("  ", " ")
    while string[0] == " ":
        string = string[1:]
    while string[-1] == " ":
        string = string[0:len(string)-1]
    string = string.split(" ")

    temp = ""
    for i in range(int(len(string)/2)):
        temp = string[i]
        string[i] = string[len(string) - i - 1]
        string[len(string) - i - 1] = temp
    string = " ".join(string)

    return string
        

string = "a good   example"
print(reverse(string))