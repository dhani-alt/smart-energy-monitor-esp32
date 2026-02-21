<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Smart Energy Saving System using ESP32

## Basic Details

### Team Name: EcoVolt

### Team Members
- Member 1: DHANIYA OV - GOVERNMENT ENGINEERING COLLEGE IDUKKI

### Hosted Project Link
[mention your project hosted link here]

### Project Description
Smart Energy Saving System is a hardware-based intelligent energy management system that automatically controls room lighting based on motion, ambient light intensity, and environmental conditions.
The system reduces unnecessary power consumption without requiring internet connectivity.

### The Problem statement
In classrooms, laboratories, hostels, and homes:
• Lights are often left ON when no one is present
• Energy is wasted during daytime even when sunlight is available
• Manual switching causes human error
This leads to increased electricity bills and energy wastage.
### The Solution
We designed a standalone ESP32-based smart system that:

• Detects human presence using PIR sensor
• Detects ambient light using LDR
• Measures temperature using DHT11
• Automatically turns lights ON/OFF
• Works completely offline
• Requires no internet or cloud

## Technical Details
### Technologies/Components Used
**For Software:**

Languages used:
• C++ (Arduino IDE)
Libraries used:
• DHT.h
Tools used:
• Arduino IDE
**For Hardware:**

Main Components:
• ESP32 Dev Module
• PIR Sensor (HC-SR501)
• DHT11 Sensor
• LDR
• LED / Relay Module
• Breadboard
• Jumper Wires

Specifications:
• ESP32 – 240 MHz dual-core processor
• PIR – Motion detection range up to 7m
• DHT11 – Temperature range 0–50°C
• LDR – Analog light sensing
Tools Required:
• USB cable
• Breadboard
• Soldering kit (optional for permanent setup)

## Features

Feature 1: Automatic Light ON when motion detected
Feature 2: Light OFF when no motion
Feature 3: Daylight detection (No light during daytime)
Feature 4: Temperature monitoring
Feature 5: Low-cost and portable
Feature 6: Fully offline operation

## Implementation

Hardware Components Required
• ESP32 Dev Board
• PIR Sensor
• DHT11
• LDR
• LED
• 220Ω Resistor
• Breadboard
• Jumper wires

Circuit Setup
• PIR OUT → GPIO 27
• DHT11 DATA → GPIO 33
• LDR → GPIO 34 (Analog input)
• LED → GPIO 25
• All VCC → 3.3V
• All GND → GND
### For Software:

#### Installation
```bash
1. Install Arduino IDE
2. Install ESP32 board package:
   - File → Preferences → Add ESP32 Board Manager URL  
3. Install required library:
   - `DHT sensor library
```

#### Run
```bash
1. Connect ESP32 via USB
2. Select Board: ESP32 Dev Module
3. Select correct COM Port
4. Click Upload
```

### For Hardware:

#### Components Required

• ESP32 Dev Board
• PIR Sensor
• DHT11
• LDR
• LED
• 220Ω Resistor
• Breadboard
• Jumper wires
Circuit Setup
• PIR OUT → GPIO 27
• DHT11 DATA → GPIO 33
• LDR → GPIO 34 (Analog input)
• LED → GPIO 25
• All VCC → 3.3V
• All GND → GND

#### Circuit Setup
System Architecture

Sensors (PIR, LDR, DHT11) → ESP32 Processing → Decision Logic → LED Control
• If Motion + Low Light → LED ON
• If No Motion → LED OFF
• If Bright Light → LED OFF


## Project Documentation

### For Software:

#### Screenshots (https://drive.google.com/drive/folders/1z6WhXm0iGgM5_GzKCj_RPsAAhTzgDJe1)

#### Diagrams

**System Architecture:**

**Application Workflow:**

https://drive.google.com/drive/folders/1z6WhXm0iGgM5_GzKCj_RPsAAhTzgDJe1

System continuously reads sensors
Checks motion detection
Checks ambient light level
Applies control logic
Turns LED ON/OFF accordingly
Displays values in Serial Monitor

### For Hardware:

#### Schematic & Circuit

## 🔌 Schematic & Circuit

### 🔹 Circuit Diagram
### 🔹 Schematic Diagram

![Circuit Diagram](https://drive.google.com/drive/folders/1z6WhXm0iGgM5_GzKCj_RPsAAhTzgDJe1)

**Figure 1: Complete Circuit Connections**

This diagram shows the hardware wiring of the Smart Energy Saving System:

- **PIR Sensor**
  - VCC → 3.3V  
  - GND → GND  
  - OUT → GPIO 27  

- **DHT11 Temperature Sensor**
  - VCC → 3.3V  
  - GND → GND  
  - DATA → GPIO 33  

- **LDR (Light Dependent Resistor)**
  - One end → 3.3V  
  - Other end → GPIO 34 (Analog Input)  
  - 10kΩ resistor connected to GND (Voltage Divider Configuration)

- **LED**
  - Anode → GPIO 25 (through 220Ω resistor)  
  - Cathode → GND  

The ESP32 processes motion and light data to control the LED automatically.

![Schematic Diagram](images/schematic-diagram.png)

**Figure 2: System Schematic Overview**

The schematic illustrates the logical connection between:

Sensors → ESP32 Microcontroller → Output (LED / Relay)

Working Logic:

1. PIR detects motion  
2. LDR checks ambient light level  
3. If motion is detected AND light level is low → LED turns ON  
4. If no motion OR sufficient daylight → LED turns OFF  
5. DHT11 continuously monitors temperature for environmental tracking  

This standalone system operates completely offline without cloud or internet dependency.

#### Build Photos

https://drive.google.com/drive/folders/1z6WhXm0iGgM5_GzKCj_RPsAAhTzgDJe1


### For Hardware Projects:
Complete connection of ESP32 with PIR, LDR, DHT11, and LED

#### Bill of Materials (BOM)

Component | Quantity | Specifications | Approx Price
ESP32 | 1 | Dev Module | ₹450
PIR Sensor | 1 | HC-SR501 | ₹120
DHT11 | 1 | Temp sensor | ₹80
LDR | 1 | Light sensor | ₹20
LED | 1 | 5mm | ₹5
Resistor | 1 | 220Ω | ₹1
Breadboard | 1 | 830 points | ₹120
Jumper wires | 10 | M-M | ₹50

**Total Estimated Cost:** ₹846

#### Assembly Instructions

**Step 1: Prepare Components**

Step 1: Connect ESP32 to breadboard
Step 2: Connect power rails (3.3V & GND)
Step 3: Connect PIR sensor
Step 4: Connect DHT11
Step 5: Connect LDR to analog pin
Step 6: Connect LED with 220Ω resistor
Step 7: Upload code using Arduino IDE

https://drive.google.com/drive/folders/1z6WhXm0iGgM5_GzKCj_RPsAAhTzgDJe1)

**Final Assembly:**
step 8: System ready for testing

![Final Build] https://drive.google.com/drive/folders/1z6WhXm0iGgM5_GzKCj_RPsAAhTzgDJe1
 Completed project ready for testing



## Project Demo

### Video
https://drive.google.com/drive/folders/1z6WhXm0iGgM5_GzKCj_RPsAAhTzgDJe1

The demo shows: 
• Motion detection
• Automatic light control
• Daylight detection
• Serial monitor output

 
## AI Tools Used 

Tool Used: ChatGPT
Purpose:
     • Code debugging
     • Circuit explanation preparation


**Key Prompts Used:**

- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** 30%



**Human Contributions:**

• Circuit design
• Hardware setup
• Testing and validation
• Logic development


## Team Contributions

 Dhaniya O V :
- Project concept and system design  
- Hardware component selection and circuit design  
- ESP32 firmware development (Arduino C++)  
- Sensor integration (PIR, LDR, DHT11)  
- Testing and debugging  
- Documentation and GitHub repository management  


## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
