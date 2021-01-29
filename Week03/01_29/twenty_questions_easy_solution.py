
import json

def is_answer_node(node):  #added "node"
    return len(node) == 1


f = open('../data/questions.json') #correct path
content = f.read() # missing brackets

node = json.loads(content)   # loads instead of reads

finished = False

while not finished: #missing :
    print(node['text']) #missing bracket

    if is_answer_node(node):   #indentation for whole portion added
        finished = True
    else:
        answer = input()   #deleted one =
        if answer.lower() in ['yes', 'y']:  #lower instead of upper
            node = node['yes']   #swapped with node[no]
        else:
            node = node['no']
