import uftpd
import wifi
import time
from machine import Pin, PWM
import _thread

import pwmio

motorrun = pwmio.PWMOut(board._, duty_cycle=0, frequency= )
motorrun.duty_cycle = 50 #on




#pulse per rev on motor driver
pulrev = 400

#distance per turn (cm/rev) from rod
rodturn = 1.27

motordir = Pin(27, Pin.OUT)
motorpul  = Pin(25)
motoron = PWM(motorpul, freq=1, duty=50)
motoron.deinit()

topbutton = Pin(4, Pin.IN, Pin.PULL_UP)
bottombutton = Pin(33, Pin.IN, Pin.PULL_UP)

#solenoids
valve6 = Pin(18, Pin.OUT, Pin.PULL_DOWN)
valve15 = Pin(23, Pin.OUT, Pin.PULL_DOWN)

#light buttons
ldbutton = Pin(22, Pin.IN, Pin.PULL_UP)
ldlight = Pin(21, Pin.OUT)

flbutton = Pin(5, Pin.IN, Pin.PULL_UP)
fllight = Pin(19, Pin.OUT)

ftbutton = Pin(26, Pin.IN, Pin.PULL_UP)
ftlight = Pin(32, Pin.OUT)

ctbutton = Pin(14, Pin.IN, Pin.PULL_UP)
ctlight = Pin(15, Pin.OUT)

ldlight.off()
fllight.off()
ftlight.off()
ctlight.off()


def status():
    while True:
        print('{} {} {} {} {} {}'.format(topbutton.value(), bottombutton.value(), 
            ldbutton.value(), flbutton.value(), ftbutton.value(), ctbutton.value()))
        time.sleep_ms(500)



def buttonstop():
    '''do not stop until button touched'''
    dontstop = True
    while dontstop:
        time.sleep_ms(10)
        if (topbutton.value() == 1 or bottombutton.value() == 1 or ldbutton.value() == 0
            or flbutton.value() == 0 or ftbutton.value == 0 or ctbutton.value == 0):
            print('{} {} {} {} {} {}'.format(topbutton.value(), bottombutton.value(), 
                    ldbutton.value(), flbutton.value(), ftbutton.value(), ctbutton.value()))
            dontstop = False

def emergencystop():
    '''check for emergency stop signal while ramping up speed'''
    if (topbutton.value() == 0 or bottombutton.value() == 0 or ldbutton.value() == 0
        or flbutton.value() == 0 or ftbutton.value == 0 or ctbutton.value == 0):
        time.sleep_ms(5)
        if (topbutton.value() == 0 or bottombutton.value() == 0 or ldbutton.value() == 0
            or flbutton.value() == 0 or ftbutton.value == 0 or ctbutton.value == 0):
            print('{} {} {} {} {} {}'.format(topbutton.value(), bottombutton.value(), 
                ldbutton.value(), flbutton.value(), ftbutton.value(), ctbutton.value()))
            return True
        else:
            return False
    else:
        return False


    
def moveshuttle(dir):
    if dir: #direction up
        motordir.on()
    else: #direction down
        motordir.off()
        
    with open('config.txt', 'r') as myfile:
        velocity = float(myfile.read())
    frequency = int(pulrev / rodturn * velocity)
    
    #full frequency
    motoron = PWM(motorpul, freq=frequency, duty=50)
    time.sleep_ms(100)
    buttonstop()
    motoron.deinit()


    
def loading():
    #all lights off, loading light on
    ldlight.on()
    fllight.off()
    ftlight.off()
    ctlight.off()
    
    #pwr off both valve
    valve6.off()
    valve15.off()
    print('loading')
    moveshuttle(True)
        
def filling():
    #all lights off, filling light on
    ldlight.off()
    fllight.on()
    ftlight.off()
    ctlight.off()
    print('filling')
    #pwr on both valve
    valve6.on()
    valve15.on()

def filtering():
    #all lights off, filtering light on
    ldlight.off()
    fllight.off()
    ftlight.on()
    ctlight.off()
    
    #pwr off both valve
    valve6.off()
    valve15.off()
    print('filtering')
    moveshuttle(False)

def counting():
    #all lights off, counting light on
    print('counting')
    ldlight.off()
    fllight.off()
    ftlight.off()
    ctlight.on()
    
    #pwr off 5 valve, pwr on 1 valve
    valve6.on()
    valve15.off()
  

if __name__ == "__main__":

    while True:
        if ldbutton.value() == 0:
            loading()
            time.sleep_ms(500)
        elif flbutton.value() == 0:
            filling()
            time.sleep_ms(500)
        elif ftbutton.value() == 0:
            filtering()
            time.sleep_ms(500)
        elif ctbutton.value() == 0:
            counting()
            time.sleep_ms(500)
        else:
            time.sleep_ms(100)
  
  
