{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7290ec7f-70eb-4275-b2b8-97fefbf77303",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pyserial\n",
      "  Downloading pyserial-3.5-py2.py3-none-any.whl.metadata (1.6 kB)\n",
      "Requirement already satisfied: matplotlib in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (3.10.8)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (1.3.3)\n",
      "Requirement already satisfied: cycler>=0.10 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (0.12.1)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (4.61.1)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (1.4.9)\n",
      "Requirement already satisfied: numpy>=1.23 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (2.4.0)\n",
      "Requirement already satisfied: packaging>=20.0 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (25.0)\n",
      "Requirement already satisfied: pillow>=8 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (12.0.0)\n",
      "Requirement already satisfied: pyparsing>=3 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (3.3.1)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from matplotlib) (2.9.0.post0)\n",
      "Requirement already satisfied: six>=1.5 in .\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)\n",
      "Downloading pyserial-3.5-py2.py3-none-any.whl (90 kB)\n",
      "Installing collected packages: pyserial\n",
      "Successfully installed pyserial-3.5\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 26.0.1 -> 26.1.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install pyserial matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7ff51ab-3328-4c24-96d4-a6dca66b1ed7",
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
