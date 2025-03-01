from ultralytics import YOLO
import cv2
model=YOLO("yolo12n.pt")
model.to("mps")
results=model("/Users/arpitsharma/cvision/Images/363140724.jpg")
results[0].show()

# # Detection of Objects in real time
# model(0,save=False)
# Open webcam

cap = cv2.VideoCapture(0)  # Ensure the correct index

if not cap.isOpened():
    print("Cannot open the webcam!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Predict on the frame
    results = model(frame)

    # Display results
    annotated_frame = results[0].plot()  # Get annotated frame
    cv2.imshow("Webcam", annotated_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

