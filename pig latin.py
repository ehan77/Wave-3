# INPUTS 

linetext = input("Type a sentence to translate into Pig Latin. \n")
vowels = ['a' , 'e' , 'i' , 'o' , 'u']

words = linetext.split()
for i, word in enumerate(words) :
    letters = list(word)
    first_vwl = 0
    for j, letter in enumerate(letters) :
        if letter.lower() in vowels :
            first_vwl = j
    if first_vwl == 0 :
        word = word + "yay"
    else :
        word = word[first_vwl:len(word)] + word[0:first_vwl] + "ay"
    words[i] = word.lower()
linetext = " ".join(words)
print(linetext)