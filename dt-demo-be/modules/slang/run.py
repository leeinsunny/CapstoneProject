import pandas as pd
import os

def run(fileName):
  # Read slang dict
  slang_dict = pd.read_excel("modules/slang/slang_dict_v1.xlsx")
  # for s in slang_dict["slang"]:
  #     print(s)

  # Find input file from database directory
  db_dir = os.path.join("..", "database")
  file_dir = os.path.join(db_dir, fileName)
  print(file_dir)

  # Replace and save as new file
  newFileName = fileName.replace(".txt", "_filtered.txt")
  new_file_dir = os.path.join(db_dir, newFileName)
  with open(new_file_dir, "x", encoding='utf-8') as nf:
    with open(file_dir, "r", encoding='utf-8') as f:
      for line in f:
        target=line.strip()
        for s in slang_dict["slang"]:
          target = target.replace(s, "*"*len(s))
        nf.write(target+'\n')

if __name__ == "__main__":
  run("fake.txt")