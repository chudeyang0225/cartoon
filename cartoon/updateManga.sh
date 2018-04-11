#!/usr/bin/env bash
rm -rf ./manga/*
scrapy crawl comic
python3 push2Kindle.py
rm -rf ./manga/*