def checkStrength(input_password):
    inputLength=len(input_password)
    hasLower = False
    hasUpper = False
    hasDigit = False
    symbols='!+-=?#%*@&^$_'
    hasSymbols=False
    for i in range(inputLength):
        if input_password[i].islower():
            hasLower= True
        if input_password[i].isupper():
            hasUpper=True
        if input_password[i].isdigit():
            hasDigit=True
        if input_password[i] in symbols:
            hasSymbols=True
    print("Strength of password : ", end= "")
    if(hasLower and hasUpper and hasDigit and hasSymbols and inputLength>11):
        print("Strong")
        return "Strong"
    elif(((hasLower and hasUpper and hasDigit) or (hasUpper and hasDigit and hasSymbols) or (hasLower and hasDigit and hasSymbols) or (hasUpper and hasLower and hasSymbols)) and 8<=inputLength<=11):
        print("Medium")
        return "Medium"
    else:
        print("POOR")
        return  "Poor"

if __name__=="__main__":
    input_Something= input("Enter your password:")
    checkStrength(input_Something)

        


