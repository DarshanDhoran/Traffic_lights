import time

def trafic_light():
    trafic_lights = ['Red', 'Green', 'Yellow'] # list of traffic lights
    currentStateIndex = 0 # index for tracking the current state
    while True:
        currentLight = trafic_lights[currentStateIndex]
        print(f"CurrentLight is now :{currentLight}")
        time.sleep(2)
        
        currentStateIndex = ( currentStateIndex + 1 ) % len(trafic_lights)
trafic_light()