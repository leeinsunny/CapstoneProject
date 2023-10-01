import pandas as pd
import os

def run(fileName):
  print("---Slang module processing---")

  # Read slang dict and sort by length
  slang_dict = pd.read_excel("modules/slang/slang_dict_v3.xlsx")
  

  # Find input file from database directory
  db_dir = os.path.join("..", "database")
  file_dir = os.path.join(db_dir, fileName)
  print(file_dir)

  # Replace and save as new file
  newFileName = fileName.replace(".txt", "_filtered.txt")
  new_file_dir = os.path.join(db_dir, newFileName)
  with open(new_file_dir, "w+", encoding='utf-8') as nf:
    with open(file_dir, "r", encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
          target = line.strip()
          print(f"target sentence: {target}")

          for s, r in zip(slang_dict['slang'], slang_dict['replacement']):
              if s in target:
                  print(f"Detected slang: {s}, Replaced with: {r}")  # 로그에 출력
                  target = target.replace(s, r)  # 대체하여 저장
                  
          nf.write(target+'\n')
    f.close()
  nf.close()

if __name__ == "__main__":
  run("fake.txt")