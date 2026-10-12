line = str(input())
currentCharacter = ""
tokens = []
keywords = ["if", "else", "for", "while", "return", "function"]
assignmentOperators = ["+", "-", "*", "/"]
isNumberCurrently = False
isStringCurrently = False
isIdentifierCurrently = False
skipNext = False

for i in range(len(line)):
    if skipNext == True:
        skipNext = False
        continue
    # Spaces
    if line[i] == " ":
        if isStringCurrently == False and isIdentifierCurrently == False:
            continue
        elif isStringCurrently:
            currentCharacter += line[i]
            continue
    # Everything else

    # Numbers
    if isNumberCurrently:
        if line[i].isdigit():
            currentCharacter += line[i]
            
        else:
            tokens.append(["NUMBER", currentCharacter])
            isNumberCurrently = False
            currentCharacter = ""
    # Strings
    elif isStringCurrently:
        if line[i] == '"' or line[i] == "'":
            if currentCharacter != "":
                tokens.append(["STRING", currentCharacter])
                isStringCurrently = False
                currentCharacter = ""
        else:
            currentCharacter += line[i]
    elif isIdentifierCurrently:
        if line[i].isalpha() or line[i].isdigit()  or line[i] == "_":
            currentCharacter += line[i]
        else:
            if currentCharacter in keywords:
                tokens.append(["KEYWORD", currentCharacter])
                isIdentifierCurrently = False
                currentCharacter = ""
            else:
                tokens.append(["IDENTIFIER", currentCharacter])
                isIdentifierCurrently = False
                currentCharacter = ""
    # Everything else
    else:
        if line[i].isdigit():
            currentCharacter += line[i]
            isNumberCurrently = True
        elif line[i].isalpha():
            currentCharacter += line[i]
            isIdentifierCurrently = True
        elif line[i] == '"' or line[i] == "'":
            isStringCurrently = True
    # Misc tokens
    if line[i] == "+":
        if line[i + 1] == "=":
            tokens.append(["PLUS_EQUALS", "+="])
            skipNext = True
            continue
        tokens.append(["PLUS", line[i]])
    if line[i] == "-":
        if line[i + 1] == "=":
            tokens.append(["MINUS_EQUALS", "-="])
            skipNext = True
            continue
        tokens.append(["MINUS", line[i]])
    if line[i] == "/":
        if line[i + 1] == "=":
            tokens.append(["SLASH_EQUALS", "/="])
            skipNext = True
            continue
        tokens.append(["SLASH", line[i]])
    if line[i] == "=":
        tokens.append(["EQUALS", line[i]])
    if line[i] == "*":
        if line[i + 1] == "=":
            tokens.append(["STAR_EQUALS", "*="])
            skipNext = True
            continue
        tokens.append(["STAR", line[i]])
    if line[i] == ";":
        tokens.append(["SEMICOLON", line[i]])
    if line[i] == "(":
        tokens.append(["LEFT_PAR", line[i]])
    if line[i] == ")":
        tokens.append(["RIGHT_PAR", line[i]])
    if line[i] == "[":
        tokens.append(["LEFT_SQR", line[i]])
    if line[i] == "]":
        tokens.append(["RIGHT_SQR", line[i]])
    if line[i] == "{":
        tokens.append(["LEFT_CURL", line[i]])
    if line[i] == "}":
        tokens.append(["RIGHT_CURL", line[i]])
        


if isNumberCurrently:
    tokens.append(["NUMBER", currentCharacter])
    isNumberCurrently = False
    currentCharacter = ""
elif isStringCurrently:
    tokens.append(["STRING", currentCharacter])
    isStringCurrently = False
    currentCharacter = ""

print(tokens)