import sys

# First, get check the arguments that were received
# if len(sys.argv) != 4:
#     raise Exception("This tool should receive,\n1) action\t2) path to input text file\t3) path to output text file")
# action = sys.argv[1]
# inPath = sys.argv[2]
# outPath = sys.argv[3]

# print(f"Action: {action}, In Path: {inPath}, Out Path: {outPath}")


def main():
    makeDictionaryOfWords()


def readFile():
    # read the input
    with open("input.txt") as intxt:
        text = intxt.read()
        return text


def makeDictionaryOfWords():
    text = readFile()
    # first we split by spaces
    wordsList = text.split()
    print(wordsList)
    dic = {}
    for word in wordsList:
        if len(word) > 1:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    print(dic)
    gen = CharsGen()
    # TODO: deal with reverse words..


class CharsGen:
    def __init__(self):
        self.nextChar = None
        charList = []
        for i in range(33, 127):
            ch = chr(i)
            if not ch.isalpha() and not ch.isdigit():
                charList.append(ch)
        self.charsList = charList
        self.current_first = charList[0]
        self.current_second = charList[0]

    def getNextChar(self):
        symbol = f"{self.current_first}{self.current_second}"

        last_index = len(self.charsList) - 1
        second_index = self.charsList.index(self.current_second)
        first_index = self.charsList.index(self.current_first)

        if second_index != last_index:
            self.current_second = self.charsList[second_index + 1]
        elif first_index != last_index:
            self.current_first = self.charsList[first_index + 1]
            self.current_second = self.charsList[0]
        else:
            raise IndexError("No more characters can be generated.")
        return symbol


if __name__ == "__main__":
    main()
