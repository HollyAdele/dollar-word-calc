prices = {"a": 1,
          "A": 1,
          "b": 2,
          "B": 2,
          "c": 3,
          "C": 3,
          "d": 4,
          "D": 4,
          "e": 5,
          "E": 5,
          "f": 6,
          "F": 6,
          "g": 7,
          "G": 7,
          "h": 8,
          "H": 8,
          "i": 9,
          "I": 9,
          "j": 10,
          "J": 10,
          "k": 11,
          "K": 11,
          "l": 12,
          "L": 12,
          "m": 13,
          "M": 13,
          "n": 14,
          "N": 14,
          "o": 15,
          "O": 15,
          "p": 16,
          "P": 16,
          "q": 17,
          "Q": 17,
          "r": 18,
          "R": 18,
          "s": 19,
          "S": 19,
          "t": 20,
          "T": 20,
          "u": 21,
          "U": 21,
          "v": 22,
          "V": 22,
          "w": 23,
          "W": 23,
          "x": 24,
          "X": 24,
          "y": 25,
          "Y": 25,
          "z": 26,
          "Z": 26,
          "0": 0,
          "1": 1,
          "2": 2,
          "3": 3,
          "4": 4,
          "5": 5,
          "6": 6,
          "7": 7,
          "8": 8,
          "9": 9,
          "-": 0,
          "&": 0,
          ",": 0,
          "'": 0,
          ".": 0,
          "/": 0,
          "!": 0}

a_file = open("/dictionary.py", "r")
              
lines = a_file.read()
dictionary = lines.splitlines()

a_file.close()

count = 0
dollar_words = []
for index in range(0, len(dictionary)):
    word = dictionary[index]
    list_of_letters = list(word)
    total = 0
    
    for letter in range(0, len(list_of_letters)):
        
        price = prices[list_of_letters[letter]]
        total += price
    
    
    if total == 100:
        #print(word)
        #count += 1
        dollar_words.append(word)
#print(dollar_words)
print(len(dollar_words))

file_string = ""
for each in range(0, len(dollar_words)):
    file_string = file_string + "\n" + dollar_words[each]


f = open("/dollar-word-list.py", "w")
f.write(file_string)
f.close()
        
        #run through list and unsplit lines, concatenating with new line character
        #file.write pass in file name
