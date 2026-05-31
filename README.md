# Computer Vision Summer Internship - IIIT Hyderabad

This repository contains tasks and project completed during my Summer internship.

---

## 📂 Structure

### 📅 Week 1
* **Task 1:** Video to image <br>
* **Task 2:** Frames to video <br>
* **Task 3:** Merging video with audio <br>

### 📅 Week 2
* **Task 1,2,3:** Object detection <br>

### 📅 Week 3
* **Task 1:** Segmentation <br>
* **Task 2:** Stack videos using FFmpeg <br>

### 📅 Week 4
* **Task 1:** Report on YOLO dataset configuration metadatafiles analysis report <br>
* **Task 2:** Dataset configuration & inputs <br>
  * **Dataset folder structure:** <br>
    * `images/` <br>
      * `train/` -> [Google Drive Link for Frames] <br>
      * `val/` <br>
    * `labels/` <br>
      * `train/` <br>
      * `val/` <br>
      * `train.cache` <br>
      * `val.cache` <br>
    * `data.yaml` <br>
    * `train.txt` <br>
    * `val.txt` <br>
  * **Input video:** Original source video used for testing <br>
  * **Test images:** [Google Drive Link for Test Images] <br>

### 📅 Week 5
* **Dataset organization:** Structured the Fire–Human dataset in YOLO format with images, labels, and configuration files. <br>
* **Image preprocessing:** Resized dataset images to the required input resolution for YOLOv8 training. <br>
* **Model training:** Fine-tuned a YOLOv8 Nano model on the custom Fire–Human detection dataset for 100 epochs. <br>
* **Model evaluation:** Analyzed training results using Precision, Recall, mAP, and Confusion Matrix metrics. <br>
* **Inference on test images:** Performed object detection on unseen test images and generated annotated outputs with bounding boxes and confidence scores. <br>
* **Video generation:** Converted prediction outputs into a demonstration video using FFmpeg to visualize detection performance across multiple frames. <br>

---

## 🛠️ Tools Used <br>
* **Python** <br>
* **FFmpeg** <br>
* **Ultralytics** <br>
* **PyTorch**<br>
* **NumPy**<br>
* **Open CV**<br>
* **Label Studio**<br>

---

## 📝 Notes <br>
* Each task is organized in separate folders. <br>
* Outputs are included wherever applicable. <br>
* The repository demonstrates practical applications of Computer Vision, Object Detection, Segmentation, Datasetset preparation and video processing workflows.

---

## 👤 Author <br>
**Midhath Firdouse**
