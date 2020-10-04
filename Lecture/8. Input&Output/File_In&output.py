# # Write
# # 1) file = 
# score_file = open("score.txt", "w", encoding='utf8')
# print("Math: 100", file=score_file)
# print("English: 80", file=score_file)
# score_file.close()

# # 2) write()
# score_file = open("score.txt", "a", encoding='utf8')
# score_file.write("Science: 85")
# score_file.write("\nCording: 100")
# score_file.close()

# # Read
# # 1) read()
# score_file = open("score.txt", "r", encoding='utf8')
# print(score_file.read())
# score_file.close()

# # 2) readline()
# score_file = open("score.txt", "r", encoding='utf8')
# print(score_file.readline()) # 줄별로 읽기. 한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# # 3) 
# score_file = open("score.txt", "r", encoding='utf8')
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 4) 몇줄 인지 모를때, 반복문으로 읽기
score_file = open("score.txt", "r", encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# # 5) readlines()
score_file = open("score.txt", "r", encoding='utf8')
# 모든 라인 가져와서 List형태로 저장
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()




