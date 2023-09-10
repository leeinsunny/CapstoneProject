import pandas as pd
import os

def run(fileName):
  # Find input file from database directory
  db_dir = os.path.join("..", "database")
  file_dir = os.path.join(db_dir, fileName)
  print(file_dir)
  with open(file_dir, "r", encoding='utf-8') as f:
    for line in f:
      print(line.strip())

if __name__ == "__main__":
  run("fake.txt")