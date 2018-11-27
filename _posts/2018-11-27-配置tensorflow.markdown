一、查看系统所安装的python版本


```
python
```

二、安装python对应版本的pip和依赖包

```
sudo apt-get install python-pip python-dev //若python版本为2.7
sudo apt-get install python3-pip python3-dev //若python版本为3.x

```


三、升级pip版本

```
python 2.7版本：sudo pip install --upgrade pip
python 3.x版本：sudo pip3 install --upgrade pip
```

四、更改pip源地址（提高下载速度）

```
修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件，文件夹要加"."，表示是隐藏文件夹)，内容如下：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com

```

五、安装TensorFlow

```
TensorFlow可以安装CPU和GPU两种版本，CPU版本安装命令如下：
python 2.7版本：sudo pip install tensorflow
python 3.x版本：sudo pip3 install tensorflow

GPU版本安装命令如下：
python 2.7版本：sudo pip install tensorflow-gpu
python 3.x版本：sudo pip3 install tensorflow-gpu

```

六、测试安装结果

```
yht@yht-vm:~/.pip$ python
Python 2.7.15rc1 (default, Apr 15 2018, 21:51:34) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> session = tf.Session()
2018-11-27 18:18:03.448263: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
>>> a = tf.constant(111)
>>> b = tf.constant(222)
>>> print(session.run(a+b))
333

```














