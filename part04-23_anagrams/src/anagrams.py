def anagrams(word1, word2):
    comp1 = sorted(word1)
    comp2 = sorted(word2)

    return comp1 == comp2


if __name__ == "__main__":
    print(anagrams("tame", "meta")) 
    print(anagrams("tame", "mate")) 
    print(anagrams("tame", "team")) 
    print(anagrams("tabby", "batty")) 
    print(anagrams("python", "java")) 