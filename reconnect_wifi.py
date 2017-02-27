#!/usr/bin/env python

from time import sleep
from datetime import datetime
from selenium import webdriver

url = 'http://192.168.14.2:8880/guest/s/default/login'
#url = 'http://gstatic.com/generate_204'
script = 'document.getElementById("connect").click()'
sleep_time = 60 # seconds
while True:
	try:
		print "{}\tReconnecting to wifi".format(datetime.now())
		driver = webdriver.PhantomJS()
		driver.get(url)
		driver.execute_script(script)
		sleep(sleep_time)
	except Exception as e:
		driver.save_screenshot('screenshot.png')
		sleep(sleep_time)
    	continue
