tokens = [
    ["IDENTIFIER", "y"],
    ["EQUALS", "="],
    ["IDENTIFIER", "x"],
    ["PLUS", "+"],
    ["NUMBER", "3"],
    ["SEMICOLON", ";"]
]
keywords = ["if", "else", "for", "while", "return", "function", "print"]
assignitionOperators = ["EQUALS", "PLUS_EQUALS", "MINUS_EQUALS", "SLASH_EQUALS", "STAR_EQUALS"]
currentPosition = 0
expression = []

def parseAssignement():
    global currentPosition
    currentPosition = 0
    expression = []
    hasSemicolon = False

    for i in range(len(tokens)):
        if tokens[i][0] == "SEMICOLON":
            hasSemicolon = True

    if not hasSemicolon:
        return False

    if tokens[currentPosition][0] != "IDENTIFIER":
        return False
    currentPosition += 1
    if tokens[currentPosition][0] not in assignitionOperators:
        return False
    currentPosition += 1

    if tokens[currentPosition][0] != "NUMBER" and tokens[currentPosition][0] != "IDENTIFIER":
        return False
    

    while tokens[currentPosition][0] != "SEMICOLON":
        expression.append(tokens[currentPosition][1])
        currentPosition += 1
    currentPosition += 1
    return True



print(parseAssignement())