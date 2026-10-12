tokens = [
    ["IDENTIFIER", "x"],
    ["MINUS_EQUALS", "-="],
    ["NUMBER", "y"],
    ["SEMICOLON", ";"]
]
keywords = ["if", "else", "for", "while", "return", "function"]
assignitionOperators = ["EQUALS", "PLUS_EQUALS", "MINUS_EQUALS", "SLASH_EQUALS", "STAR_EQUALS"]
currentPosition = 0
expression = []

def parseAssignement():
    global currentPosition

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