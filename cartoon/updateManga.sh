#!/bin/bash
PATH=$PATH:/usr/local/bin
export PATH

if [ ! -f data.json ]; then
    echo '{"comic": "", "filenum": "0", "eptitle": ""}' > data.json
    echo "Edit config file!"
    break
fi

rm -rf ./manga/*
scrapy crawl comic
python3 push2Kindle.py