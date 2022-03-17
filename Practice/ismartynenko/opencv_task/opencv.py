import argparse
import math
import os
import cv2
import numpy
from PIL import Image, ImageDraw


def image_match_template(current_img_path, pattern_img_path):
    current_img = Image.open(current_img_path)
    pattern_img = Image.open(pattern_img_path)
    current_img_arr = cv2.cvtColor(numpy.array(current_img), cv2.COLOR_RGB2BGR555)
    pattern_img_arr = cv2.cvtColor(numpy.array(pattern_img), cv2.COLOR_RGB2BGR555)
    res = cv2.matchTemplate(current_img_arr, pattern_img_arr, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    size = pattern_img_arr.shape
    closest_area = [max_loc[0], max_loc[1], max_loc[0] + size[1], max_loc[1] + size[0]]
    return max_val, closest_area


def screen_graphical_result(current_img_file, bbox):
    current_img = Image.open(current_img_file)
    ImageDraw.Draw(current_img).rectangle(xy=bbox, outline=(255, 0, 0), width=10)
    result_file_name = f'result_{os.path.basename(current_img_file)}'
    current_img.save(result_file_name)
    return result_file_name


def parse_args():
    parser = argparse.ArgumentParser(description='Searches for pattern in image')
    parser.add_argument('-s', '--source', help='Path to source file')
    parser.add_argument('-p', '--pattern', help='Path to pattern file')
    parser.add_argument('-i', '--ignore-color', type=bool, default=False, help='Ignore color')
    return parser.parse_args()


def counter(img_file, params):
    img = cv2.imread(img_file)
    img_h, img_w, _ = img.shape

    point_x = (params[0] + params[2]) / 2
    point_y = (params[1] + params[3]) / 2

    center_x = int(img_w/2)
    center_y = int(img_h/2)
    rad = int(math.hypot(center_x - point_x, center_y - point_y))

    num = 0
    tup = (439, 398, 357, 316, 275, 234, 193, 152, 111, 70)
    for i, j in enumerate(tup, start=1):
        if rad <= j:
            num = i
    print(num)


if __name__ == "__main__":
    args = parse_args()
    max_val, closest_area = image_match_template(args.source, args.pattern)
    res_file_name = screen_graphical_result(args.source, closest_area)
    print(f"Pattern found with confidence {max_val}. Open {res_file_name} for details")
    if max_val < 0.5:
        print("Looser")
    else:
        counter(args.source, closest_area)
