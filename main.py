import sys

# First, get check the arguments that were received
# if len(sys.argv) != 4:
#     raise Exception("This tool should receive,\n1) action\t2) path to input text file\t3) path to output text file")
# action = sys.argv[1]
# inPath = sys.argv[2]
# outPath = sys.argv[3]

# print(f"Action: {action}, In Path: {inPath}, Out Path: {outPath}")

with open("input.txt") as intxt:
    text = intxt.readlines()
    print(text)
# detect sequences
def detection(text):
    for line in text:
        words = str(line).split(" ")
