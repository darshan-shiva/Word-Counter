class Exception(Exception):
    pass

def output(count):                          #print the word count
    print("Word count in the given sentence/paragraph:")
    print(count)

def count(sentence):                        #function to calculate the count
    freq = {}                               #dictionary to store the count of each word
    for line in sentence.splitlines():      #spliting the lines from the paragraph
        words = line.split()                #extracting the words from a line
        for w in words:                     
            if w:                           
                w = w.strip(',.?!').capitalize()        #removing all special characters and capitalizing them
                if w.isalpha():                         #checking if word contains on alphabets
                    freq[w] = freq.get(w,0)+1           #accessing the word from the dictionary and incrementing its count

                else:                        #if sentence contains numbers and terminates the program
                    print("Sentence contains numbers which is invalid.")
                    exit()
        return freq

def accept():                               #function to input sentence or paragraph
    return input("Enter Sentence or paragraph: \n")

def main():
    sentence = accept()
    word_count = count(sentence)
    output(word_count)

if __name__ == '__main__':
    main()