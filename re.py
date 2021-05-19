import re

handle = open(regex_sum_1034951.txt,'w')
x=list
for line in handle:
    y = re.findall('[0-9]+', line)
    x = x + y
    sum = 0
    for number in x :
        sum = sum + int(number)
print(sum)
