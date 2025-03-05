import cv2

def resize_and_display(image_path):
    
    image = cv2.imread(image_path)
    
    sizes = [(300, 300), (600, 400), (800, 600)]
    
    for idx, (width, height) in enumerate(sizes, start=1):
        resized_image = cv2.resize(image, (width, height))
        cv2.imshow(f'Resized Image {idx}: {width}x{height}', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'dog.jpg'
resize_and_display(image_path)
