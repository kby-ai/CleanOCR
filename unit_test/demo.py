import os
import sys
sys.path.append('.')
import glob
import cv2
import numpy as np
from kbyocr import denoise_ocr, denoise_ocr_on_patch, thinning, binarization


def test():
    image = cv2.imread('unit_test/test.png')
    result = denoise_ocr_on_patch(image)
    cv2.imwrite('unit_test/result.png', result)


def test_org():
    image = cv2.imread('unit_test/test1.png')

    dst_img = denoise_ocr(image)

    cv2.imwrite('unit_test/result.png', dst_img)


def test_dir():
    image_list = glob.glob('unit_test/train_cleaned/*.png')
    for path in image_list:
        filename = os.path.basename(path)
        image = cv2.imread(path)
        result = denoise_ocr_on_patch(image)
        dst_path = os.path.join('unit_test/train_result', filename)
        cv2.imwrite(dst_path, result)


def test_thinning():
    image = cv2.imread('unit_test/result.png')
    result = thinning(image)
    cv2.imwrite('unit_test/thin.png', result)


def test_binarization():
    image = cv2.imread('unit_test/result.png')
    result = binarization(image)
    cv2.imwrite('unit_test/binary.png', result)


if __name__ == '__main__':
    test()
    test_org()
    test_thinning()
    test_binarization()

