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

11. 最简单的podfile

```
platform :ios, '9.0'
target 'dd' do 
    pod 'Reachability'
end

```
