# Pedestrian_detection

### Pedestrain detection using YOLO algirithm

This is pedestrian detection project using yolo(You only look once) algorithm from scratch in python and keras.

### Data

Data used is TUD-Brussels and TUD-MotionPairs and Downloaded from [here](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/people-detection-pose-estimation-and-tracking/multi-cue-onboard-pedestrian-detection/)

For training and validation 1092 positive and 192 Negative images are used

### Labelling
Labelling is done using [labelImg](https://github.com/tzutalin/labelImg)

Annotations are [here](https://drive.google.com/open?id=10xa2eaMWB2MypZ9UPtUrVJLvQP_36Jox)

### Preprosessing
All images are resized to (512,512) and saved in array. Also, ground truths are processed to form a array of (16,16,1,5).All images normalized between -1 and 1.

### Loss Function
Loss function for yolo is implemented as mentiond in [yolo paper](https://arxiv.org/pdf/1506.02640.pdf).

### Model
For feature extraction VGG16 model is used. 

Fully connected layers of VGG16 are removed and two conv layers are added to the architechture of VGG16 to get the expected output form i.e (16,16,1,5).

### Training
Training is done for 90 epochs on batch size of 16.

For First 50 epochs learning rate is 0.0001

For next 40 epochs learning rate is 0.00001.

Get pretrained weights [here](https://drive.google.com/open?id=1rtBL4Bm3_dMnwyL91mN0LpgoXySFzSLZ)

### Output
Output is in the form (16,16,1,5). To get boxes from output required functions are in decode_boxes.py file. Non max suppression is used to eliminate boxes as mentioned in yolo paper.

##### Output on [eth dataset](https://data.vision.ee.ethz.ch/cvl/aess/cvpr2008/seq04-img-left.tar.gz)

![alt text](https://github.com/tusharbhosale/pedestrian_detection/blob/master/output/eth_gif.gif)
