import cv2
import datetime
import time
import os

def motion_detection():
    cap = cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    motion_counter = 0
    photo_counter = 0

    # Créer un dossier pour sauvegarder les photos si il n'existe pas
    if not os.path.exists("motion_captures"):
        os.makedirs("motion_captures")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        blur_frame = cv2.GaussianBlur(frame, (21, 21), 0)
        grey_frame = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2GRAY)
        fgmask = fgbg.apply(grey_frame)
        thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)[1]
        dilate_image = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(dilate_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False
        if contours:
            for c in contours:
                if cv2.contourArea(c) > 300:
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 0), 2)
                    motion_detected = True

        if motion_detected:
            motion_counter += 1
            current_time = datetime.datetime.now().strftime('%Y-%m-%d heure %H-%M-%S')
            with open("motion_log.txt", "a") as log_file:
                log_file.write(f"{current_time} il y a eu un mouvement chez vous\n")

            # Prendre une photo tous les 20 mouvements
            if motion_counter % 20000 == 0:
                photo_counter += 1
                photo_filename = f"motion_captures/capture_{photo_counter}_{current_time}.jpg"
                cv2.imwrite(photo_filename, frame)
                print(f"Photo sauvegardée: {photo_filename}")

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

motion_detection()