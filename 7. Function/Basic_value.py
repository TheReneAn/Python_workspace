def profile(name, age, main_lang):
    print("Name: {0}\t Age: {1}\t Main_language: {2}"\
        .format(name, age, main_lang))

profile("Rene", 28, "Python")
profile("Nick", 31, "Javascript")

# If they are in the same class at school.

def profile2(name, age = 28, main_lang = "Python"):
    print("Name: {0}\t Age: {1}\t Main_language: {2}"\
        .format(name, age, main_lang))

profile2("Rene")
profile2("Nick")

