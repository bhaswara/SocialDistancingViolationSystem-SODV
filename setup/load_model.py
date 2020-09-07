import cv2
import numpy as np

def loading_dependencies():

    net = cv2.dnn.readNet("utils/model/yolov3.weights", "utils/model/yolov3.cfg")

    classes = []

    with open("utils/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    
    return net, output_layers, classes