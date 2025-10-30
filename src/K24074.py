import os
import sys
import numpy as np
import cv2

# === ✅ モジュールパスを追加 ===
# K24074.py（src/）の1階層上（= プロジェクトルート）をパスに追加
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

# === ✅ モジュールインポート ===
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture


def lecture05_01():
    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # カメラ画像を取得
    capture_img: cv2.Mat = app.get_img()
    if capture_img is None:
        print("カメラ画像の取得に失敗しました。")
        return

    # 置き換え対象のGoogle画像を読み込む
    google_img: cv2.Mat = cv2.imread(os.path.join(project_root, "images/google.png"))
    if google_img is None:
        pr
