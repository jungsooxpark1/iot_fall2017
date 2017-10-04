
#!/usr/bin/env python


###############################################################
##DEBOUNCE INTERNAL PULLUP & INTERNAL PULLDOWN
import os
from time import sleep
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#btns
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.IN)
GPIO.setup(12,GPIO.IN)
#LED
GPIO.setup(11,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
#buzzer
GPIO.setup(15,GPIO.OUT)
ck_pwm = GPIO.PWM(15, 1000)

loop_count = 0

prev_input = 0
prev_input2 = 0

print "\n\nSay 'love' through Morse code\n  love = .-.. --- ...- . (Green is . and Blue is -)\n\n"
while True:

  #DOT btn
  input = GPIO.input(7)

  #DOT btn-DEBOUNCE_START
  if ((not prev_input) and input):
    #TEXT
    print(".")
    #LED
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(11,GPIO.LOW)
    #Dot buzzer
    ck_pwm.start(10)
    sleep(0.1)
    ck_pwm.stop()
  #DOT btn-DEBOUNCE_END
  prev_input = input

  #DASH btn
  input2 = GPIO.input(12)

  #DASH btn-DEBOUNCE
  if (( prev_input2) and not input2):
    #TEXT
    print("-")
    #LED
    GPIO.output(16,GPIO.LOW)
    GPIO.output(11,GPIO.HIGH)
    #Dash buzzer
    ck_pwm.start(10)
    sleep(0.3)
    ck_pwm.stop()
  #DASH btn-DEBOUNCE_END
  prev_input2 = input2
  

  
  time.sleep(0.05)

os.system('clear')
GPIO.cleanup()