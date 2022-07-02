@echo off
cd C:\Users\Truls\Documents\git\scrape_finn
:loop
timeout 900
scrape_finn.py
goto loop