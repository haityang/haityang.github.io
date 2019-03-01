
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

#### 1. 从xib中加载cell
```
@property (strong, nonatomic) UINib *countryCellNib;
- (UINib *)countryCellNib
{
  if (!_countryCellNib)
  {
    _countryCellNib = [UINib nibWithNibName:@"CountryCell" bundle:nil];
  }
  return _countryCellNib;
}

- (UITableViewCell *)tableView:(UITableView *)tableView
         cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
  UITableViewCell *cell = [tableView
            dequeueReusableCellWithIdentifier:UYLCountryCellIdentifier];

  if (cell == nil)
  {
    [self.countryCellNib instantiateWithOwner:self options:nil];
    cell = self.countryCell;
    self.countryCell = nil;
  }

  // Code omitted to configure the cell...

  return cell;
}
```

#### 2.只要注册了以后就无需实例化。表视图cell nib的用法
```
- (void)viewDidLoad
{
  UINib *countryNib = [UINib nibWithNibName:@"CountryCell" bundle:nil];
  [self.tableView registerNib:countryNib
                  forCellReuseIdentifier:UYLCountryCellIdentifier];
}

- (UITableViewCell *)tableView:(UITableView *)tableView
         cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
  UITableViewCell *cell = [tableView
            dequeueReusableCellWithIdentifier:UYLCountryCellIdentifier];
  return cell;
}
```

#### 3.使用UINib的方式
```
NSArray *topLevelObjects = [_bigAppNib instantiateWithOwner:self options:nil];
bigAppCell = [topLevelObjects objectAtIndex:0];

-----------------

static NSString* kMMBigAppCellID = @"MMAppBigCellIdentifier";
UINib *bigAppNib = [UINib nibWithNibName:@"MMAppBigCell" bundle:nil];
[self.collectionView registerNib:bigAppNib forCellWithReuseIdentifier:kMMBigAppCellID];
    
MMAppBigCell * cell = [cv dequeueReusableCellWithReuseIdentifier:kMMBigAppCellID forIndexPath:indexPath];
```

#### 4.不用注册的方式，的cell nib用法
```
cell = [tableView dequeueReusableCellWithIdentifier:@"ReminderCell"];
if (cell == nil) {
	NSArray *topLevelObjects = [[NSBundle mainBundle] loadNibNamed:@"ReminderCell" owner:self options:nil];
	cell = [topLevelObjects objectAtIndex:0];
	
	ReminderCell *reminderCell = (ReminderCell *)cell;
	reminderCell.rkCellDelegate = self;
	[reminderCell initUI];
}
return cell;
```

#### 5.UIViewController nib文件用法
```
CommonGoodsListController *cvc = nil;
cvc = [[[GoodsListModel03 alloc] initWithNibName:@"GoodsListModel03" bundle:nil] autorelease];
```

#### 6.加载 uiview nib的方法
```
-(void)awakeFromNib {
    NSArray *obj = [[NSBundle mainBundle] loadNibNamed:@"MyView" owner:self options:nil];
    [self addSubview:obj[0]];
}
```

#### 7.加载 uiview nib的方法
```
JJGWebView *webViewToPush = [[JJGWebView alloc] initWithNibName:@"JJGWebView" bundle:nil];
```

-------------------------------------
#### 8.对于原型cell,可以用以下方法(在storyboard中构建了的cell nib，不需要注册，也不需要实例化)
```
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"PlayerCell"];
 
    Player *player = (self.players)[indexPath.row];
    cell.textLabel.text = player.name;
    cell.detailTextLabel.text = player.game;
 
    return cell;
}
```

#### 9.对于collection header and footer
```
- (UICollectionReusableView *)collectionView:(UICollectionView *)collectionView viewForSupplementaryElementOfKind:(NSString *)kind atIndexPath:(NSIndexPath *)indexPath
{
    UICollectionReusableView *reusableview = nil;
    
    if (kind == UICollectionElementKindSectionHeader) {
        reusableview = [collectionView dequeueReusableSupplementaryViewOfKind:UICollectionElementKindSectionHeader withReuseIdentifier:@"HeaderView" forIndexPath:indexPath];
    }
 
    if (kind == UICollectionElementKindSectionFooter) {
        reusableview = [collectionView dequeueReusableSupplementaryViewOfKind:UICollectionElementKindSectionFooter withReuseIdentifier:@"FooterView" forIndexPath:indexPath];
    }
        
    return reusableview;
}        
```
     

#### 10. 对于没有Segue连接的，（在storyboard中的UIViewController）
```
UIViewController *vc = nil;
vc = [self.storyboard instantiateViewControllerWithIdentifier:@"MMRecommendVC"];
```


#### 11. 对于有Segue连接的push viewcontroller方法
```
[self performSegueWithIdentifier:@"MMSearchVCSegue" sender:self];
```

#### CocoaPods 镜像使用帮助
新版的 CocoaPods 不允许用pod repo add直接添加master库了，但是依然可以：

```
$ cd ~/.cocoapods/repos 
$ pod repo remove master
$ git clone https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git master
```

最后进入自己的工程，在自己工程的podFile第一行加上：

```
source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'
```

画一个PDF 页面

```
CFURLRef pdfURL = CFBundleCopyResourceURL(CFBundleGetMainBundle(), 
    (__bridge CFStringRef)self.fileName, NULL, NULL);
CGPDFDocumentRef pdfDocument = 
    CGPDFDocumentCreateWithURL((CFURLRef)pdfURL);
CFRelease(pdfURL);
CGContextTranslateCTM(context, 0.0, self.bounds.size.height);
CGContextScaleCTM(context, 1.0, -1.0);
CGPDFPageRef page = CGPDFDocumentGetPage(pdfDocument, self.pageNumber);
CGContextSaveGState(context);
CGAffineTransform pdfTransform = CGPDFPageGetDrawingTransform(page, 
    kCGPDFCropBox, self.bounds, 0, true);
CGContextConcatCTM(context, pdfTransform);
CGContextDrawPDFPage(context, page);
CGContextRestoreGState(context);

```


