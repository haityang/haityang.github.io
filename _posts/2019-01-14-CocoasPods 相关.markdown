1.改变gem 镜像

```
gem -v
gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org/
gem sources -l

```


2.更新pod源

```
pod repo update
```

3.查看当前版本

```
pod --version

```


4.更新到某一版本

```
sudo gem install cocoapods -v 1.6.0

```

5.更新到最新版本

```
sudo gem install cocoapods


```


6.删除当前版本

```
sudo gem uninstall cocoapods

```


7.issue

```
Include of non-modular header inside framework module ...

Build Setting — Apple LLVM 8.1 Language Modules — Allow Non-modular Includes In Framework Modules
设置为YES，则可以在Framework中使用模块外的Include，不过这种过于粗暴

```
8.更新到最新

```
sudo gem update cocoapods --pre
pod update
clean
build

```

9 . does not specify a Swift version 

```
In this case bridging header must be created.
1.Open the project with XCode. Then choose File -> New -> File -> Swift File.
A dialog will be displayed when creating the swift file(Since this file is deleted, any name can be used.). XCode will ask you if you wish to create Bridging Header, click yes.
2.Make sure you have use_frameworks! in the Runner block, in ios/Podfile。
3. Make sure you have SWIFT_VERSION 4.2 selected in you XCode -> Build Settings
4.Do flutter clean
5. Go to your ios folder, delete Podfile.lock and Pods folder and then execute pod install --repo-update

this works!!! thank you very much
```

10 . Disable bitcode for project and cocoapods dependencies

```
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['ENABLE_BITCODE'] = 'NO'
    end
  end
end

```

11.最简单的podfile

```
platform :ios, '9.0'
target 'dd' do 
    pod 'Reachability'
end

```

12.换电脑更新 cocoapod

```
//重新安装pod
sudo gem uninstall cocoapods
sudo gem install cocoapods
pod cache clean --all
//重新生成当前项目
pod deintegrate
pod install

```

Podfile 中的一些关键字


在 Xcode 9 之前，不支持 Swift 静态库编译，因此 Swift pod 不得不使用动态库编译，即使用 use_frameworks!。但是，引用了大量动态库会导致应用程序启动时间变长。

如果一个 Swift pod 依赖了一个 OC pod，那么我们要为对应的 OC pod 开启 modular headers（use_modular_headers! 就会开启 modular headers）。开启 modular headers 的本质就是将 pod 转换为 Modular（也就是支持模块），而 Modular 是可以直接在 Swift 中 import 的，不需要再经过 bridging-header 进行桥接，从而简化了 Swift 引用 OC 的方式。

```
use_frameworks!
use_modular_headers!

```