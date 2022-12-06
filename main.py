import sys

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

# I need to make an array of the arrarys


# need to save system output
ogStdout = sys.stdout


def fourCombo():
    with open('PasswordList.txt', 'w') as file:
        sys.stdout = file
        
        start = 0
        count = 4
        
        num = numRow[start:count]
        qwer = qwerRow[start:count]
        SHnum = SHnumRow[start:count]
        SHqwer = SHqwerRow[start:count]

        combo = [num + qwer + SHnum + SHqwer]
        this = ''.join(combo)

        for i in numRow :
            if start < 7 :
                print(this) 
                start += 1
                count += 1

        sys.stdout = ogStdout
        #for i in combo : 

fourCombo()