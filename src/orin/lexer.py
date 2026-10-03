line = str(input())
currentCharacter = ""
tokens = []
keywords = ["if", "else", "for", "while", "return", "function"]
isNumberCurrently = False
isStringCurrently = False
isIdentifierCurrently = False

for i in line:

    # Spaces
    if i == " ":
        if isStringCurrently == False and isIdentifierCurrently == False:
            continue
        elif isStringCurrently:
            currentCharacter += i
            continue
    # Everything else

    # Numbers
    if isNumberCurrently:
        if i.isdigit():
            currentCharacter += i
            
        else:
            tokens.append(["NUMBER", currentCharacter])
            isNumberCurrently = False
            currentCharacter = ""
    # Strings
    elif isStringCurrently:
        if i == '"' or i == "'":
            if currentCharacter != "":
                tokens.append(["STRING", currentCharacter])
                isStringCurrently = False
                currentCharacter = ""
        else:
            currentCharacter += i
    elif isIdentifierCurrently:
        if i.isalpha() or i.isdigit() or i == "-" or i == "_":
            currentCharacter += i
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
        if i.isdigit():
            currentCharacter += i
            isNumberCurrently = True
        elif i.isalpha():
            currentCharacter += i
            isIdentifierCurrently = True
        elif i == '"' or i == "'":
            isStringCurrently = True
    # Misc tokens
    if i == "+":
        tokens.append(["PLUS", i])
    if i == "-":
        tokens.append(["MINUS", i])
    if i == "/":
        tokens.append(["SLASH", i])
    if i == "=":
        tokens.append(["EQUALS", i])
    if i == "*":
        tokens.append(["STAR", i])
    if i == ";":
        tokens.append(["SEMICOLON", i])
    if i == "(":
        tokens.append(["LEFT_PAR", i])
    if i == ")":
        tokens.append(["RIGHT_PAR", i])
    if i == "[":
        tokens.append(["LEFT_SQR", i])
    if i == "]":
        tokens.append(["RIGHT_SQR", i])
    if i == "{":
        tokens.append(["LEFT_CURL", i])
    if i == "}":
        tokens.append(["RIGHT_CURL", i])
        


if isNumberCurrently:
    tokens.append(["NUMBER", currentCharacter])
    isNumberCurrently = False
    currentCharacter = ""
elif isStringCurrently:
    tokens.append(["STRING", currentCharacter])
    isStringCurrently = False
    currentCharacter = ""

print(tokens)