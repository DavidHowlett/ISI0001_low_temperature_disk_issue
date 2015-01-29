import sys
sys.path.append(r'X:\CODE\Reusable')
import time
import picoscope
import alicatFlowMeter
import tsiFlowMeter

mainOutput = tsiFlowMeter.TSI()
controlOutput = alicatFlowMeter.alicat()
scope = picoscope.picoWrapper()

sensorCaliberation = [
    {'lowPressure':0.9967484474182129,'highPressure':9.93439769744873,'lowVoltage':0.5032121658159956,'highVoltage':4.076011326728309},
    {'lowPressure':0.9967484474182129,'highPressure':9.93439769744873,'lowVoltage':0.5118834771240478,'highVoltage':4.0882460239622525},
    ]

def voltageToPressure(voltage,sensorNumber):
    #to make the main formulae short I define these acronyms
    LP = sensorCaliberation[sensorNumber]['lowPressure']
    HP = sensorCaliberation[sensorNumber]['highPressure']
    LV = sensorCaliberation[sensorNumber]['lowVoltage']
    HV = sensorCaliberation[sensorNumber]['highVoltage']
    pressure = LP + (HP-LP)*(voltage-LV)/(HV-LV) 
    return pressure

try:
    startTime=time.time()
    while(startTime+60>time.time()):
    #while True:
        print(time.time()-startTime,end='\t')
        print(mainOutput.massFlow()/1000,end='\t')
        print(controlOutput.massFlow(),end='\t')
        print(voltageToPressure(scope.voltage(0),0),end='\t')
        print(voltageToPressure(scope.voltage(1),1),end='\t')
        print()
        time.sleep(0.001)
finally:
    scope.close()
    mainOutput.close()
    controlOutput.close()

