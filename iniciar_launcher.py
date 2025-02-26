#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
from threading import Thread
import time
import webbrowser

def start_navigator():
    time.sleep(5)
    webbrowser.open(url)

puerto = "8888"

url = "http://localhost:" + puerto

print("[!] Iniciando Quick Launcher ...\n")

thread_navigator = Thread(target=start_navigator)
thread_navigator.start()

cmd = "python -m flask --app main.py run --port=8888"

call(cmd)