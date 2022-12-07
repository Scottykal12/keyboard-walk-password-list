import sys
#import itertools

# unshifted rows
numRow = ["1", "2", "3", "4", "5", "6", "6", "7", "8", "9", "0", "-"]
qwerRow = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
asdfRow = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
zxcvRow = ["z", "x", "c", "v", "b", "n", "m", ","]

# shifted rows
SHnumRow = ["!", "@",  "#", "$", "%", "^", "&", "*", "(", ")", "_"]
SHqwerRow = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
SHasdfRow = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
SHzxcvRow = ["Z", "X", "C", "V", "B", "N", "M", "<"]

# unshifted colums
col1 = list("1qaz")
col2 = list("2wsx")
col3 = list("3edc")
col4 = list("4rfv")
col5 = list("5tgb")
col6 = list("6yhn")
col7 = list("7ujm") 
col8 = list("8ik,")
col9 = list("9ol.")
col0 = list("0p;/")

# shift colums
SHcol1 = list("!QAZ")
SHcol2 = list("@WSX")
SHcol3 = list("#EDC")
SHcol4 = list("$RFV")
SHcol5 = list("%TGB")
SHcol6 = list("^YHN")
SHcol7 = list("&UJM")
SHcol8 = list("*IK<")
SHcol9 = list("(OL>")
SHcol0 = list(")P:?")

# I need to make an array of the arrarys

# need to save system output
ogStdout = sys.stdout


def fourCombo():
    with open('PasswordList.txt', 'w') as file:

        
        start = 0
        count = 4
        
        for i in numRow :
            if start < 7 :
                sys.stdout = file

                #join here?????
                num = ''.join(numRow[start:count])
                qwer = ''.join(qwerRow[start:count])
                SHnum = ''.join(SHnumRow[start:count])
                SHqwer = ''.join(SHqwerRow[start:count])

                combo = [num, qwer, SHnum, SHqwer]
                for j in combo :
                    for k in combo :
                        for l in combo :
                            for m in combo :
                                print(''.join(j+ k + l + m))
                start += 1
                count += 1

                sys.stdout = ogStdout


# only does 4 combos
def testCombo() :
    import itertools

    start = 0
    count = 4

    with open('PasswordList.txt', 'w') as file:

        for i in numRow : 
            if start < 7 :
                #dont hard choose count here
                num = ''.join(numRow[start:count])
                qwer = ''.join(qwerRow[start:count])
                SHnum = ''.join(SHnumRow[start:count])
                SHqwer = ''.join(SHqwerRow[start:count])

                combo = [num, qwer, SHnum, SHqwer]

                combinations = []

                for r in range(len(combo)+1):
                    for combination in itertools.combinations(combo, r):
                        combinations.append(combination)

                for iterations in combinations :
                    #print(''.join(i))
                    #print(iterations)
                    for j in iterations :
                        for k in iterations :
                            for l in iterations :
                                for m in iterations :
                                    sys.stdout = file
                                    print(''.join(j+ k + l + m))
                start += 1
                count += 1
                sys.stdout = ogStdout

def minCombo() :
    import itertools

    start = 0
    count = 4

    num = ''.join(numRow[start:count])
    qwer = ''.join(qwerRow[start:count])
    SHnum = ''.join(SHnumRow[start:count])
    SHqwer = ''.join(SHqwerRow[start:count])

    combo = [num, qwer, SHnum, SHqwer]

    combinations = []

    for r in range(len(combo)+1):
        for combination in itertools.combinations(combo, r):
            combinations.append(combination)

    for iterations in combinations :
        #print(''.join(i))
        print(iterations)

minCombo()
#fourCombo()
#testCombo()
#print(list("1qaz"))
