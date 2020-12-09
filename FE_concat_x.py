#finger excercises at the end of chapter 2 in Intro to Programming 2nd ed Guttag
#ex 1 - take user input of number they want a string concatenated
numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
while(numXs != 0):
    toPrint = toPrint + 'X'
    numXs = numXs - 1
print(toPrint)
