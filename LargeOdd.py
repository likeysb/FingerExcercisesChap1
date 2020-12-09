#ex 2 - ask users to input a list of ints and pick greatest odd int
numYs = int(input('How many integers u wanna input'))
SK88 = []
LargeOdd = 0
for i in range(0,numYs):
    SK88[i] = int(input('enter num:')
    if (SK88[i] % 2 == 1 and SK88[i] > LargeOdd) :
        LargeOdd = SK88[i]
print(LargeOdd)
