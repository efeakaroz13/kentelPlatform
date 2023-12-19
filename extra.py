import random

def generate_id(charNumber):
    alphabet = "thequickbrownfoxjumpedoverthelazydog"
    a = []
    for _ in alphabet:
        a.append(_)
    output = ""
    for i in range(charNumber):
        intorchar = random.randint(0,1)
        if intorchar == 1:
            #char
            selectedChar = random.choice(a)
            upperOrLower = random.randint(0,1)
            if upperOrLower == 1:
                selectedChar = selectedChar.upper()
            output += selectedChar

        if intorchar == 0:
            num = random.randint(0,9)
            num = str(num)
            output+=num

    return output

if __name__ == "__main__":
    print(generate_id(25))
