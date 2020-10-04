def std_weight(height, gender):
    if gender == "woman":
        return height * height * 21
    else:
        return height * height * 22
        
height = 172
gender = "woman"
weight = round(std_weight(height / 100, gender), 2)
print("Height {0} {1}'s standard weight is {2}kg."\
    .format(height, gender, weight))

