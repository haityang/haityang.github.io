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
sudo gem install cocoapods -v 1.5.3

```

5.更新到最新版本

```
sudo gem install cocoapods


```


6.删除当前版本

```
sudo gem uninstall cocoapods

```
