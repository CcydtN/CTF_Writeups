import cv2
import numpy as np

def sharpen_image(image, sharpening_factor=2.0):
    # Define a custom sharpening kernel
    kernel = np.array([
        [-1, -1, -1],
        [-1, sharpening_factor, -1],
        [-1, -1, -1]
    ])

    # Apply the custom kernel using the filter2D function
    sharpened = cv2.filter2D(image, -1, kernel)

    return sharpened

def find_sharpened_area(image, threshold_value=30):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the original and sharpened images
    diff = cv2.absdiff(gray, cv2.cvtColor(sharpen_image(image), cv2.COLOR_BGR2GRAY))

    # Threshold the difference image to identify sharpened regions
    _, thresholded = cv2.threshold(diff, threshold_value, 255, cv2.THRESH_BINARY)

    # Blur the thresholded image to reduce object outlines
    blurred_thresholded = cv2.GaussianBlur(thresholded, (5, 5), 0)

    # Find contours of the sharpened regions in the blurred image
    contours, _ = cv2.findContours(blurred_thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask for the sharpened area
    mask = np.zeros_like(image)

    # Draw the contours on the mask and fill with red color
    cv2.drawContours(mask, contours, -1, (0, 0, 255), thickness=cv2.FILLED)

    # Add the mask to the original image to highlight the sharpened area
    sharpened_area = cv2.addWeighted(image, 1, mask, 0.5, 0)

    return sharpened_area

# Read the image
original_image = cv2.imread('DF2.jpg')

# Adjust the sharpening factor to control the strength of the sharpening effect
sharpening_factor = 6.7  # Experiment with different values
for _ in range(20):
    sharpened_image = sharpen_image(original_image, sharpening_factor)

# Adjust the threshold value to control the visibility of the sharpened area
threshold_value = 100  # Experiment with different values
highlighted_image = find_sharpened_area(sharpened_image, threshold_value)

# Display the results
cv2.imshow('Original Image', original_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imshow('Highlighted Sharpened Area', highlighted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
