
import sys
import cv2
import datetime

# デフォルトのカメラ
defaultDevideId = 2

# 押されたキーの情報
def showKey(key):
    if key != -1:
        print(f"Pressed {key} ({key:#x}), 2LSB: {key % 2**16} ({repr(chr(key%256)) if key%256 < 128 else '?'})")

# 
def main(devid):
    #カメラの設定　デバイスIDは0
    cap = cv2.VideoCapture(devid)

    #繰り返しのためのwhile文
    while True:
        #カメラからの画像取得
        ret, frame = cap.read()

        #カメラの画像の出力
        cv2.imshow('camera' , frame)

        #繰り返し分から抜けるためのif文
        key =cv2.waitKey(10)
        
        showKey(key)
        if key == 27:       # ESC
            break
        elif key == 113:    # 'q'
            break
        elif key == 119:    # 'w'
            dt_now = datetime.datetime.now()
            dt_str = dt_now.strftime('%Y%m%d%H%M%S')
            img_name = 'ret_' + dt_str + '.jpg'
            cv2.imwrite(img_name, frame)
    

    #メモリを解放して終了するためのコマンド
    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    devid = defaultDevideId if len(sys.argv) < 2 else int(sys.argv[1])
    main(devid)
