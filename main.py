import cv2

# Read the image
image = cv2.imread("harshit.jpg")

# Display the original image in an adjustable window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", image)
cv2.waitKey()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image in an adjustable window
cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)
cv2.imshow("Gray Image", gray_image)
cv2.waitKey()

# Invert the grayscale image
inverted_image = 255 - gray_image

# Display the inverted image in an adjustable window
cv2.namedWindow("Inverted", cv2.WINDOW_NORMAL)
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

# Apply Gaussian blur to the inverted image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# Invert the blurred image
inverted_blurred = 255 - blurred

# Create the pencil sketch by dividing the grayscale image by the inverted blurred image
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Display the pencil sketch in an adjustable window
cv2.namedWindow("Pencil Sketch", cv2.WINDOW_NORMAL)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey()

# Close all windows
cv2.destroyAllWindows()
