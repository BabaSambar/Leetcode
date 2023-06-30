def isSubsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len(s):
        return True
    else:
        return False
t = """mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvml
    hgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbu
    aktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcv
    ljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmi
    imbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdao
    dzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinz
    mkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhllj
    zejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcn
    zcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahosw
    hlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"""
s = "rjufvjafbxnbgriwgokdgqdqewn"
print(isSubsequence(s, t))