# License Plate Recognition using YOLOv10 and PaddleOCR

This project demonstrates the **License Plate Recognition (LPR)** system using the **YOLOv10** object detection model and **PaddleOCR** for optical character recognition (OCR). The system is designed to detect and recognize license plates in images or videos, with preprocessing to improve accuracy and clarity.

### Key Features:
- **YOLOv10 Model**: Used for detecting license plates in images and videos.
- **PaddleOCR**: Used for reading and extracting text (license plate numbers) from the detected regions.
- **Customizable for Images and Videos**: The system can process both images and video files.

---

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [How it Works](#how-it-works)
- [Usage](#usage)
- [License](#license)

---

## Features

- **License Plate Detection**: Uses the YOLOv10 model to detect license plates in an image or video.
- **OCR Recognition**: Extracts text from the detected regions using PaddleOCR.
- **Video or Image Input**: Capable of processing both image and video files.
- **Output**: Annotates the image/video with detected license plates and recognized text.

---

## Requirements

This project requires the following libraries:

- **Python 3.8+**
- **OpenCV**: For image and video processing.
- **YOLOv10 (Ultralytics)**: For object detection.
- **PaddleOCR**: For text recognition (OCR).
- **NumPy**: For numerical operations and array handling.

### Install Required Libraries

You can install the required Python libraries using `pip`:

```bash
pip install opencv-python-headless
pip install ultralytics
pip install paddlepaddle
pip install paddleocr
pip install numpy
```

---

## Setup

1. **Download the YOLOv10 Model**: You need to download the pre-trained YOLOv10 model (`best.pt`) and place it in the `weights/` directory.
   - You can train your own YOLO model or use a pre-trained one. Ensure the model weights are located at `r"C:\path\to\best.pt"`, or adjust the path accordingly.

2. **Download PaddleOCR**: You need to set up **PaddleOCR** which is used for text recognition from license plates. Ensure PaddleOCR is correctly installed (as shown in the `pip` install command).

---

## How It Works

The system processes the input in the following steps:

1. **Video or Image Capture**: 
   - If an image is provided, the script processes that single image. 
   - If a video file is provided, the system processes it frame by frame.

2. **YOLOv10 for Object Detection**:
   - The YOLOv10 model is used to detect bounding boxes around regions that are likely license plates.
   - These bounding boxes are drawn on the image or video frame for visualization.

3. **PaddleOCR for Text Recognition**:
   - After detecting the license plates, the system extracts the region within the bounding box and applies **PaddleOCR** to recognize the text (i.e., the license plate number).

4. **Annotations**:
   - The detected license plate and recognized text are annotated and displayed on the image or video.
   - The confidence score of the detection is also calculated.

---

## Usage

### 1. Input Video or Image
   You can change the input source by modifying the following line:
   
   ```python
   cap = cv2.VideoCapture(r"C:\path\to\your_video_or_image")
   ```

   Replace `"C:\path\to\your_video_or_image"` with the path to either an image or video file. For example:
   - Video: `C:\Videos\license_plate_video.mp4`
   - Image: `C:\Images\license_plate.jpg`

### 2. Running the Script
Run the Python script:

```bash
python license_plate_recognition.py
```

The script will process the input file and display the annotated video or image with detected license plates and OCR results.

### 3. Annotated Output
The system will display the processed frames (video) or images with bounding boxes drawn around detected license plates, along with the recognized text (license plate number).

- Press `1` to exit the processing loop if using a video file.
  
---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Notes

- **Model Path**: Ensure that the YOLOv10 model weights file (`best.pt`) is available at the correct path.
- **OCR Accuracy**: The accuracy of OCR can vary depending on the quality of the input image or video and the training of the YOLO model.
- **Performance**: For optimal performance, ensure that PaddleOCR is installed correctly with the required dependencies.

---

Let me know if you need further adjustments or if there's any specific detail you'd like to include!
