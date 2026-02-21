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

#### Screenshots (Add at least 3)

![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

![Workflow](docs/workflow.png)

System continuously reads sensors
Checks motion detection
Checks ambient light level
Applies control logic
Turns LED ON/OFF accordingly
Displays values in Serial Monitor

### For Hardware:

#### Schematic & Circuit

![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

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


![Step 1](images/assembly-step1.jpg)

![Step 2](images/assembly-step2.jpg)

![Step 3](images/assembly-step3.jpg)

**Final Assembly:**
step 8: System ready for testing

![Final Build](images/final-build.jpg)

 Completed project ready for testing

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

The demo shows: 
• Motion detection
• Automatic light control
• Daylight detection
• Serial monitor output

 
### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

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
