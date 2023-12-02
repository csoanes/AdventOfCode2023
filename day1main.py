import regex as re
from word2number import w2n

#1: load and print the data

number_words = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
sum = 0

with open("Day1Data", 'r') as file:
    lines = [line.rstrip() for line in file]

cal_values1 = {}
cal_values2 = {}
print (lines)

sum = 0

for line in lines:
    calibration_value=0
    # printing original string
    numwords = re.findall(number_words, line, overlapped=True)
    print(numwords)
    calibration_text = str(w2n.word_to_num(numwords[0]))+str(w2n.word_to_num(numwords[-1]))
    if (calibration_text != ""):
        calibration_value = int(calibration_text)
        print(calibration_value)
        cal_values1[line]=calibration_value
        sum += calibration_value
    print(sum)

print (sum)


