import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "increased_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decreased_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    return filtered_image

image_path = 'gg.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to load the image.")
else:
    print("Image loaded successfully.")

    filter_type = 'original'
    
    print('PRESS TO APPLY FILTER')
    print('r - Red Tint')
    print('g - Green Tint')
    print('b - Blue Tint')
    print('i - increase Red')
    print('d - decrease Blue')
    print('e - EXIT')

    while True:
      filtered_image = apply_color_filter(image, filter_type)
      cv2.imshow('Filtered Image', filtered_image)

      key = cv2.waitKey(0)

      if key == ord('r'):
          filter_type = 'red_tint'
      elif key == ord('g'):
          filter_type = 'green_tint'
      elif key == ord('b'):
          filter_type = 'blue_tint'
      elif key == ord('i'):
          filter_type = 'increased_red'
      elif key == ord('d'):
          filter_type = 'decreased_blue'
      elif key == ord('e'):
        print('EXITIING')
        break
      else:
        print('Invalid pressed key')

    cv2.destroyAllWindows()

print('DONE')