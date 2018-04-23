#!/bin/bash
PATH=$PATH:/usr/local/bin
export PATH
rm -rf ./manga/*
scrapy crawl comic
python3 push2Kindle.py