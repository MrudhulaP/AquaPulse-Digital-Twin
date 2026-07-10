# Digital Twin Pipeline Monitoring System

## Overview

This project is a **Digital Twin Pipeline Monitoring System** using:

* **Arduino sensors**
* **Python**
* **Machine Learning (Random Forest)**
* **Real-time graph visualization**

The system reads live sensor values from Arduino and predicts whether the pipeline condition is:

* ✅ **NORMAL**
* ⚠ **LEAK DETECTED**

using a trained **Random Forest Classifier**.

---

# Features

* Real-time serial communication with Arduino
* Machine Learning based leak detection
* Live sensor monitoring
* Dynamic graph plotting
* Digital Twin simulation
* Pressure, Flow, and Leak analysis

---

# Technologies Used

* Python
* Arduino
* Scikit-learn
* Pandas
* Matplotlib
* PySerial

---

# Project Structure

```plaintext
project/
│
├── digital_twin.py
├── README.md
└── arduino_code.ino
```

---

# Machine Learning Model

The project uses a **Random Forest Classifier** trained on sample sensor data.

### Input Features

* Flow
* Leak
* Pressure

### Output

* `0` → Normal
* `1` → Leak Detected

---

# How It Works

## Step 1: Train ML Model

The Random Forest model is trained using sample pipeline sensor data.

## Step 2: Connect Arduino

Python connects to Arduino through serial communication.

```python
arduino = serial.Serial('COM8',9600)
```

## Step 3: Read Live Sensor Data

Python continuously receives sensor values from Arduino.

## Step 4: Predict Pipeline Status

The ML model predicts whether the system is normal or leaking.

## Step 5: Visualize Digital Twin

Real-time graphs display:

* Flow values
* Leak sensor values
* Pressure values

---

# Graph Visualization

The system displays a live graph for:

* Flow Sensor
* Leak Sensor
* Pressure Sensor

This acts as the **Digital Twin Dashboard**.

---

# Future Enhancements

* Cloud integration
* Mobile app monitoring
* Advanced AI prediction
* MQTT/IoT support
* Real sensor dataset training
* Alert notification system

---

# Author

Developed as a Mini Project on:

**Digital Twin Technology using Machine Learning and Arduino**
BY Mrudhula , Sudarshan , Moksha , Skanda 

