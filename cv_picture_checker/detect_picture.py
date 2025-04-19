import cv2
from pdf2image import convert_from_path
import os
import sys


def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=r"C:\poppler-24.08.0\Library\bin")
    image_path = "converted_page.jpg"
    images[0].save(image_path, "JPEG")
    return image_path

def detect_face(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return len(faces) > 0

def check_cv_for_picture(cv_path):
    if not os.path.exists(cv_path):
        print("❌ CV file not found.")
        return
    print("📄 Processing CV:", cv_path)
    try:
        img_path = pdf_to_image(cv_path)
        has_picture = detect_face(img_path)
        os.remove(img_path)
        if has_picture:
            print("✅ Profile Picture Detected in CV.")
        else:
            print("🚫 No Profile Picture Found in CV.")
    except Exception as e:
        print("⚠️ Error during processing:", e)

if __name__ == "__main__":
    cv_path = r"D:\python-django-test\dev_test_nima\cv_picture_checker\Nima patel Resume new.pdf"
    check_cv_for_picture(cv_path)
