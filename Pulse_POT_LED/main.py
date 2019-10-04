import time
import board
import pulseio as pio
from analogio import AnalogIn
 
#Pin A1
pot_in = AnalogIn(board.A1)
#Pin 12
led = pio.PWMOut(board.D12, frequency=5000, duty_cycle=0)

rngnum = 100

btrng = 65535


def get_voltage(pin):
    return ((pin.value * 3.3) / btrng)

def volt_value(in_volt):
    #Voltage in the input from pot on pin 12
    if in_volt <= 0.02:
        ptime = 0.00005
    elif in_volt > 0.030 and in_volt < 0.700:
        ptime = 0.0005
    elif in_volt > 0.700 and in_volt < 1.200:
        ptime = 0.005
    elif in_volt > 1.200 and in_volt < 1.500:
        ptime = 0.015
    elif in_volt > 1.500 and in_volt < 2.5:
        ptime = 0.05
    elif in_volt > 2.5:
        ptime = 0.1
    return ptime
 
while True:
        for i in range(rngnum):
            # PWM LED up and down
            if i < 50:
                # Up
                led.duty_cycle = int(i * 2 * btrng / rngnum)  
            else:
                # Down
                led.duty_cycle = btrng - int((i - 50) * 2 * btrng / rngnum)
        volt = get_voltage(pot_in)
        #Uncomment the next line to view the values on serial in Mu
        #print(volt)
        btime = volt_value(volt)
        time.sleep(btime)
        #Uncomment the next line to view the values on serial in Mu
        #print(btime)