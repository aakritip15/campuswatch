import cv2
import os

def extract_frames_with_timestamps(video_path, output_folder, num_frames=10):
    """
    Extracts video frames with their timestamp in the video.

    Args:
        video_path (str): Path of input video.
        output_folder (str): Folder to save the frames.
        num_frames (int): No of frames to extract sequentially.

    Returns:
        list: A list of dictionaries with frame info.
    """
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video FPS: {fps}")

    extracted_frames = []
    frame_count = 0

    # Note: Here we are saving first n frames sequentially 
    # To extract 1 frame per second, we would need to skip frames based on fps value.
    while frame_count < num_frames:
        ret, frame = cap.read()
        if not ret:
            print("No more frames or video ended early.")
            break

        # calculate timestamp in seconds
        timestamp = frame_count / fps

        # Save frame with timestamp in filename
        frame_filename = os.path.join(output_folder, f"frame_{frame_count+1}_{timestamp:.2f}s.jpg")
        cv2.imwrite(frame_filename, frame)

        extracted_frames.append({
            "frame_number": frame_count + 1,
            "timestamp_sec": round(timestamp, 2),
            "file_path": frame_filename
        })

        frame_count += 1

    cap.release()
    print(f"Extraction complete. {len(extracted_frames)} frames saved.")
    return extracted_frames


if __name__ == "__main__":
    video_path = "sample_video.mp4"
    output_folder = "extracted_frames"

    frames_info = extract_frames_with_timestamps(video_path, output_folder, num_frames=10)

    print("\nFrame Extraction Summary:")
    for info in frames_info:
        print(f"Frame {info['frame_number']} → {info['timestamp_sec']}s → {info['file_path']}")
