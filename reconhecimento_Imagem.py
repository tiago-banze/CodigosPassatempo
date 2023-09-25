import cv2

# Carregar um modelo de detecção de objetos (por exemplo, YOLO)
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Substitua com o caminho correto
classes = []
with open("coco.names", "r") as f:  # Arquivo contendo os nomes das classes
    classes = f.read().strip().split("\n")

# Captura de vídeo da câmera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detectar objetos no frame
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(net.getUnconnectedOutLayersNames())

    # Processar saída da detecção
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = scores.argmax()
            confidence = scores[class_id]
            if confidence > 0.5:  # Limiar de confiança
                label = f"{classes[class_id]}: {confidence:.2f}"
                cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Detecção de Objetos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
