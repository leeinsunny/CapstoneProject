import os
import requests
import json
import re
import pandas as pd
import time


def run(fileName):
  start =time.time()
  print("---Slang module processing---")

  # Read slang dict and sort by length
  slang_dict = pd.read_excel("modules/slang/slang_dict_v2.xlsx")
  sorted_slangs = sorted(slang_dict['slang'], key=len, reverse=True)

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
        print(f"target sentence: {target}")
        for s in sorted_slangs:
          target = target.replace(s, "*"*len(s))
        nf.write(target+'\n')
    #f.close()
  #nf.close()
  end = time.time() 
  print(f"{end-start:.5f}sec")

if __name__ == "__main__":
  run("fake.txt")