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
