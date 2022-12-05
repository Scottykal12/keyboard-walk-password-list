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


# need to save system output
ogStdout = sys.stdout


def fourCombo():
    with open('PasswordList.txt', 'w') as file:
        sys.stdout = file

        for i in (numRow[0:4] + qwerRow[0:4] + SHnumRow[0:4] + SHqwerRow[0:4]):
            print(i)

        sys.stdout = ogStdout


fourCombo()

#test = numRow + qwerRow + SHnumRow +SHqwerRow

# print(asdfRow)
