import numpy as np
import tensorflow as tf
import cv2

x0 = 0
y0 = 0
width = 480
height = 480
channel = 1
inference_path = tf.Graph()
filepath = r'C:\Users\12485\Desktop\model\auto_drive_model\-546'
temp_image = np.zeros(width * height * channel, 'uint8')
value = 0


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
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    return res


def auto_pilot():
    cap = cv2.VideoCapture(0)
    global value
    with tf.Session(graph=inference_path) as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        saver = tf.train.import_meta_graph(filepath + '.meta')
        saver.restore(sess, filepath)

        tf_X = sess.graph.get_tensor_by_name('input:0')
        pred = sess.graph.get_operation_by_name('pred')
        number = pred.outputs[0]
        prediction = tf.argmax(number, 1)

        while cap.isOpened():
            ret, frame = cap.read()  # 返回的第一个参数为bool类型，用来表示是否读取到帧，如果为False说明已经读到最后一帧。frame为读取到的帧图片
            # 图像翻转（如果没有这一步，视频显示的刚好和我们左右对称）
            frame = cv2.flip(frame, 2)  # 第二个参数大于0：就表示是沿y轴翻转
            # 显示ROI区域 # 调用函数
            res = binaryMask(frame, x0, y0, width, height)
            cv2.imshow("frame", res)
            cv2.waitKey(1)
            frame = np.array(res, dtype=np.float32)
            value = prediction.eval(feed_dict={tf_X: np.reshape(frame, [-1, height, width, channel])})
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()


if __name__ == '__main__':
    auto_pilot()
