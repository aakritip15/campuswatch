
# Video Frame Extraction with OpenCV

##  Overview
This script extracts the **first 10 frames** from a video file using **OpenCV**, saving them as image files with their **timestamps** in the filename.  
It also returns structured metadata about each frame.  


##  Features
- Extracts sequential frames from a video.  
- Saves frames as `.jpg` with **timestamps in seconds**.  
- Returns a list of dictionaries with frame details (`frame number`, `timestamp`, `file path`).  
- Automatically creates an output folder if it doesn’t exist.  


## How It Works
1. Open the video using OpenCV.  
2. Read frames sequentially until the desired number (`num_frames`) is reached.  
3. For each frame:  
   - Compute timestamp = `frame_number / FPS`.  
   - Save image with filename format:  
     ```
     frame_<number>_<timestamp>s.jpg
     ```  
   - Store frame info in a dictionary.  
4. Return and print a summary of extracted frames.  



## Usage
Run the script:
```bash
python extract_frames.py
