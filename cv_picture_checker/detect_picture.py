import cv2
from pdf2image import convert_from_path
import os

# Path to poppler bin folder
POPPLER_PATH = r"C:\poppler-24.08.0\Library\bin"

def pdf_to_image(pdf_path):
    """Converts the first page of a PDF to an image and saves it."""
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    original_img_path = "converted_page.jpg"
    images[0].save(original_img_path, "JPEG")
    return original_img_path

def detect_and_save_face(image_path):
    """Detects face and saves image with a rectangle around the face."""
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        output_path = "output_with_face.jpg"
        cv2.imwrite(output_path, img)
        return True, output_path
    return False, None

def check_cv_for_picture(cv_path):
    if not os.path.exists(cv_path):
        print("❌ CV file not found.")
        return

    print("📄 Processing CV:", cv_path)
    try:
        image_path = pdf_to_image(cv_path)
        has_face, face_img_path = detect_and_save_face(image_path)

        if has_face:
            print(f"✅ Profile Picture Detected. Saved to: {face_img_path}")
        else:
            print("🚫 No Profile Picture Found.")
    except Exception as e:
        print("⚠️ Error during processing:", e)

if __name__ == "__main__":
    cv_path = r"D:\python-django-test\dev_test_nima\cv_picture_checker\Nima patel Resume new.pdf"
    check_cv_for_picture(cv_path)
