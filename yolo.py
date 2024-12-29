import time
import cv2
from picamera2 import Picamera2
from ultralytics import YOLO

def main():
    # Set up the camera with Picam2
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (1280, 1280)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()
    picam2.configure("preview")
    picam2.start()

    # Load YOLOv8 model (tiny model used here as an example)
    model = YOLO("yolov8n.pt")

    print("Starting detection loop. Press Ctrl+C to stop...")

    frame_count = 0
    try:
        while True:
            frame_count += 1

            # Capture a frame from the camera
            frame = picam2.capture_array()

            # Run YOLO model on the captured frame
            # results is a list of ultralytics.engine.results.Results
            results = model(frame)

            # Each results list can contain multiple images; here we only have 1 image per capture
            result = results[0]

            # Get inference time (ms) and compute approximate FPS
            inference_time_ms = result.speed['inference']
            fps = 1000.0 / inference_time_ms if inference_time_ms != 0 else 0

            # Print frame header
            print(f"\n=== Frame {frame_count} ===")
            print(f"Inference Time: {inference_time_ms:.2f} ms | FPS: {fps:.1f}")

            # Retrieve and print detections
            boxes = result.boxes  # ultralytics.yolo.engine.results.Boxes object
            # YOLO model knows the class names via model.names or result.names
            class_names = model.names

            if boxes is not None and len(boxes) > 0:
                print("Detections:")
                for box in boxes:
                    # box.cls, box.conf, box.xyxy are tensors, so get actual values
                    cls_id = int(box.cls[0])       # class index
                    conf = float(box.conf[0])      # confidence
                    x1, y1, x2, y2 = box.xyxy[0]   # bounding box coords

                    class_name = class_names.get(cls_id, "unknown")
                    print(f"  - {class_name} (conf: {conf:.2f}) at "
                          f"({x1:.0f}, {y1:.0f}), ({x2:.0f}, {y2:.0f})")
            else:
                print("No objects detected.")

            # Optional: small delay to avoid spamming if you like
            # time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopping detection loop.")
    finally:
        picam2.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
