def build_lps(needle):

    lps = [0] * len(needle)  #заповнення 0 масиву та присвоєння масиву довжини тексту
    j = 0
    i = 1

    while i < len(needle):
        if needle[j] == needle[i]:
            j += 1
            lps[i] = j
            i += 1

        else:
            if j == 0:
                lps[1] = 0
                i += 1
            else:
               j = lps[j - 1]

    return lps

def kmp(haystack, pattern):
    lps = build_lps(pattern)
    length_text = len(haystack)
    length_pattern = len(pattern)
    i = 0
    j = 0
    idx = []
    while i < length_text:
        if haystack[i] == pattern[j]:
            i += 1
            j += 1
            if j == length_pattern:
                idx.append(i - j)
                break
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    if not idx:
         print(" nothing ")
    else:
        return idx

























