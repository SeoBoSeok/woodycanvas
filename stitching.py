import os
import math
from PIL import Image
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

"""\
image_stitching.py
function resize
파일 이름을 받아서 열고 이미지의 크기가 1MB보다 크면
크기를 점점 줄여나가서 1MB보다 작게 되면 해당 이미지를 리턴하는 함수
처음부터 1MB보다 작다면 그대로 리턴
"""
def resize(filename):
    img = cv2.imread(filename)
    width, height = img.shape[:2]
    if height * width * 3 <= 2 ** 25:
        return img
    i = 2
    t_height, t_width = height, width
    while t_height * t_width * 3 > 2 ** 25:
        t_height = int(t_height / math.sqrt(i))
        t_width = int(t_width / math.sqrt(i))
        i += 1
    height, width = t_height, t_width
    image = Image.open(filename)
    resize_image = image.resize((height, width))
    filename = filename[:-1 * (len(filename.split(".")[-1]) + 1)] + "_resized." + filename.split(".")[-1]
    resize_image.save(filename)
    img = cv2.imread(filename)
    os.system("del " + filename.replace("/", "\\"))
    return img
  
"""\
image_stitching.py
argument parsing
-i 입력 이미지들의 폴더 디렉토리
-o 출력할 결과 이미지의 파일 이름
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
                help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True,
                help="path to the output image")
args = vars(ap.parse_args())

"""\
image_stitching.py
loading images
입력 받은 폴더의 모든 파일들을 리사이즈 시키고 리스트에 로드하는 부분
"""
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []

for imagePath in imagePaths:
    image = resize(imagePath)
    images.append(image)
    
"""\
image_stitching.py
image stitching
이미지 스티칭하여 성공 여부(status)와 결과(stitched)를 받는 부분
"""
print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

"""\
image_stitching.py
exception handling
status가 0인 경우(stitching 성공) 이미지를 아까 받은 이름으로 저장하고 보여준다.
status가 0이 아닌 경우(stitching 실패 예외)의 메시지를 출력한다.
    1 : 이미지를 연결 시키기에 match point가 부족해서 나오는 에러, 이미지를 더 추가시켜줘야 한다.
    2 : 2D 이미지 변환을 하지 못하는 에러, 이미지를 다시 찍는 것을 추천한다.
    3 : 카메라 위치의 에러, 카메라의 방향이 잘못돼서 나오는 에러, 입력 이미지들을 같은 방향으로 회전시키거나 새로운 이미지를 찍어야 한다.
"""
if status == 0:
    # write the output stitched image to disk
    cv2.imwrite(args["output"], stitched)

    # display the output stitched image to our screen
    # cv2.imshow("Stitched", stitched)
    # cv2.waitKey(0)
else:
    if status == cv2.STITCHER_ERR_NEED_MORE_IMGS:
        print("[INFO] image stitching failed (1: STITCHER_ERR_NEED_MORE_IMGS)")
    elif status == cv2.STITCHER_ERR_HOMOGRAPHY_EST_FAIL:
        print("[INFO] image stitching failed (2: STITCHER_ERR_HOMOGRAPHY_EST_FAIL)")
    else:
        print("[INFO] image stitching failed (3: STITCHER_ERR_CAMERA_PARAMETERS_ADJUSTMENT_FAIL)")

print("stitching end")
        
if __name__ == '__main__':
    print(__doc__)