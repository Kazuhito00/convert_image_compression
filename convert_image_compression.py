#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import argparse
from tqdm import tqdm

import cv2 as cv


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("src", type=str)
    parser.add_argument("dst", type=str)
    parser.add_argument(
        "--mode",
        type=int,
        default=0,
        choices=[0, 1],  # 0:JPG→PNG 1:PNG→JPG
    )

    args = parser.parse_args()

    return args


setting = [
    # 0:JPG→PNG
    [
        'Convert JPG→PNG',
        '*.jpg',
        '.png',
        [int(cv.IMWRITE_PNG_COMPRESSION), 0],
    ],
    # 1:PNG→JPG
    [
        'Convert PNG→JPG',
        '*.png',
        '.jpg',
        [int(cv.IMWRITE_JPEG_QUALITY), 100],
    ],
]


def main():
    # コマンドライン引数
    args = get_args()
    src = args.src
    dst = args.dst
    mode = args.mode

    print(setting[mode][0])

    # 保存先ディレクトリ生成
    os.makedirs(dst, exist_ok=True)

    # 変換対象ファイルリスト
    file_list = glob.glob(os.path.join(src, setting[mode][1]))

    # 変換
    for image_path in tqdm(file_list):
        # 画像読み出し
        image = cv.imread(image_path)

        # 保存先パス生成
        basename = os.path.splitext(os.path.basename(image_path))[0]
        save_path = os.path.join(dst, basename + setting[mode][2])

        # 保存
        cv.imwrite(save_path, image, setting[mode][3])


if __name__ == '__main__':
    main()
