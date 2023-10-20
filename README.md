# American-Sign-Language-Classification
An application for real-time American Sign Language classification

## Training
```
  pip install -r requirements.txt
  python env.py
  python train.py --img 448 --batch 64 --epochs 500 --data data.yaml --weights yolov5s.pt --workers 8
```
Modify data.yml to set training and validation image path

The trained model will be saved to yolov5/runs/train/exp/weights/best.pt

## Validation
```
  python val.py --weights runs/train/exp/weights/best.pt --data data.yaml --img 448
```

## Dectection
### Video Input
```
  python detection.py --source path_to_video
```
### Webcam
```
  python detection.py --source 0
```
