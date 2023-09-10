import os
from collections import OrderedDict

def run(fileName):
    print("---Duplication detection module processing---")

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