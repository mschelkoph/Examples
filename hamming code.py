import random

def parityBit(DataLength):

    length = len(DataLength)
    
    for x in range(length):
        if 2**x >= length + x + 1:
            break
    return x

def calculateParity(UserBin, ParityBitCount):

    UserList = list(reversed(UserBin))
    BinList = []
    Remaining = 1
    num = 1

    # insert and create visual representation into User List
    for x in range(ParityBitCount):
        UserList.insert((2**x) - 1, 'PB ' + str(x + 1))

    print('\nParity bit locations:\n', list(reversed(UserList)))

    # creating a list of bit locations with correct formating   
    for x in range(len(UserList)):
        BinList.append(format(x + 1, '0' + str(ParityBitCount) + 'b'))

    print('\nBinary for total amount of bits:\n', list(reversed(BinList)), '\n')

    # created an identical user input list to make changes to so
    # UserList remains the same for the for loops
    ParityList = UserList[:]

    # initial loop to set a parity bit to check
    for x in range(ParityBitCount, 0, -1):
        Count = 0
        ParityNum = 0

        # secondary loop to check against the UserList
        for y in UserList:

            # Variable to get the current bit location being checked
            Current = BinList[Count]

            # comparing the bit location and UserList to check for parity
            if 'PB' in y:
                pass
            elif int(Current[x - 1]) == 1 and int(y) == 1:
                ParityNum = ParityNum + 1

            Count = Count + 1

        print('Parity count for PB ' + str(num) + ': ' + str(ParityNum))

        # Replacing PB in ParityList with the necessary parity bit
        index = ParityList.index('PB ' + str(Remaining))
        
        if ParityNum % 2 == 0:
            ParityList[index] = '0'
        else:
            ParityList[index] = '1'

        # showing all the parity bits for each location
        print('PB ' + str(num) + ' = ' + ParityList[index], '\n')

        Remaining = Remaining + 1
        num = num + 1

    # reversing list to correct order
    ParityList = list(reversed(ParityList))

    # making that list into a string to return
    HammingValue = ''.join(str(x) for x in ParityList)

    return HammingValue

def calculateError(newNum, ParityCount):

    ErrorCode = list(reversed(newNum))
    BinList = []
    Location = 0

    ErrorCodeString = ''.join(str(x) for x in list(reversed(ErrorCode)))
    print('\nCorrect code:            ' + ErrorCodeString)

    # Creating random error
    RandomNum = random.randint(0, len(ErrorCode) - 1)

    if ErrorCode[RandomNum] == '1':
        ErrorCode[RandomNum] = 0
    else:
        ErrorCode[RandomNum] = 1

    ErrorCodeString = ''.join(str(x) for x in list(reversed(ErrorCode)))
    print('Code with one wrong bit: ' + ErrorCodeString)

    # creating a list for each binary location
    for x in range(len(ErrorCode)):
        BinList.append(format(x + 1, '0' + str(ParityCount) + 'b'))
        
    num = 0

    #checking the correct code with the error code
    for x in range(ParityCount, 0, -1):
        Total = 0
        Count = 0
        
        for y in ErrorCode:
            Current = BinList[Count]
            
            if int(Current[x-1]) == 1 and int(y) == 1:
                Total = Total + 1

            Count = Count + 1

        if Total % 2 != 0:
            Location = Location + 2 ** num
            print('\nParity bit for position ' + str(2 ** num) + ' is odd')

        num = num + 1

    print('\nThe bit location with the Error is (counting from the right): ' + str(Location))
            

##### MAIN #########################################################

UserBin = input('enter binary number (q to quit):')
while UserBin != 'q':
    ParityBitCount = parityBit(UserBin)

    Result = calculateParity(UserBin, ParityBitCount)

    print('\nThe data with error correction is: ' + Result)

    UserBin = input('\nDo you want to calculate for a single random error? (y/n): ')

    if UserBin == 'y':
        calculateError(Result, ParityBitCount)
    elif UserBin == 'n':
        pass

    UserBin = input('\nenter binary number (q to quit):')




    
