import os
import re
import pickle

def fit(prefix_count = 2, data = 'data'):
    text = ''
    for file in os.listdir(data):
        with open(os.path.join(data, file), 'r', encoding='UTF-8') as f:
            text += ' ' + f.read()

    text = text.lower()
    array = re.findall(r'\w+', text)

    dic = {}
    for i in range(len(array)-prefix_count):
        if tuple(array[i:i+prefix_count]) not in dic.keys():
            dic[tuple(array[i:i+prefix_count])] = [1,{array[i+prefix_count]:1}]
        else:
            if array[i+prefix_count] in dic[tuple(array[i:i+prefix_count])][1]:
                dic[tuple(array[i:i + prefix_count])][1][array[i+prefix_count]] +=1
            else:
                dic[tuple(array[i:i + prefix_count])][1][array[i + prefix_count]] = 1
            dic[tuple(array[i:i + prefix_count])][0] += 1



    for prefix in dic.keys():
        probabilities=[]
        for word in dic[prefix][1].keys():
            probabilities.append([word, dic[prefix][1][word] / dic[prefix][0]])
        dic[prefix] = probabilities

    with open('model/model.pickle', 'wb') as f:
        pickle.dump(dic, f)