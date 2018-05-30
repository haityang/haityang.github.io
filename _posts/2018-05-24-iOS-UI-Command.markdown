
####1.CocoaPods 镜像使用帮助
```
source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'
```

####2.访问权限
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


####环境变量：
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

-----------------
####OpenGL
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

####安装apk
```
~/Library/Android/sdk/platform-tools/adb install /Users/yanghaitao/Downloads/app-debug-v1.0.0.14.apk
```

####得到Document目录
```
NSHomeDirectory();
NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES);
STemporaryDirectory();
```

重新安装cocospods:
-----------
```
sudo chown $(whoami):admin /usr/local/opt

brew link --overwrite cocoapods

cocoapods换源：
pod repo
git clone https://git.coding.net/CocoaPods/Specs.git ~/.cocoapods/repos/master
pod repo update
```

####iOS 代码目录 
```
https://developer.apple.com/library/content/navigation/
https://developer.apple.com/library/content/navigation/
```



