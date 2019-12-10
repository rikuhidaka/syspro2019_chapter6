#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('deg<input type="number" name="deg" size="40">')
print('<input type="submit" name="button" value="rotate">')
print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

form = cgi.FieldStorage()
value = form.getvalue("deg")

def setservo(deg):
	D = ((0.01055556 * (deg+90) + 0.5)/20)*100
	servo.ChangeDutyCycle(D)
	time.sleep(1.0)

setservo(int(value))
