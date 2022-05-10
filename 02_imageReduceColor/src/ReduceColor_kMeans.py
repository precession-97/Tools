# kmean_recolored.py #  プログラム名

import os
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import MiniBatchKMeans

if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        # 引数から対象画像のパスを取得
        img_path = os.path.join('../input/', args[1])

        # 画像の読み込み
        image = cv2.imread(img_path)

        # imageのデータ形状確認
        print(image.shape)

        # 画像サイズ取得
        h, w = image.shape[:2]

        image_tmp = image.reshape(h*w, 3)

        # imageのデータを正規化して（255.0で割って）0.0～1.0の間にデータをおさめる
        image_1 = image / 255.0

        # image_1のデータ形状を変形（全ピクセル数, 色ch数）
        image_1 = image_1.reshape(h*w, 3)

        # image_1のデータ形状確認
        print('image_1=',image_1.shape)


        ### k平均法によるカラー圧縮 ###
        # パラメータ
        color_n = 1024  # 色数

        # 計算
        kmeans = MiniBatchKMeans(n_clusters = color_n, batch_size=1024)
        kmeans.fit(image_1)
        new_colors = kmeans.cluster_centers_[kmeans.predict(image_1)]

        # new_colorsのデータ形状確認
        print('new_colors=', new_colors.shape)

        # imageの形状を整形
        img_recolored = new_colors.reshape(image.shape)
        img_recolored = img_recolored * 255.0
        img_recolored = img_recolored.astype(np.uint8)

        # img_recoloredの形状を確認
        print('img_recolored=', img_recolored.shape)

        # img_recolored画像を1枚だけ保存
        outputFileName = os.path.splitext(os.path.basename(args[1]))[0] + '.bmp'
        cv2.imwrite(os.path.join('../output/', outputFileName), img_recolored)
    else:
        print('Arguments are too short')