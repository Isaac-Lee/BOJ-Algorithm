def is_anagram(str1, str2):
    if "".join(sorted(str1)) == ''.join(sorted(str2)):
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        word1, word2 = input().split()
        if is_anagram(word1, word2):
            print(word1, "&", word2, "are anagrams.")
        else:
            print(word1, "&", word2, "are NOT anagrams.")