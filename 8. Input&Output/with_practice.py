with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("I'm studing Python well")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

