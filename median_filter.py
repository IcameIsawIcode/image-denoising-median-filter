"""
A simple implementation of a median filter to reduce noise in grayscale images.
The script takes a noisy image as input, applies a 3x3 median filter, and displays
the denoised result.

Libraries used:
- OpenCV (cv2)
- NumPy

To run:
    python median_filter.py
"""

import cv2
import numpy as np

def median_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
 
    padded_image = np.pad(image, kernel_size // 2, mode='constant', constant_values=0)
    result = np.zeros_like(image)

    rows, cols = image.shape

    for i in range(rows):
        for j in range(cols):
            region = padded_image[i:i+kernel_size, j:j+kernel_size].flatten()
            # Compute the median
            result[i, j] = np.median(region)
    return result
def main():
    # Load the image, here your image goes
    image_path = input("Enter path to the grayscale image: ").strip()
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    noisy = image.copy()

    if image is None:
        print("Error: Could not load image.")
        return

    # Applying the median filter
    denoised = median_filter(noisy, kernel_size=3)
    cv2.imshow("Original Image", image)
    cv2.imshow("Denoised Image (Median Filter)", denoised)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("denoised_output.png", denoised)
    print("Denoised image saved as 'denoised_output.png'.")


if __name__ == "__main__":
    main()
