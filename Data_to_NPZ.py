import numpy as np
import cv2
import time
import os

# ROI框的显示位置
x0 = 0
y0 = 0
# 录制的手势图片大小
width = 480
height = 480
NUM = 7  # 分类数量：0, 1, 2, 3, 4, 5, 6
rang = 1000  # 每个分类的图片数
data_path = 'D:/data/train/'
saved_file_name = 'labeled_img_data_' + str(int(time.time()))
k = np.zeros((7, 7), 'float')
for i in range(7):
    k[i, i] = 1


def collect_image():
    # 初始化数数
    gesture = []
    num_list = [0, 0, 0, 0, 0, 0, 0]
    images = np.zeros((1, 230400), dtype=float)
    labels = np.zeros((1, NUM), dtype=float)
    for file in os.listdir(data_path):
        name = file.split(sep='.')
        gesture.append(data_path + file)
        gesture = gesture[0]
        res = cv2.imread(gesture)
        res = cv2.resize(res, (480, 480), interpolation=cv2.INTER_CUBIC)
        res = cv2.cvtColor(np.array(res), cv2.COLOR_BGR2GRAY)
        res = np.reshape(res, [1, -1])
        if name[0] == 'A':  # Fist[0]
            if num_list[0] < rang:
                num_list[0] += 1
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[0]))
                print("Fist: ", num_list[0])
                gesture = []
            else:
                continue

        elif name[0] == 'B':  # Good[1]
            if num_list[1] < rang:
                num_list[1] += 1
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[1]))
                print("Good: ", num_list[1])
                gesture = []
            else:
                continue

        elif name[0] == 'C':  # No[2]
            if num_list[2] < rang:
                num_list[2] += 1
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[2]))
                print("No: ", num_list[2])
                gesture = []
            else:
                continue

        elif name[0] == 'D':  # Three[3]
            if num_list[3] < rang:
                num_list[3] += 1
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[3]))
                print("Three: ", num_list[3])
                gesture = []
            else:
                continue

        elif name[0] == 'E':
            if num_list[4] < rang:
                num_list[4] += 1
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[4]))
                print("Two: ", num_list[4])
                gesture = []
            else:
                continue

        elif name[0] == 'F':
            if num_list[5] < rang:
                num_list[5] += 1
                images = np.vstack((images, res))
                labels = np.vstack((labels, k[5]))
                print("One: ", num_list[5])
                gesture = []
            else:
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
    # 保存数据
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    try:
        np.savez(data_path + '/' + saved_file_name + '.npz', train=img, train_labels=lbl, num_list=num_list)
    except IOError as e:
        print(e)


if __name__ == "__main__":
    collect_image()
