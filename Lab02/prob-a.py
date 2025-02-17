from sys import stdin

def decodemassage(phrase: str):
    words = phrase.split()
    char_index, message = 0, ""
    for word in words:
        if char_index < len(word):
            message += word[char_index]
            char_index += 1
    return message

def processParagraph(no_case):
    print("Case #{}:".format(no_case))
    line = stdin.readline().strip()
    while line:
        print(decodemassage(line))
        line = stdin.readline().strip()
    print()

def main():
    no_cases = int(stdin.readline().strip())
    stdin.readline().strip()
    for paragraph_index in range(no_cases):
        processParagraph(paragraph_index + 1)
main()