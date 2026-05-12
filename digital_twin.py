{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c79b3b02-4267-49af-b867-b01ca0d86b13",
   "metadata": {},
   "outputs": [],
   "source": [
    "import serial\n",
    "import matplotlib.pyplot as plt\n",
    "from collections import deque\n",
    "\n",
    "# Change COM3 to your Arduino port\n",
    "arduino = serial.Serial('COM3', 9600)\n",
    "\n",
    "flow_data = deque(maxlen=20)\n",
    "water_data = deque(maxlen=20)\n",
    "\n",
    "plt.ion()\n",
    "\n",
    "while True:\n",
    "\n",
    "    data = arduino.readline().decode().strip()\n",
    "\n",
    "    try:\n",
    "        parts = data.replace(\"Flow: \",\"\").replace(\"Water: \",\"\").split()\n",
    "\n",
    "        flow = int(parts[0])\n",
    "        water = int(parts[1])\n",
    "\n",
    "        flow_data.append(flow)\n",
    "        water_data.append(water)\n",
    "\n",
    "        plt.clf()\n",
    "\n",
    "        plt.plot(flow_data, label='Flow Sensor')\n",
    "        plt.plot(water_data, label='Water Level')\n",
    "\n",
    "        plt.legend()\n",
    "        plt.xlabel(\"Time\")\n",
    "        plt.ylabel(\"Sensor Values\")\n",
    "        plt.title(\"AquaPulse Digital Twin\")\n",
    "\n",
    "        # Leak Detection\n",
    "        if flow < 300 or water < 300:\n",
    "            print(\"⚠️ LEAK DETECTED\")\n",
    "\n",
    "        plt.pause(0.1)\n",
    "\n",
    "    except:\n",
    "        pass"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
