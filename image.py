import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
  plt.figure(figsize = (8, 8))
  if len(image.shape) == 3:
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  else:
    plt.imshow(image, cmap = 'gray')
  plt.title(title)
  plt.show()

def interactive_edge_detection(image_path):
  image = cv2.imread(image_path)
  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  display_image('Original Image', image_gray)

  print('Select Option')
  print('1. Canny Edge Detection')
  print('2. Laplacian Edge Detection')
  print('3. Sobel Edge Detection')
  print('4. Gaussian Smoothing')
  print('5. Median Filtering')
  print('6. Exit')

  while True:
    option = int(input('Enter Option: '))
    if option == 1:
      upper_t = int(input('Enter Upper Threshold: '))
      lower_t = int(input('Enter Lower Threshold: '))
      edges = cv2.Canny(image_gray, lower_t, upper_t)
      display_image('Canny Edge Detection', edges)
    elif option == 2:
      edges = cv2.Laplacian(image_gray, cv2.CV_64F)
      display_image('Laplacian Edge Detection', edges)
    elif option == 3:
      edges = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize = 3)
      display_image('Sobel Edge Detection', edges)
    elif option == 4:
      kernel_size = int(input('Enter Kernel Size: '))
      blurred = cv2.GaussianBlur(image_gray, (kernel_size, kernel_size), 0)
      display_image('Gaussian Smoothing', blurred)
    elif option == 5:
      kernel_size = int(input('Enter Kernel Size: '))
      blurred = cv2.medianBlur(image_gray, kernel_size)
      display_image('Median Filtering', blurred)
    elif option == 6:
      break
    else:
      print('Invalid Option')

interactive_edge_detection('image.jpg')