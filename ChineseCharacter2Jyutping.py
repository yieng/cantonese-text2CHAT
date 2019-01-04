import pycantonese as pc
corpus = pc.hkcancor()
from pprint import pprint
import pprint
import collections

# Input a file containing the Chinese characters
file_in = input('Please input the name of the file (no .txt) containing Traditional Chinese characters:\n>> ')

with open(file_in+'.txt','r',encoding="utf-8") as fi:
    for SampleSentence in fi:
    
        # Get the length of the input sentence
        lenSampSent = len(SampleSentence)

        # Define a dictionary to store the Jyutping entries of the words
        searchResult = {}

        # Extract the individual Chinese characters and their Jyutping to the dictionary
        for c in range(lenSampSent):
            char = SampleSentence[c]
            sR_raw = corpus.search(character=char)
            sR_all = sorted(sR_raw, key=lambda tup:len(tup[0]))
            
            sR_uniq = list(dict.fromkeys(sR_all))
            searchResult[char] = sR_uniq

        # Write the results to a text file inside the specificed directory above
        sR = collections.OrderedDict(sorted(searchResult.items()))
        f = open(file_in+'_output'+'.txt','a',encoding="utf-8")
        pp = pprint.PrettyPrinter(indent=4,stream=f)
        for c in range(lenSampSent):
            char = SampleSentence[c]
            locChar = '\"'+char+'\" '+str(c+1)+'/'+str(lenSampSent)+' ----------------'
            pp.pprint(sR[char])
            pp.pprint(locChar)
        f.close()

        
