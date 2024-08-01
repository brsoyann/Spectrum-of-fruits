def findparameterByType(linesList, parameterType):
    for line in linesList:
        if line.startswith(parameterType + ': '):
            return line[line.find(' ')+1:]
