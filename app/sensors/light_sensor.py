from grove.adc import ADC

adc = ADC()

def read_light(port=0):
    return adc.read(port)
