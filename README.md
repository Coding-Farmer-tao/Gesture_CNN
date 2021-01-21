## 基于肤色检测和卷积神经网络的手语动作识别

### 项目文件：

项目文件列表如下：

1. `data`：存放采集的数据。

2. `dataset`:存放Train_model_tensorflow.py训练的数据。

3. `model`：存放在网络训练中表现好的模型。

4. `Collect.py`：采集界面。
5. `Data_to_NPZ.py`：图片转.npz文件。用来制作数据集。
6. `Frame.py`：UI界面。使用Python的PyQt5进行设计。
7. `Gesture_CNN.py`：实时手语动作识别。将摄像头实时获取的帧图片送入已训练好的CNN模型中判断其手语动作。
8. `Main.py`：主界面。
9. `SaveGesture.py`：采集数据。利用OpenCV获取帧图像并转为.npz文件（.npz文件是数据训练的格式）
10. `Train_model_tensorflow.py`：模型训练，采用AlexNet结构。TensorFlow=1.4.0
11. `Translate.py`：手语识别界面。
12. `Data_rename`:图片批量重命名。
    项目文件已经上传至我个人的GitHub，有需要的可自行下载。

### 项目内容：

#### 内容简介

项目设定可以识别5种手语动作，大家可根据自己的需求增减动作的种类，但是程序可能需要改动一些地方。采用的数据集是自己采集的。

1. `A`动作  2.`B`动作 3.`C`动作  4.`D`动作  5.`F`动作

同时，项目准备对图像不进行肤色检测，即不对数据进行预处理，直接进行训练。采用的数据集是ASL Alphabet。ASL数据集包含 87，000 张图像，即 200x200 像素，总共有29个类。

[ASL](https://www.kaggle.com/grassknoted/asl-alphabet)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210121121653926.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDg1Mjk1NA==,size_16,color_FFFFFF,t_70#pic_center)

整体的界面设计是利用PyQt5进行设计的，主要是因为PyQt5开发迅速，学习成本低，界面预览如下。

![主界面](https://img-blog.csdnimg.cn/20210121122427874.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDg1Mjk1NA==,size_16,color_FFFFFF,t_70#pic_center)

![采集界面](https://img-blog.csdnimg.cn/20210121122613630.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDg1Mjk1NA==,size_16,color_FFFFFF,t_70#pic_center)

#### 肤色检测

别的大佬解释肤色检测的基本原理更为详细，这里不做赘述。（下图为项目实现的肤色检测）
[肤色检测](https://blog.csdn.net/shadow_guo/article/details/43635181?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161120181916780266275169%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161120181916780266275169&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-43635181.first_rank_v2_pc_rank_v29&utm_term=%E8%82%A4%E8%89%B2%E6%A3%80%E6%B5%8B%20Python&spm=1018.2226.3001.4187)

![肤色检测前](https://img-blog.csdnimg.cn/20210121123255104.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDg1Mjk1NA==,size_16,color_FFFFFF,t_70#pic_center)

![肤色检测后](https://img-blog.csdnimg.cn/20210121122901907.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDg1Mjk1NA==,size_16,color_FFFFFF,t_70#pic_center)


#### 卷积神经网络

这个项目采用的是CNN经典模型的AlexNet，大家可以参考AlexNet设计者对AlexNet的分析。（论文链接如下）

[ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)

#### 测试结果

具体测试还得回学校用高端机训练，笔记本过于乐色，训练太慢！！！

#### 未来期望

 - 用YOLO代替肤色检测，解决了当人物离摄像头较远时肤色检测失效的问题，能够增强整体的鲁棒性。
 - 这个项目只适用于静态手语动作的识别，而现实生活中更多的是动态的手语动作，希望大家在这个项目的基础之上能够加入时间序列，实现动态手语动作的识别。

### 总结：

这篇文章是我在寒假做大创的过程中突然想写的，这也是我第一次写这么正式的博客，可能中间有许多的漏洞，希望大家能多多指正。







