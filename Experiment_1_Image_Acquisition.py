         import cv2

         image = cv2.imread(r'C:/Users/N.YUGESH/Downloads/231126.jpg')

         if image is None:
             print("Error: Image not found") 
         else:
             cv2.imshow('Acquired Image', image)
             cv2.waitKey(0) cv2.destroyAllWindows()
