import tagme
import os
import pandas as pd
import burst_detection 

tagme.GCUBE_TOKEN =  'd4898143-1266-403d-95a6-95104f701255-843339462'
file_path = os.getcwd() + '/data/'
topics = []

for file in os.listdir(file_path):
    path = os.path.join(file_path, file)

    f = open(path, "r")

    text = ''
    for line in f:
        text.append(line)
    
    lunch_annotations = tagme.annotate(text)
    for ann in lunch_annotations.get_annotations(0.1):
        topics.append(ann)

posts = pd.DataFrame(topics,columns=['topics'])


