## 🔥 Detecting Fire–Human Presence For Safety Monitoring
 This project demonstrates object detection using YOLOv8 for identifying Fire and Human objects in images. A custom dataset was prepared, annotated, and used to train a YOLOv8 model capable of detecting fire incidents and human presence in various scenarios.
 The project also includes evaluation of model performance using metrics such as Precision, Recall, mAP, and Confusion Matrix analysis.

## 📊 Project Overview
**The project highlights:**<br>
-🔥 Fire Detection: Bounding boxes around visible flames.<br>
-👤 Human Detection: Identification of humans in fire-related scenes.<br>
-📈 Performance Evaluation: Precision, Recall, mAP, and Confusion Matrix analysis.<br>
-🎥 Detection Demonstration: Prediction results converted into a video for visualization.<br>

**Key Insights:**
- Detection of Fire and Human objects on unseen test images.
- Performance evaluation using YOLOv8 validation metrics.
- Training and validation behavior visualized through graphs.
- Analysis of strengths and limitations of the trained model.

## 🛠 Tools Used:
- Python
- Ultralytics YOLOv8
- PyTorch
- OpenCV
- NumPy
- FFmpeg

## 📂 Project Files:
 Dataset/ → Images, labels, train.txt, val.txt and data.yaml<br>
 best.pt → Best trained YOLOv8 model weights<br>
 detection_video.mp4 → Video generated from prediction outputs<br>
 predict → Sample detection outputs<br>
 README.md → Project documentation<br>

## 📦 Dataset:
The dataset was prepared in YOLO format and contains two classes:
Class ID	Class Name<br>
0	        Fire<br>
1	        Human<br>

**Dataset Statistics:**
Class	Instances<br>
Fire	97<br>
Human	96<br>
Total annotated objects: 193

## 📸 Sample Outputs:
<img width="640" height="360" alt="frame_355" src="https://github.com/user-attachments/assets/89a6ffed-4b2f-48e9-aab7-0694652e6809" />
<img width="640" height="360" alt="frame_307" src="https://github.com/user-attachments/assets/f0d410ca-28c8-47f3-b61b-74fad1adbe77" />
<img width="640" height="360" alt="frame_016" src="https://github.com/user-attachments/assets/fce865bc-8c4b-4f09-a24e-8110930db014" />

**Example detections include:**
Fire detection with confidence scores
Human detection with confidence scores
Simultaneous Fire and Human detection in the same image

## 🚀 Training Configuration
Parameter:<br>
Model      -	YOLOv8 Nano (yolov8n.pt)<br>
Epochs     -	100<br>
Image Size -	384 × 384<br>
Classes	   - Fire, Human<br>
**Generated Outputs:**
best.pt<br>
last.pt<br>
results.png<br>
confusion_matrix_normalized.png<br>
prediction outputs<br>

## 📊 Training Metrics
<img width="1449" height="813" alt="image" src="https://github.com/user-attachments/assets/966041a3-3ece-4cbd-b055-d2b095a6bc9a" />
Performance Summary:<br>
Metric	Value<br>
Precision	~0.90<br>
Recall  	~0.89<br>
mAP@50	  ~0.93<br>
mAP@50-95	~0.55<br>

**Interpretation:**
High Precision indicates that most detected objects are classified correctly.
High Recall shows that the model successfully detects most Fire and Human instances.
Strong mAP@50 demonstrates effective object detection performance on the validation dataset.

## Confusion Matrix
<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/a2498fd9-23fa-4310-90ef-a6091ea758ca" />
**Observations:**
-**Fire Detection**<br>
- Correctly Detected: ~95%<br>
- Background Confusion: ~5%<br>
-**Human Detection**<br>
- Correctly Detected: ~82%<br>
- Background Confusion: ~18%<br>

## 🎥 Demonstration Video
The prediction outputs were converted into a video using FFmpeg to visualize the model's performance across multiple frames.
detection_video.mp4:https://drive.google.com/file/d/1VVXAJSZTYN8fVxOAntBCuUvl7x4DBHXu/view?usp=sharing

## 🔍 Analysis of Detection Performance
The trained YOLOv8 model achieved strong performance on both Fire and Human detection tasks. Based on the confusion matrix, Fire detection achieved a higher detection rate than Human detection on the validation dataset.

**Observations**
Fire objects were detected with high accuracy despite their irregular shape and varying appearance.<br>
Human detection performance was slightly lower due to factors such as occlusion, partial visibility, and variations in pose.<br>
Some missed detections occurred when objects were small, distant, or appeared under challenging lighting conditions.<br>
Background complexity and visual noise occasionally affected object localization.<br>

Overall, the results demonstrate the effectiveness of YOLOv8 for safety monitoring applications involving Fire and Human detection.

## 🔥 Challenges in Fire Detection

Fire detection remains a challenging computer vision task due to several real-world factors:

- **No fixed shape:** Fire is highly dynamic and has irregular boundaries that change continuously, making it difficult for models to learn stable features.
- **Visual similarity with background:** Bright objects such as sunlight, lamps, reflections, and warm-colored surfaces can resemble fire and lead to false detections.
- **Small or distant fire regions:** Flames may occupy only a small portion of an image, making accurate localization more difficult.
- **Lighting and smoke variations:** Fire appearance can vary significantly across indoor/outdoor environments, day/night conditions, and smoke-covered scenes.

Despite these challenges, the trained YOLOv8 model achieved strong fire detection performance on the validation dataset.


## 🔑 Learnings & Takeaways

- Building and organizing a custom YOLO-format dataset
- Annotating images for object detection tasks
- Training YOLOv8 using transfer learning
- Evaluating model performance using Precision, Recall, and mAP
- Understanding confusion matrix analysis
- Detecting Fire and Human objects in unseen images
- Creating visual demonstrations from prediction outputs
- Gaining practical experience with an end-to-end computer vision workflow

## 🏁 Conclusion
This project demonstrates the successful application of YOLOv8 for Fire and Human detection using a custom dataset. The trained model achieved strong precision, recall, and mAP scores while effectively detecting target objects in unseen images.<br>
The project provided practical experience in dataset preparation, annotation, model training, evaluation, and result visualization, forming a complete end-to-end computer vision workflow.<br>


  ## 👤 Author
  
**Midhath Firdouse**<br>
Computer Science Engineering (CSE)<br>
Detecting Fire and Human Presence For Safety Monitoring


