import serial
import time
import pandas as pd
import matplotlib.pyplot as plt

from collections import deque
from sklearn.ensemble import RandomForestClassifier

# -------------------------------
# TRAIN RANDOM FOREST MODEL
# -------------------------------

data = {

    'Flow': [520,510,500,200,180,150],
    'Leak': [300,320,310,80,70,60],
    'Pressure': [100200,100100,100000,88000,87000,86000],

    # 0 = Normal
    # 1 = Leak
    'Status': [0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[['Flow','Leak','Pressure']]
y = df['Status']

model = RandomForestClassifier()

model.fit(X,y)

# -------------------------------
# CONNECT ARDUINO
# -------------------------------

arduino = serial.Serial('COM8',9600)

time.sleep(2)

# -------------------------------
# GRAPH STORAGE
# -------------------------------

flow_data = deque(maxlen=20)
leak_data = deque(maxlen=20)
pressure_data = deque(maxlen=20)

plt.ion()

fig, ax = plt.subplots()

# -------------------------------
# LIVE DIGITAL TWIN
# -------------------------------

while True:

    try:

        data = arduino.readline().decode().strip()

        print(data)

        # Expected:
        # Flow:520 Leak:300 Pressure:100200

        parts = data.split()

        flow = int(parts[0].split(":")[1])

        leak = int(parts[1].split(":")[1])

        pressure = float(parts[2].split(":")[1])

        # ML Prediction
        result = model.predict([[flow, leak, pressure]])

        if result[0] == 1:

            print("⚠ LEAK DETECTED")

        else:

            print("✅ NORMAL")

        print("---------------------")

        # Store graph values
        flow_data.append(flow)
        leak_data.append(leak)
        pressure_data.append(pressure)

        # Update graph
        ax.clear()

        ax.plot(flow_data, label="Flow")

        ax.plot(leak_data, label="Leak Sensor")

        ax.plot(pressure_data, label="Pressure")

        ax.legend()

        ax.set_title("Digital Twin Pipeline Monitoring")

        plt.pause(0.1)

    except Exception as e:

        print(e)
