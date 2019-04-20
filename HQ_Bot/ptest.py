

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from PIL import Image
import pytesseract
import argparse
import cv2
import pyscreenshot as Imagegrab
from threading import Thread


from project_utils import testing_utils





def extract_text_from_image(img_path, lang = 'eng'):    
    image = cv2.imread(img_path)
#     cv2.imshow("Original", image)
    
    # Apply an "average" blur to the image
    
#     blurred = cv2.blur(image, (3,3))
# # #     cv2.imshow("Blurred_image", blurred)
#     img = Image.fromarray(blurred)

    text = pytesseract.image_to_string(image, lang)
    
    return text


print(extract_text_from_image("S:\\Downloads\\test_pdf.png"))






