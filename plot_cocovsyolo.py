import cv2
import numpy as np
import json
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("img_path", help='Path of the image') 
parser.add_argument("label_path", help='Path of YOLO .txt label file') 
parser.add_argument("coco_path", help='Path of COCO label json file') 
parser.add_argument("img_id", help='ID of image') 
args = parser.parse_args()

def plot_yolo(img_path , label_path):
  img = cv2.imread(img_path)
  dh, dw, _ = img.shape
  fl = open(label_path, 'r')
  data = fl.readlines()
  fl.close()
  for dt in data:
      _, x, y, w, h = map(float, dt.split(' '))
      l = int((x - w / 2) * dw)
      r = int((x + w / 2) * dw)
      t = int((y - h / 2) * dh)
      b = int((y + h / 2) * dh)
      if l < 0:
          l = 0
      if r > dw - 1:
          r = dw - 1
      if t < 0:
          t = 0
      if b > dh - 1:
          b = dh - 1
      cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)
  plt.imshow(img)
  plt.title('YOLO Bounding Box')
  plt.show()

def plot_coco(coco_path , img_path , image_id):
	with open(coco_path) as file:
	   annotations = json.load(file)
	   plt.figure()
	   plt.title('COCO Bounding Boxes')
	   img = cv2.imread(img_path)
	   plt.imshow(img)
	   ann = annotations['annotations']
	   for i in ann:
	     if i['image_id'] == image_id:
	       box = i['bbox']
	       label = i['category_id']
	       x = box[0]
	       y = box[1]
	       w = box[2]
	       h = box[3]
	       rect = Rectangle((x , y) , (w - xmin), (h - ymin), fill=False, color = 'blue', label= label)
	       plt.axes().add_patch(rect)
	       plt.text(xmax + 5 , ymax , label)
def main():
	plot_yolo(args.img_path , args.label_path)
	plot_coco(args.coco_path , args.img_path , args.image_id)

if __name__ == '__main__':
	main()

