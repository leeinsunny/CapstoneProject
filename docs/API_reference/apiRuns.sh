#!/bin/bash

function virtualEnv {
    source .venv/bin/activate
}

function slang {
    slangRet=`python slang/slang.py --input "fuck you"`
    echo "slang result: ${slangRet}"
}

virtualEnv
slang