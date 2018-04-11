#!/usr/bin/env bash
cd /home/deyangchu/Documents/python-spider/cartoon/cartoon
rm -rf /home/deyangchu/manga/*
scrapy crawl comic
python3 push2Kindle.py
rm -rf /home/deyangchu/manga/*