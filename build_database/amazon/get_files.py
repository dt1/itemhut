#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re

import os.path
import sys
import glob

sys.path.append("/itemhut/pydb/")
import dbconn

def find_links(sfile):
    for link in sfile.find_all("a"):
        candidate_link = link.get("href")
        if (candidate_link is not None
            and "Flat.File" in candidate_link):
            yield candidate_link

def save_excel_files(sfile):
    for link in find_links(sfile):
        xfile = requests.get(link)
        junk, sep, name = link.partition("Flat.File.")
        file_name = "{0}{1}".format(sep, name)
        if xfile:
            with open("us/" + file_name, "wb") as ofolder:
                ofolder.write(xfile.content)
                ofolder.close()

def start_excel_saves():
    flat_file_page = requests.get("http://www.amazon.com/gp/help/customer/display.html?nodeId=200186090")
    file_soup = BeautifulSoup(flat_file_page.text, "lxml")
    save_excel_files(file_soup)
    print("success")

start_excel_saves()
