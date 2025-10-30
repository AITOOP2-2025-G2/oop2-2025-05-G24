import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # --- "implement me" 1 ---
    capture_img: cv2.Mat | None = app.get_img()


    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    
    # (エラーチェック) Google画像が読み込めない場合
    if google_img is None:
        print("エラー: 'images/google.png' が見つかりません。")
        return

    # 提出時にはこの行は不要です (app.get_img() を使うため)
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') 

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape

    print(f"Google画像サイズ: {google_img.shape}")
    print(f"キャプチャ画像サイズ: {capture_img.shape}")

    print("画像の合成処理を開始します...(時間がかかる場合があります)")

    for y in range(g_hight):  # 0 から 639 まで
        for x in range(g_width):  # 0 から 1279 まで
            b, g, r = google_img[y, x]
            
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                
                # --- "implement me" 2 ---
                # capture_img の (y, x) ピクセルで置き換える
                # ただし、サイズが違うため、剰余(%)を使って座標を計算する
                
                # y (0..639) % c_hight (480) -> 0..479, 0..159 
                # x (0..1279) % c_width (640) -> 0..639, 0..639
                
                capture_y = y % c_hight
                capture_x = x % c_width
                
                # google_img の (y,x) を capture_img の (capture_y, capture_x) で上書き
                google_img[y, x] = capture_img[capture_y, capture_x]
                # --------------------------

    # --- "implement me" 3 ---
    # 書き込み処理
    output_filename = 'google_capture_composite.png'
    cv2.imwrite(output_filename, google_img)
    # --------------------------
    
    print(f"処理が完了しました。'{output_filename}' として保存しました。")

# このファイルが直接実行された時だけ lecture05_01 を呼ぶ
if __name__ == "__main__":
    lecture05_01()
