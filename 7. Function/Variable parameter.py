def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("Name: {0}\t Age: {1}\t" .format(name, age), end=" ")
    print(lang1, lang2, lang3, lang3, lang4, lang5)

profile("Rene", 28, "Python", "Java", "C", "C++", "C#")
profile("Nick", 31, "Kotlin", "Swift", "", "", "")

# I would want to write more language, or 
# I would not want to write "" again.

def profile2(name, age, *language):
    print("Name: {0}\t Age: {1}\t" .format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile2("Rene", 28, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile2("Nick", 31, "Kotlin", "Swift")

