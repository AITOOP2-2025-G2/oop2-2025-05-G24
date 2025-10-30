import numpy as np
import cv2
import os
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture


def lecture05_01():
    """
    Google検索画面の白色部分をカメラ画像で置換し、output_imagesフォルダに保存するプログラム。
    """

    # === 1. カメラキャプチャ実行 ===
    app = MyVideoCapture()
    app.run()

    # メモリ上にキャプチャ画像を取得
    capture_img: np.ndarray | None = app.get_img()
    if capture_img is None:
        print("カメラ画像が取得できませんでした。")
        return

    # === 2. Google画像読み込み ===
    google_img: cv2.Mat = cv2.imread('images/google.png')
    if google_img is None:
        print("google.png が見つかりません。images フォルダに配置してください。")
        return

    g_height, g_width, _ = google_img.shape
    c_height, c_width, _ = capture_img.shape
    print(f"Google画像サイズ: {g_width}x{g_height}")
    print(f"カメラ画像サイズ: {c_width}x{c_height}")

    # === 3. 白色部分の置換処理 ===
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = capture_img[y % c_height, x % c_width]

    # === 4. 出力フォルダを確認して保存 ===
    output_dir = 'output_images'
    os.makedirs(output_dir, exist_ok=True)  # フォルダがない場合は自動作成

    output_path = os.path.join(output_dir, 'lecture05_01_K24059.png')
    cv2.imwrite(output_path, google_img)
    print(f"置換後の画像を {output_path} に保存しました。")


if __name__ == "__main__":
    lecture05_01()
