# API researching

### 1. Requirements:
- Every APIs must run in python environment
- Every file names are _APItype.py_: i.e. typo.py
- Every file should contain _main_ function to run sample usage.

### 2. Input
Regarding text data as an input for using each API, use following convention using **arguments** for API verification:  
``` shell
python {api_test_file} --input {input text}
```

### 3. Output
Every sample output should be tested through running apiRuns.sh file: `bash apiRuns.sh`
``` bash
function {api_name} {
    apiRet=`python {api_test_file} --input {input text}`
    echo "api result: ${apiRet}"
}
```

### 4. Virtual Environment
__Setting up virtual environment:__
1. Create virtual environment under /API_reference:  
`% python3 -m venv .venv`  
2. Activate virtual environment:  
`% source .venv/bin/activate`
3. Upgrade Pip:  
`(.venv) % pip install --upgrade pip`
4. Necessary package:  
    - Slang API(google perspective API)
        - `(.venv) % pip install google-api-python-client`
<!-- `(.venv) % pip install py-hanspell` -->
<!-- TODO: update package installation commend here -->
