
#### CocoaPods 镜像使用帮助
```
source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'
```

#### 访问权限
```
Privacy - Microphone Usage Description //麦克风权限
Privacy - Contacts Usage Description   //通讯录权限
Privacy - Camera Usage Description     //摄像头权限
Privacy - NSSiriUsageDescription       //Siri的权限
Privacy - Bluetooth Peripheral Usage Description //蓝牙
Privacy - Reminders Usage Description  //提醒事项
Privacy - Motion Usage Description     //运动与健康
Privacy - Media Libaray Usage Description //媒体资源库
Privacy - Calendars Usage Description  //日历
Privacy - Photo Library Usage Description //相册
Privacy - Location Always Usage Description //始终访问位置
Privacy - Location Usage Description 位置
Privacy - Location When In Use Usage Description 在使用期间访问位置
Privacy - Health Share Usage Description //访问健康分享
Privacy - Health Update Usage Description //访问健康更新
Privacy - Motion Usage Description//访问运动与健身
Privacy - Reminders Usage Description //访问提醒事项
```


#### 环境变量：
```
$(BUILT_PRODUCTS_DIR)
build成功后的，最终产品路径－－可以在Build Settings参数的Per-configuration Build Products Path项里设置

$(TARGET_NAME)
目标工程名称

$(SRCROOT)
工程文件（比如Nuno.xcodeproj）的路径

$(CURRENT_PROJECT_VERSION)
当前工程版本号
```


#### OpenGL
```
1.GLEW
2.GLM 

Installing: /usr/local/include/GLFW
Installing: /usr/local/include/GLFW/glfw3.h
Installing: /usr/local/include/GLFW/glfw3native.h
Installing: /usr/local/lib/libglfw3.a
Installing: /usr/local/include/glm

/usr/local/lib/cmake/glfw3
/usr/local/lib/cmake/glm


VBO，全称Vertex Buffer Object
FBO，全名Frame Buffer Object
```

#### 安装apk
```
~/Library/Android/sdk/platform-tools/adb install /Users/yanghaitao/Downloads/app-debug-v1.0.0.14.apk
```

#### 得到Document目录
```
NSHomeDirectory();
NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES);
STemporaryDirectory();
```

### 重新安装cocospods:
```
sudo chown $(whoami):admin /usr/local/opt

brew link --overwrite cocoapods

cocoapods换源：
pod repo
git clone https://git.coding.net/CocoaPods/Specs.git ~/.cocoapods/repos/master
pod repo update
```

#### iOS 代码目录 
```
https://developer.apple.com/library/content/navigation/
https://developer.apple.com/library/content/navigation/
```
#### 非常简单的Python HTTP服务
```
SimpleHTTPServer python内置，支持下载功能 
$ cd /home/haoel
$ python -m SimpleHTTPServer
http://192.168.1.1:8000
$ python -m SimpleHTTPServer 8080
```

#### Droopy 支持文件上传
```
pip install -i http://pypi.douban.com/simple droopy

```
-----------------
文件压缩 

```

 *.Z        compress程序压缩的文件（最早期使用）,压缩后取代源文件；
 
 *.zip      一个夸平台的文件打包程序，适用于Linux、windows和Mac OS系统；
 
 *.bz2      bzip2程序压缩的文件；
 
 *.gz       gzip程序压缩的文件；
 
 *.tar      tar程序打包的文件，并没有压缩；
 
 *.tar.gz   tar程序打包的文件，并经过gzip程序的压缩；
 
 *.tar.bz2  tar程序打包的文件，并经过bzip2程序压缩。
 
1.  tar -cvf   test.tar   test                ### 仅打包，不压缩
2.	tar -zcvf  test.tar.gz    test        ### 打包后以gzip压缩
3.	tar -jcvf  test.tar.bz2   test        ### 打包后以bzip2压缩

如何解压缩包：
1.	tar -xvf   test.tar
2.	tar -xvf   test.tar.gz
3.	tar  -jxvf  test.tar.bz2
4.	tar  -jxvf  test.tar.bz2  -C  /var/tmp/find     解压到其他目录
```

