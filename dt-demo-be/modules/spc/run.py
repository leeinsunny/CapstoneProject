import pandas as pd
import os
import time
import emoji


def run(fileName):
    
    print("---Special character replacing module processing---")
    
    # Read Excel and save to ../database/fake.txt
    test_data = pd.read_excel("../database/dataset.xlsx")
    with open("../database/demo.txt", "w", encoding='utf-8') as fd:
      for t in test_data['document']:
            line = t.split('\n')
            for l in line:
                  fd.write(l)
    fd.close()
    
    # module processing start
    start = time.time()

    # Read spc_dict
    spc_dict = pd.read_excel("modules/spc/spc_dict_v1.xlsx")
  
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
                # TODO: emoji logic if-else
                target=emoji.demojize(target)
                for s in spc_dict['spc']:
                    target = target.replace(s, '')
                nf.write(target+'\n')
        f.close()
    nf.close()
    
    # module processing end
    end = time.time()
    
    print(f"Total running time of spc module: {end-start:.5f} sec")
