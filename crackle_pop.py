
# Adam Zivitofsky adam.zivitofsky@outlook.com
# print out numbers 1 to 100 (inclusive).
# If the number is divisible by 3, print Crackle instead of the number.
# If it's divisible by 5, print Pop.
#If it's divisible by both 3 and 5, print CracklePop.
# was not entriely clear if you wantd to print number and CracklePop (and Pop)

for rangeNumber in range (1,1001):

    if (rangeNumber % 15 == 0):
        # if number is divisible by 3 & 5 it is divisible by 15, so mod 15 => 0
        print rangeNumber, "CracklePop"
    elif (rangeNumber % 3 == 0):
        # if number is divisible by 3, mod 3 will be 0
            print "Crackle"
    elif (rangeNumber % 5 == 0 ):
        # if number is divisible by 5, mod 5 will be 0
            print rangeNumber, "Pop"
    else:
            print rangeNumber
