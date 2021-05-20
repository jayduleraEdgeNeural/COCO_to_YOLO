from __future__ import print_function
import argparse
import glob
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument("json", help='Path of the json file containing annotations') 
parser.add_argument("output_path", help='Output directory for image.txt files') 
args = parser.parse_args()

def main():
	with open(args.json) as f:
  		data = json.load(f) 
  	images = data['images']
	annotations = data['annotations']
	for i in range(len(images)):
	  converted_results = []
	  for ann in annotations:
	    if ann['image_id'] == i:
	      cat_id = int(ann['category_id'])
	      height = images[i]['height']
	      width = images[i]['width']
	      left, top, bbox_width, bbox_height = map(float, ann['bbox'])
	      cat_id -= 1
	      x_center, y_center = (left + bbox_width / 2, top + bbox_height / 2)
	      x_rel, y_rel = (x_center / width, y_center / height)
	      w_rel, h_rel = (bbox_width / width, bbox_height / height)
	      converted_results.append((cat_id, x_rel, y_rel, w_rel, h_rel))
	      image_name = images[i]['file_name']
	      file = open(args.output_path + str(image_name) + '.txt', 'w+')
	      file.write('\n'.join('%d %.6f %.6f %.6f %.6f' % res for res in converted_results))
	      file.close()
	print('Conversion completed successfully.')

if __name__ == '__main__':
	main()


            

