# Alert Severity Logic

##  Overview
This script calculates and assigns severity levels to security alerts based on factors like:
- Threat type  
- Location risk  
- Confidence score  
- Contextual details (person count, duration, camera, etc.)

It also generates a JSON object containing all relevant alert information.
 

## Features
- Defines threat types, severity levels, and location risk categories.  
- Dynamically adjusts severity based on risk and confidence score.  
- Generates structured JSON output for alerts.  
- Saves generated alerts into a file (`generated_alerts.json`).  
 
## How It Works
1. Define the context of an alert (`AlertContext`) including threat type, risk level, and metadata.  
2. Use `calculate_severity()` to determine severity level.  
3. Generate a JSON alert with `generate_alert_json()`.  
4. Save results to a file and print them.  
 

## Usage
Run the script:
```bash
python main.py
