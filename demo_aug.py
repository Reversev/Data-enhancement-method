#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/6 14:51
# @Author : 'IReverser'
# @FileName: demo_aug.py

import shutil
import glob
import albumentations as A
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'


def select_aug(img, str):
    im = image
    if str == '1':
        im = A.RGBShift(r_shift_limit=133, g_shift_limit=120, b_shift_limit=26, p=0.56)(image=image)['image']
    elif str == '2':
        im = A.RandomBrightness(limit=0.3, p=0.88)(image=image)['image']  # reduce Brightness randomly
    elif str == '3':
        im = A.RandomBrightness(limit=1.2, p=0.6)(image=image)['image']    # reduce Brightness randomly
    elif str == '4':
        im = A.RandomGamma(gamma_limit=20, p=0.3)(image=image)['image']   # Gamma transformation randomly
    elif str == '5':
        im = A.HueSaturationValue(p=0.3)(image=image)['image']
    elif str == '6':
        im = A.RandomContrast(limit=1.3, p=0.5)(image=image)['image']  # random contrast
    elif str == '7':
        im = A.ImageCompression(quality_lower=80, quality_upper=80, p=0.5)(image=image)['image']
    elif str == '8':
        im = A.Blur(blur_limit=10, p=1)(image=image)['image']
    elif str == '9':
        im = A.Blur(blur_limit=7, p=1)(image=image)['image']
    elif str == '10':
        im = A.MedianBlur(blur_limit=11, p=0.1)(image=image)['image']
    elif str == '11':
        im = A.MotionBlur(p=0.7)(image=image)['image']
    elif str == '12':
        im = A.GaussianBlur(blur_limit=7, p=0.5)(image=image)['image']
    elif str == '13':
        im = A.GlassBlur(sigma=0.6, max_delta=4)(image=image)['image']
    elif str == '14':
        im = A.CLAHE(clip_limit=4.0, tile_grid_size=(10, 10))(image=image)['image']
    elif str == '15' or str == '20' or str == '21':
        # im = A.Superpixels(p=1)(image=image)['image']   # 15
        im = A.Superpixels(p=10)(image=image)['image']    # 20
        im = A.Superpixels(p=5)(image=image)['image']     # 21
    elif str == '16' or str == '18' or str == '19':
        # im = A.GaussNoise(p=10)(image=image)['image']     # 16
        # im = A.GaussNoise(p=100)(image=image)['image']    # 18
        im = A.GaussNoise(p=500)(image=image)['image']       # 19
    elif str == '17':
        im = A.Sharpen(p=1)(image=image)['image']
    return im


if __name__ == "__main__":
    path = './pic/'
    arr = '21'

    for img_path in glob.glob(path + '*jpg'):
        _, name_att = os.path.split(img_path)
        name = name_att.split('.')[0]
        shutil.copyfile(path + str(name) + '.txt', path + str(name) + '_' + arr + '.txt')
        print(img_path)
        image = plt.imread(img_path, 1)
        im = select_aug(image, arr)
        plt.imsave(path + str(name) + '_' + arr + '.jpg', im/255)


