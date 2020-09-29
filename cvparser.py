from collections import Counter
import tokenize
from os import walk
from tika import parser

cvs = []
for (dirpath, dirnames, filenames) in walk('./cv/'):
    cvs.extend(filenames)

for cv in cvs:
        cv = './cv/' + cv
        raw = parser.from_file(cv)
        cnt = str(raw['content']).lower()
        cnt = cnt.split()
        counts = Counter(cnt)
        print(counts['linux'])
        
        f = open("./tmp/" + cv + '.input.txt', "a")
        f.write(str(counts))
        f.close()
