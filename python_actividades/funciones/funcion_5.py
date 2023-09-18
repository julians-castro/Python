def invertir():
    string = input("Dime la frase para invertirlo: ")
    string_reversed = ""
    for i in string:
        string_reversed = i + string_reversed
        
    return string_reversed
print(invertir())