from paddleocr import PaddleOCR
from PIL import Image, ImageDraw, ImageFont
import cv2 as cv

img = cv.imread(r'.\mkScoreboardScreenshots\music.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
# global thresholding
h, w = img.shape
img = img[int(0.075*h):h-int(0.075*h), int(0.5078125*w):w-int(0.2578125*w)]
h, w = img.shape
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
#blur = cv.GaussianBlur(img,(5,5),0)
# mean filter (crap)
#blur = cv.blur(img, (5,5))
# median filter (bad)
#blur = cv.medianBlur(img,5)
# bilateral filter (meh)
blur = cv.bilateralFilter(img, 2, 200,200)
ret3,th3 = cv.threshold(blur,195,255,cv.THRESH_BINARY)
th3 = cv.dilate(th3, cv.getStructuringElement(cv.MORPH_RECT,(2,2)), iterations=1)
th3 = cv.morphologyEx(th3, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_RECT,(2,1)))
#th3 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,3,10)
th3 = cv.rectangle(th3, (0,0),(30,h),(0,0,0),cv.FILLED)
#th3 = cv.dilate(th3, cv.getStructuringElement(cv.MORPH_RECT,(2,2)), iterations=1)
#contours, hierarchy = cv.findContours(th3,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
#th3 = cv.drawContours(th3, contours, -1, (0,0,0), 8)
#th3 = cv.morphologyEx(th3, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
cv.imwrite("temp.png",th3)

# Initialize OCR engine
ocr = PaddleOCR(use_angle_cls=False, lang="ch", det_lang="ml")
# r'C:\Users\evanm\Downloads\monoTableEditdkSummit.jpg'
img_path = 'temp.png'
slice = {'horizontal_stride': w, 'vertical_stride': int(h/12), 'merge_x_thres': 50, 'merge_y_thres': 35}
results = ocr.ocr(img_path, cls=False, slice=slice)

for idx in range(len(results)):
    res = results[idx]
    for line in res:
        print(line)

# Load image
image = Image.open(img_path).convert("RGB")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("./fonts/simfang.ttf", size=20)  # Adjust size as needed

# Process and draw results
for res in results:
    for line in res:
        box = [tuple(point) for point in line[0]]
        # Finding the bounding box
        box = [(min(point[0] for point in box), min(point[1] for point in box)),
               (max(point[0] for point in box), max(point[1] for point in box))]
        txt = line[1][0]
        draw.rectangle(box, outline="red", width=2)  # Draw rectangle
        draw.text((box[0][0], box[0][1] - 25), txt, fill="white", font=font, stroke_width=2, stroke_fill="black")  # Draw text above the box

# Save result
image.save("result.jpg")