from collections import Counter
from os import walk
from tika import parser

cvs = []
for (dirpath, dirnames, filenames) in walk('./cv/'):
    cvs.extend(filenames)
    
items = ['linux','cloud','container','docker','terraform','git']

results = {
    'linux'         : ['linux','debian','centos','rhce','ubuntu'],
    'cloud'         : ['cloud','aws','azure','gcp'],
    'git'           : ['git'],
    'container'     : ['container','docker','lxc'],
    'cicd'          : ['cicd','gitlab','automate','terraform','ansible','automation'],
    'monitoring'    : ['monitoring'],
    'documentation' : ['documentation']
}

data = ""
for cv in cvs:
        cv = './cv/' + cv
        raw = parser.from_file(cv)
        cnt = str(raw['content']).lower().replace(",",'').replace(".",'').replace("/",' ')
        cnt = cnt.split()
        counts = Counter(cnt)
        
        line = ""
        for item in items:
            line = line + str(counts[item]) + ','
        
        output = ""
        total = 0
        for result in results:
            res = 0
            for i in results[result]:
                if(counts[i] > 0):
                    res = 1
                    total += res
                    break
            output += str(res) + ','
        #data += "%s %s %i\t\t\t%s\n" % (line,output,total,cv)
        data += "%s %i\t\t\t%s\n" % (output,total,cv)
        
f = open("./data.txt", "w")
f.write(data)
print(data)
f.close()
