import numpy as np
import cv2
import time
import os


img=[]
lbl=[]
num_list=[]
# ROI框的显示位置
x0 = 0
y0 = 0
# 录制的手势图片大小
width = 480
height = 480
NUM = 7  # 分类数量：0, 1, 2, 3, 4, 5, 6
rang = 1000  # 每个分类的图片数
data_path = r"C:\Users\12485\Desktop\大创模型搭建\UI界面\data"
saved_file_name = 'labeled_img_data_' + str(int(time.time()))
k = np.zeros((7, 7), 'float')
for i in range(7):
    k[i, i] = 1


def skinMask(roi):
    YCrCb = cv2.cvtColor(roi, cv2.COLOR_BGR2YCR_CB)  # 转换至YCrCb空间
    (y, cr, cb) = cv2.split(YCrCb)  # 拆分出Y,Cr,Cb值
    cr1 = cv2.GaussianBlur(cr, (5, 5), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Ostu处理
    res = cv2.bitwise_and(roi, roi, mask=skin)
    return res


def binaryMask(frame, x0, y0, width, height):
    cv2.rectangle(frame, (x0, y0), (x0 + width, y0 + height), (0, 255, 0))  # 画出截取的手势框图
    roi = frame[y0:y0 + height, x0:x0 + width]  # 获取手势框图
    res = skinMask(roi)  # 进行肤色检测
    cv2.imshow("VideoCapture", res)  # 显示肤色检测后的图像
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    return res


def collect_image():
    # 初始化数数
    global img,lbl,num_list
    num_list = [0, 0, 0, 0, 0, 0, 0]
    cap = cv2.VideoCapture(0)
    images = np.zeros((1, 230400), dtype=float)
    labels = np.zeros((1, NUM), dtype=float)
    while 1:
        ret, frame = cap.read()  # 返回的第一个参数为bool类型，用来表示是否读取到帧，如果为False说明已经读到最后一帧。frame为读取到的帧图片
        # 图像翻转（如果没有这一步，视频显示的刚好和我们左右对称）
        frame = cv2.flip(frame, 2)  # 第二个参数大于0：就表示是沿y轴翻转
        # 显示ROI区域 # 调用函数
        res = binaryMask(frame, x0, y0, width, height)
        # slice the lower part of a frame
        command = cv2.waitKey(1) & 0xFF
        if command == ord('q'):  # 保存并退出
            break

        elif command == ord('w'):  # Fist[0]
            if num_list[0] < rang:
                num_list[0] += 1
                res = np.reshape(res, [1, -1])
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[0]))
                print("Fist: ", num_list[0])
            else:
                continue

        elif command == ord('a'):  # Good[1]
            if num_list[1] < rang:
                num_list[1] += 1
                res = np.reshape(res, [1, -1])
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[1]))
                print("Good: ", num_list[1])
            else:
                continue

        elif command == ord('d'):  # No[2]
            if num_list[2] < rang:
                num_list[2] += 1
                res = np.reshape(res, [1, -1])
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[2]))
                print("No: ", num_list[2])
            else:
                continue

        elif command == ord('s'):  # Three[3]
            if num_list[3] < rang:
                num_list[3] += 1
                res = np.reshape(res, [1, -1])
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[3]))
                print("Three: ", num_list[3])
            else:
                continue

        elif command == ord('i'):
            if num_list[4] < rang:
                num_list[4] += 1
                res = np.reshape(res, [1, -1])
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[4]))
                print("Two: ", num_list[4])
            else:
                continue

        elif command == ord('j'):
            if num_list[5] < rang:
                num_list[5] += 1
                res = np.reshape(res, [1, -1])
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[5]))
                print("One: ", num_list[5])
            else:
                continue

        elif command == ord('z'):
            continue

        elif command == ord('c'):
            continue

    img = images[1:, :]
    lbl = labels[1:, :]
    print("image shape:", img.shape)
    print("label shape:", lbl.shape)
    print("Fist images num:", num_list[0])
    print("Good images num:", num_list[1])
    print("No images num:", num_list[2])
    print("Three images num:", num_list[3])
    print("Two images num:", num_list[4])
    print("One images num:", num_list[5])
    cap.release()
    cv2.destroyAllWindows()
    # 保存数据
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    try:
        np.savez(data_path + '/' + saved_file_name + '.npz', train=img, train_labels=lbl, num_list=num_list)
    except IOError as e:
        print(e)

def saveGesture():
    collect_image()

if __name__=="__main__":
    saveGesture()

