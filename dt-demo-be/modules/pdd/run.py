import re
import argparse
import os

pattern_dict = {
    "res_num": {
        "pattern": r"\b\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\-?\d{7}\b|\b\d{6}\d{7}\b",
        "type": "주민등록번호",
        "replacement": "******-*******"
    },
    "phone_num": {
        "pattern": r'010-\d{4}-\d{4}',
        "type": "전화번호",
        "replacement": "010-****-****"
    }
}

def run(fileName):
    print("---Personal data detection module processing---")

    # Find input file from database directory
    db_dir = os.path.join("..", "database")
    file_dir = os.path.join(db_dir, fileName)
    print(file_dir)

    # Replace and save as new file
    newFileName = fileName.replace(".txt", "_filtered.txt")
    new_file_dir = os.path.join(db_dir, newFileName)
    with open(new_file_dir, "w+", encoding='utf-8') as nf:
        with open(file_dir, "r", encoding='utf-8') as f:
            for line in f:
                target=line.strip()

                for pattern in pattern_dict:
                    if re.search(pattern_dict[pattern]["pattern"], target):
                        print(f'{pattern_dict[pattern]["type"]} detected on target sentence:')
                        print(f"{target}")
                        target = re.sub(pattern_dict[pattern]["pattern"], pattern_dict[pattern]["replacement"], target)

                nf.write(target+'\n')
        f.close()
    nf.close()