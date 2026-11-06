# ==============================================================================
# Developed By: Mithik jain G
# Register No: 212224240087
# Experiment 4: Geometric Transformations Using OpenCV
# ==============================================================================

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    image_path = 'image3.jpg'
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)

    # 1. Load Original Image
    image = cv2.imread(image_path)
    if image is None:
        print(f"[ERROR] Could not load image from '{image_path}'.")
        return

    # Display & Save Original Image
    plt.figure()
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "original_image.png"))
    plt.close()
    print("[SUCCESS] Original image processed.")

    # 2. Image Translation
    tx, ty = 100, 50
    M_translation = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, M_translation, (image.shape[1], image.shape[0]))

    plt.figure()
    plt.imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
    plt.title("Translated Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "translated_image.png"))
    plt.close()
    print("[SUCCESS] Translated image saved.")

    # 3. Image Scaling
    fx, fy = 5.0, 2.0
    scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)

    plt.figure()
    plt.imshow(cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB))
    plt.title("Scaled Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "scaled_image.png"))
    plt.close()
    print("[SUCCESS] Scaled image saved.")

    # 4. Image Shearing
    shear_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])
    sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))

    plt.figure()
    plt.imshow(cv2.cvtColor(sheared_image, cv2.COLOR_BGR2RGB))
    plt.title("Sheared Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "sheared_image.png"))
    plt.close()
    print("[SUCCESS] Sheared image saved.")

    # 5. Image Reflection
    reflected_image = cv2.flip(image, 2)

    plt.figure()
    plt.imshow(cv2.cvtColor(reflected_image, cv2.COLOR_BGR2RGB))
    plt.title("Reflected Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "reflected_image.png"))
    plt.close()
    print("[SUCCESS] Reflected image saved.")

    # 6. Image Rotation
    (height, width) = image.shape[:2]
    angle = 45
    center = (width // 2, height // 2)
    M_rotation = cv2.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv2.warpAffine(image, M_rotation, (width, height))

    plt.figure()
    plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
    plt.title("Rotated Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "rotated_image.png"))
    plt.close()
    print("[SUCCESS] Rotated image saved.")

    # 7. Image Cropping
    x, y, w, h = 100, 100, 200, 150
    cropped_image = image[y:y+h, x:x+w]

    plt.figure()
    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.title("Cropped Image")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "cropped_image.png"))
    plt.close()
    print("[SUCCESS] Cropped image saved.")

if __name__ == "__main__":
    main()
