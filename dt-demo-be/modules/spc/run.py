import os

def run(fileName):
    print("---Special character substitution module processing---")

    # Find input file from database directory
    db_dir = os.path.join("..", "database")
    file_dir = os.path.join(db_dir, fileName)
    print(file_dir)

    # Replace and save as new file
    newFileName = fileName.replace(".txt", "_filtered.txt")
    new_file_dir = os.path.join(db_dir, newFileName)
    with open(new_file_dir, "w+", encoding='utf-8') as nf:
        with open(file_dir, "r", encoding='utf-8') as f:
            # TODO: Implement spc substitution logic
            for line in f:
                nf.write(line)
        f.close()
    nf.close()
    