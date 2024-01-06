import sys
vowels = 'aeiou'
while True:
    word = input("Enter your word : ")
    
    if word[0] in vowels:
        pig_latin = word + 'way' 
    else:
        pig_latin = word[1:] + word[0] + 'ay'

    print("\nyour new pig_latin word")
    print((pig_latin),'\n')

    try1 = input('enter for another try or (press n to stop)\n')
    if try1.lower() == 'n':
        sys.exit()
