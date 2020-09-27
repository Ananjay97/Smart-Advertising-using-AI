import cv2
import argparse


def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
    return frameOpencvDnn, faceBoxes


parser = argparse.ArgumentParser()
parser.add_argument('--image')

args = parser.parse_args()

faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"
genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-22)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

faceNet = cv2.dnn.readNet(faceModel, faceProto)
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)

video = cv2.VideoCapture(args.image if args.image else 0)
padding = 20

while cv2.waitKey() < 0:
    hasFrame, frame = video.read()
    if not hasFrame:
        cv2.waitKey()
        break

    resultImg, faceBoxes = highlightFace(faceNet, frame)
    if not faceBoxes:
        print("No face detected")

    for faceBox in faceBoxes:
        face = frame[max(0, faceBox[1] - padding):
                     min(faceBox[3] + padding, frame.shape[0] - 1), max(0, faceBox[0] - padding)
                                                                    :min(faceBox[2] + padding, frame.shape[1] - 1)]

        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]
        print(f'Gender: {gender}')

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]
        print(f'Age: {age[1:-1]} years')

        cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                    (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Detecting Age and Gender", resultImg)

        while (cv2.waitKey(1) != ord('q')):
            for i in genderList:
                if (i == gender):
                    if (gender == 'Male'):
                        for j in ageList:
                            if (j == age):
                                if (age == '(0-2)' or age == '(4-6)' or age == '(8-12)'):
                                    cap = capture = cv2.VideoCapture('Mvideo/child.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('0-12', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                                elif (age == '(15-22)'):
                                    cap = capture = cv2.VideoCapture('Mvideo/teen.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('15-22', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                                elif (age == '(25-32)'):
                                    cap = capture = cv2.VideoCapture('Mvideo/adult.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('25-32', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                                elif (age == '(38-43)'):
                                    cap = capture = cv2.VideoCapture('Mvideo/middle.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('38-43', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                                elif (age == '(48-53)' or age == '(60-100)'):
                                    cap = capture = cv2.VideoCapture('Mvideo/old.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('48-100', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                    if (gender == 'Female'):
                        for j in ageList:
                            if (j == age):
                                if (age == '(0-2)' or age == '(4-6)' or age == '(8-12)'):
                                    cap = capture = cv2.VideoCapture('Fvideo/fchild.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('frame', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                                elif (age == '(15-22)'):
                                    cap = capture = cv2.VideoCapture('Fvideo/fteen.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('frame', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                                elif (age == '(25-32)'):
                                    cap = capture = cv2.VideoCapture('Fvideo/fadult.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('frame', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                                elif (age == '(38-43)'):
                                    cap = capture = cv2.VideoCapture('Fvideo/fmiddle.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('frame', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()

                                elif (age == '(48-53)' or age == '(60-100)'):
                                    cap = capture = cv2.VideoCapture('Fvideo/fold.mp4')  // Place your video location here //
                                    while (cap.isOpened()):
                                        ret, frame = cap.read()

                                        cv2.imshow('frame', frame)
                                        if (cv2.waitKey(15) == ord('q')):
                                            break

                                    cap.release()
                                    cv2.destroyAllWindows()




