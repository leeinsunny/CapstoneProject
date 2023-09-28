import os
import time
import pandas as pd

from collections import OrderedDict

def run(fileName):
    start =time.time()
    print("---Duplication detection module processing---")

    # Read Excel and save to ../database/fake.txt
    test_dict = pd.read_csv("modules/dup/seoul_freeboard.csv")
    with open("../database/fake.txt", "w", encoding='utf-8') as fd:
        for t in test_dict['content']:
            # print(t)
            line = t.split('\n')
            for l in line:
                fd.write(l)
    fd.close()

    # Find input file from database directory
    db_dir = os.path.join("..", "database")
    file_dir = os.path.join(db_dir, fileName)
    print(file_dir)

    # Replace and save as new file
    newFileName = fileName.replace(".txt", "_filtered.txt")
    new_file_dir = os.path.join(db_dir, newFileName)
    with open(new_file_dir, "w+", encoding='utf-8') as nf:
        sentences = []
        with open(file_dir, "r", encoding='utf-8') as f:
            for line in f:
                target=line.strip()
                sentences.append(target)
        f.close()

        no_dup = OrderedDict.fromkeys(sentences)
        for item in no_dup:
            nf.write(item+"\n")

    nf.close()
    end = time.time()
    print(f"{end-start:.5f} sec")
