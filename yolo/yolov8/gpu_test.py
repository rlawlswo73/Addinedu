from ultralytics import YOLO


# 학습된 모델 로드
model = YOLO('/home/kjj37/dev_ws/yolo/yolov8/runs/detect/train3/weights/best.pt')  # 학습된 모델 경로

# 이미지 예측
# results = model.predict(source='/path/to/test/image.jpg', save=True)

# 비디오 예측
results = model.predict(source='/home/kjj37/dev_ws/yolo/data/VideoEditor_20241127_060046.mp4', 
                        show=True, 
                        save=True, 
                        imgsz=640, 
                        conf=0.7, 
                        save_conf=True, 
                        device=0,
                        project="./")

