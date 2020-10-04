import pickle

# b means binary type. Pickle을 이용하기 위해서 반드시 정의.
profile_file = open("profile.pickle", "wb")
profile = {"Name": "Rene", "Age": 28, "Hobby": ["Soccer", "Golf", "Cording"]}
print(profile)
# profile에 있는 내용을 file에 Save
pickle.dump(profile, profile_file)
profile_file.close()


profile_file = open("profile.pickle", "rb")
# file에 있는 정보를 profile에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

