for i in range (1, 11):
    with open(str(i) + " 주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간 report -" .format(i))
        report_file.write("\n부서: ")
        report_file.write("\nName: ")
        report_file.write("\n업무 요약: ")





