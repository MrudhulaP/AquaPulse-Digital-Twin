import matplotlib
matplotlib.use('Qt5Agg')

import serial
import time
import pandas as pd
import matplotlib.pyplot as plt

from collections import deque
from sklearn.ensemble import RandomForestClassifier



data = {

    # NORMAL
    'Flow': [20,30,40,50,60,120,130,140,150,160],

    'Leak': [
        100,120,130,110,115,
        600,620,640,650,660
    ],

    'Pressure': [
        100200,100100,100000,100300,100400,
        88000,87000,86000,85000,84000
    ],

    'Status': [
        0,0,0,0,0,
        1,1,1,1,1
    ]
}

df = pd.DataFrame(data)

X = df[['Flow', 'Leak', 'Pressure']]

y = df['Status']



model = RandomForestClassifier(
    n_estimators=100
)

model.fit(X, y)



arduino = serial.Serial('COM8', 9600)

time.sleep(2)

print("Arduino Connected")
print("-----------------------")

# STORE GRAPH DATA


flow_data = deque(maxlen=20)

leak_data = deque(maxlen=20)

pressure_data = deque(maxlen=20)

plt.ion()

fig, ax = plt.subplots(figsize=(10,5))

plt.show()

# MAIN LOOP

while True:

    try:

        # READ SERIAL DATA
        raw_data = arduino.readline().decode().strip()

        print(raw_data)

        

        parts = raw_data.split()

        if len(parts) != 3:

            print("Invalid Data")

            continue

    
        raw_flow = int(parts[0].split(":")[1])
        
        raw_leak = int(parts[1].split(":")[1])
        
  
        flow = raw_flow - 550
        
        leak = raw_leak - 550

        pressure = float(parts[2].split(":")[1])

 
        # MACHINE LEARNING PREDICTION
   
        if flow > 50 or leak > 50:
        
            print("⚠ LEAK DETECTED")
        
        else:
        
            print("✅ NORMAL")
        sample = pd.DataFrame(
            [[flow, leak, pressure]],
            columns=['Flow', 'Leak', 'Pressure']
        )

        result = model.predict(sample)

  
        # OUTPUT
  

        if result[0] == 1:

            print("⚠ LEAK DETECTED")

        else:

            print("✅ NORMAL")

        print("-----------------------")

        # STORE GRAPH VALUES
     

        flow_data.append(flow)

        leak_data.append(leak)

        pressure_data.append(pressure)

     

        ax.clear()

        ax.plot(
            list(flow_data),
            label="Flow"
        )

        ax.plot(
            list(leak_data),
            label="Leak Sensor"
        )

        # SCALE PRESSURE
        scaled_pressure = [
            p / 1000 for p in pressure_data
        ]

        ax.plot(
            scaled_pressure,
            label="Pressure / 1000"
        )

        ax.set_title(
            "Digital Twin Pipeline Monitoring"
        )

        ax.set_xlabel("Time")

        ax.set_ylabel("Sensor Values")

        ax.legend()

        ax.grid(True)

        plt.pause(0.1)

    except KeyboardInterrupt:

        print("Program Terminated")

        break

    except Exception as e:

        print("Error:", e)

        #Ctrl + c TO stop
