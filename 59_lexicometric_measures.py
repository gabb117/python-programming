#a program that calculate lexicometric measures of an italian text


def load_text(filename):
    #open file
    f = open(filename,'r')
    #create string with file text
    body = "" #empty variable to contain the text
    for r in f: #read all lines of text
        body += r #read line is added to variable 'body' which concatenates each line read by the loop
    f.close() # close the file
    return body # return variable 'body'


def normalize_text(text):
    #capitalization normalization, all characters in the text are converted to lowercase by the lower() method
    text = text.lower()

    #punctuation transformation, all characters of punctuation are converted in space character
    punctuation = "''" + '-:[](),;!?/\n\t'

    for c in punctuation:
        text = text.replace(c, " ") #replaces the various characters with the space via a loop

    return text #returns the normalized text


def token_measure(text):
    #transformation into a list of sentences
    list_ph = text.split(". ")
    n_list_ph = len(list_ph)
    #accumulate the length of sentences
    l_ph = 0
    #token/word count
    nt = 0
    #token dictionary, structured: (token1: (af1,rf1), token2: (af2, rf2),...)
    dtoken = {}
    #Tokenization of sentences in the dictionary
    for p in list_ph:
        p = p.strip()
        ltoken = p.split()
        for t in ltoken:
            if t not in dtoken:
                dtoken[t] = [1,0.0]
            else:
                dtoken[t] [0] += 1
            nt += 1
    #calculation of relative frequency

    for t in dtoken:
        dtoken[t] [1] = float(dtoken[t] [0]) / float(nt)
    
    return n_list_ph,nt,l_ph/n_list_ph , dtoken

def print_measure(n_phrases, N, len_med_ph, dtoken):
    #number of distinct tokens in the text
    V = len(dtoken)
    print("Sentences number: ",n_phrases)
    print("Average sentence length: %0.6f", len_med_ph)
    print("Length in words N: ", N)
    print("Vocabulary size V: ",V)
    print("Lexical richness V/N: %0.6f" % (V/N))
    #builds a list from the dictionary to sort it
    l = []
    for k in dtoken:
        af = int(dtoken[k][0])
        rf = dtoken[k][1]
        l = l + [(af, k, rf)]
    #sorting of the list
    l.sort(reverse = True)
    #Print the list header on the screen
    print("(:^30)".format("Token"),"(:^4)".format("af"),"(:^8)".format("ef"),"{:^4}".format("len"),sep="")
    #print the list
    for e in l:
        print("(:<30)".format("Token"),"(:^4)".format(e[0]),"(:^0.6f)".format(e[2]),"{:^4}".format(len(e[1])),sep="")
   
    
        

def main():
    filename = input("Enter filename: ")
    text = load_text(filename)
    text = normalize_text(text)
    n_phrases, N, len_med_ph, dtoken = token_measure(text)
    print_measure(n_phrases, N, len_med_ph, dtoken)

    print("Exit program!")

main()


