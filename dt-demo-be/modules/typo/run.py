import os
import requests
import json
import re

def run(fileName):
    print("---Typo module processing---")

    # Find input file from database directory
    db_dir = os.path.join("..", "database")
    file_dir = os.path.join(db_dir, fileName)
    print(file_dir)

    # Replace and save as new file
    newFileName = fileName.replace(".txt", "_filtered.txt")
    new_file_dir = os.path.join(db_dir, newFileName)

    contents = ""
    with open(new_file_dir, "w+", encoding='utf-8') as nf:

        print("Reading from original contents ...")
        with open(file_dir, "r", encoding='utf-8') as f:
            for line in f:
                target=line.strip()
                contents += target
        f.close()

        print("Fetching errors ...")
        contents = contents.replace('\n', '\r\n')
        response = requests.post('http://164.125.7.61/speller/results', data={'text1': contents})
        data = response.text.split('data = [', 1)[-1].rsplit('];', 1)[0]

        # Initialize storage to match typo and expected(correct) word
        typo_detected = []

        # Catch Json decode error if API response is unexpected data type
        try:
            '''
            Here loads typo response,
            and match typo words to the expected(correct) words
            '''
            data_dict = json.loads(data)
            err_info = data_dict['errInfo']
            for err in err_info:
                typo_detected.append("typo: "+err["orgStr"]+", "+"expected word: "+err["candWord"])
        except json.JSONDecodeError as e:
            if "찾지 못한 맞춤법 오류나 문법 오류" in data:
                # When error has not detected from the API:
                print("Given input data seems clean enough")

        print("Replacing errors ...")
        # Typo replacement
        # get dictionary from given text
        # ex input
        # typo: 더워요옷의, expected word: 더워요. 옷의
        # typo: 이뿐데, expected word: 이쁜데
        # typo: 더우네요, expected word: 덥네요|더 우네요
        # ex dict
        # {'더워요옷의': ['더워요. 옷의'], '이뿐데': ['이쁜데'], '더우네요': ['덥네요', '더 우네요']}
        dictionary = {}
        for line in typo_detected:
            if line.startswith('typo:'):
                parts = line.split(', expected word:')
                typo = parts[0].replace('typo:', '').strip()
                expected_words = parts[1].strip()
                if '|' in expected_words:
                    expected_words = expected_words.split('|')
                else:
                    expected_words = [expected_words]
                dictionary[typo] = expected_words

        for key , value in dictionary.items():
            if key in contents:
                contents = contents.replace(key, value[0])
                
        pattern = r'(?<=[.?!])\s+'
        # 문장의 끝마다 '\n' 추가
        # TODO: verify if it's needed
        contents = re.sub(pattern, '\n', contents)
        nf.write(contents)
    nf.close()

if __name__ == "__main__":
    run("fake.txt")