1.创建自定义configuration的作用

1).影响到的功能 configuration -->

	* Build Active Architecture Only
	* Code Signing Identity
	* Preprocessor Macros
	* Asset Catalog Compiler
	* User-Defined

      


2).根据不同的宏编译不同的URL

```
#ifdef DEVELOP
#define kSearchHost @"http://www.baidu.com"
#elif BAOLEI
#define kSearchHost @"http://www.bing.com"
#else
#define kSearchHost @"http://www.google.com"
#endif
```


3.具体步骤：

1). 创建一个新的configuration：Duplicate "Release" Configuration， 命名为Adhoc

2). 创建3个 .xcconfig 文件。都不勾选。命名为Adhoc.xcconfig，Debug.xcconfig
，Release.xcconfig


3). 在configurations部分的Adhoc 选择 Adhoc.xcconfig

4). 编辑.xcconfig.

Adhoc.xcconfig

```
//App
TEST_APP_BUNDLE_ID = net.
TEST_APP_BUNDLE_NAME = AdhocApp

TEST_CODE_SIGN_ENTITLEMENTS = TestConfig.entitlements

TEST_CODE_SIGN_IDENTITY = iPhone Distribution: Beijing google Co.,Ltd. (33DD2HGF3H)
TEST_CODE_SIGN_IDENTITY[sdk=iphoneos*] = iPhone Distribution: Beijing google Co.,Ltd. (33DD2HGF3H)
TEST_DEVELOPMENT_TEAM = 33DD2HGF3H
TEST_CODE_SIGN_STYLE = Manual

TEST_PROVISIONING_PROFILE_SPECIFIER = TestConfig_adhoc

//notification extension
TEST_APP_NOTIF_BUNDLE_ID = net.google.TestConfig.serviceExtension

TEST_NOTIF_CODE_SIGN_IDENTITY = iPhone Distribution: Beijing google Co.,Ltd. (33DD2HGF3H)
TEST_NOTIF_CODE_SIGN_IDENTITY[sdk=iphoneos*] = iPhone Distribution: Beijing google Co.,Ltd. (33DD2HGF3H)
TEST_NOTIF_DEVELOPMENT_TEAM = 33DD2HGF3H
TEST_NOTIF_CODE_SIGN_STYLE = Manual

TEST_NOTIF_PROVISIONING_PROFILE_SPECIFIER = TestConfig.serviceExten_adhoc
TEST_NOTIF_PROVISIONING_PROFILE = 23dd72f4-55oo-8322-89ww-02310a444636

//xcodebuild -scheme TestConfig archive -archivePath ~/Desktop/a.xcarchive -configuration Adhoc
//xcodebuild -exportArchive  -archivePath ~/Desktop/a.xcarchive -exportPath ~/Desktop/a -exportOptionsPlist AutoPackage/ad_hoc/AdHocExportOptions.plist 

```


Debug.xcconfig

```
TEST_APP_BUNDLE_ID = com.google.TestConfig
TEST_APP_BUNDLE_NAME = DebugApp

TEST_CODE_SIGN_ENTITLEMENTS = TestConfig.entitlements

TEST_CODE_SIGN_IDENTITY = iPhone Developer
TEST_CODE_SIGN_IDENTITY[sdk=iphoneos*] = iPhone Developer: oooOOO (8WUH82T4EF)
TEST_DEVELOPMENT_TEAM = 445HW1G3DD
TEST_CODE_SIGN_STYLE = Manual

TEST_PROVISIONING_PROFILE_SPECIFIER = OOO_prol_ee


//notification extension
TEST_NOTIF_BUNDLE_ID = com.google.TestConfig.serviceExtension

TEST_NOTIF_CODE_SIGN_IDENTITY = iPhone Developer: oooOOO (8WUH82T4EF)
TEST_NOTIF_CODE_SIGN_IDENTITY[sdk=iphoneos*] = iPhone Developer: oooOOO (8WUH82T4EF)
TEST_NOTIF_DEVELOPMENT_TEAM = 445HW1G3DD
TEST_NOTIF_CODE_SIGN_STYLE = Manual

TEST_NOTIF_PROVISIONING_PROFILE_SPECIFIER = Development_ serviceExtens
TEST_NOTIF_PROVISIONING_PROFILE = 23dd72f4-55oo-8322-89ww-02310a444636
```

Release.xcconfig

```
//App
TEST_APP_BUNDLE_ID = net.google.TestConfig
TEST_APP_BUNDLE_NAME = ReleaseApp

TEST_CODE_SIGN_ENTITLEMENTS = TestConfig.entitlements 

TEST_CODE_SIGN_IDENTITY = iPhone Distribution: Beijing google Co.,Ltd. (33DD2HGF3H)
TEST_CODE_SIGN_IDENTITY[sdk=iphoneos*] = iPhone Distribution: Beijing google Co.,Ltd. (33DD2HGF3H)
TEST_DEVELOPMENT_TEAM = 33DD2HGF3H
TEST_CODE_SIGN_STYLE = Manual

TEST_PROVISIONING_PROFILE_SPECIFIER = TestConfig_distr
TEST_PROVISIONING_PROFILE = 0dff72f6-80gg-4155-94ff-02310d436000


//notification extension
TEST_APP_NOTIF_BUNDLE_ID = net.google.TestConfig.superappNotificationServiceExtension

TEST_NOTIF_CODE_SIGN_IDENTITY = iPhone Distribution: Beijing google Co.,Ltd. (33DD2HGF3H)
TEST_NOTIF_CODE_SIGN_IDENTITY[sdk=iphoneos*] = iPhone Distribution: Beijing google Co.,Ltd. (33DD2HGF3H)
TEST_NOTIF_DEVELOPMENT_TEAM = 33DD2HGF3H
TEST_NOTIF_CODE_SIGN_STYLE = Manual

TEST_NOTIF_PROVISIONING_PROFILE_SPECIFIER = Development_ ServiceExtens
TEST_NOTIF_PROVISIONING_PROFILE = 0dff72f6-80gg-4155-94ff-02310d436000

```



5). 修改build setting 中相应的变量，设置其值为比如 ${TEST\_APP\_BUNDLE\_ID}







