from selenium import webdriver
import time
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import sys, codecs

class escrito:

    def capturing(self):
        if sys.stdout.encoding != 'cp850':
            sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
        if sys.stderr.encoding != 'cp850':
            sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')
        url = "https://pt.savefrom.net/download-from-tiktok"
        req = requests.get(url)
        req = req.text
        with open("index.html", "w+") as f:
            f.write(req)

hehe = escrito()
hehe.capturing()