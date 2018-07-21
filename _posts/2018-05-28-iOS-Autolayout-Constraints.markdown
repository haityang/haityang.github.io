
--------------
# 自动约束 
`button.translatesAutoresizingMaskIntoConstraints = NO;`

## 上边距
```
constraint = [NSLayoutConstraint
              constraintWithItem:button
              attribute:NSLayoutAttributeTop
              relatedBy:NSLayoutRelationEqual
              toItem:self.view
              attribute:NSLayoutAttributeTop
              multiplier:1.0f
              constant:50.0f];
[self.view addConstraint:constraint];
```

## 左边距
```
constraint = [NSLayoutConstraint
              constraintWithItem:button
              attribute:NSLayoutAttributeLeading
              relatedBy:NSLayoutRelationEqual
              toItem:self.view
              attribute:NSLayoutAttributeLeading
              multiplier:1.0f
              constant:100.0f];
[self.view addConstraint:constraint];
```

## 右边距
```
constraint = [NSLayoutConstraint
              constraintWithItem:button
              attribute:NSLayoutAttributeTrailing
              relatedBy:NSLayoutRelationEqual
              toItem:self.view
              attribute:NSLayoutAttributeTrailing
              multiplier:1.0f
              constant:-100.0f];
[self.view addConstraint:constraint];
```

## 下边距
```
constraint = [NSLayoutConstraint
              constraintWithItem:button
              attribute:NSLayoutAttributeBottom
              relatedBy:NSLayoutRelationEqual
              toItem:self.view
              attribute:NSLayoutAttributeBottom
              multiplier:1.0f
              constant:-350.0f];
[self.view addConstraint:constraint];
```

## 水平居中
```
constraint = [NSLayoutConstraint
              constraintWithItem:button
              attribute:NSLayoutAttributeCenterX
              relatedBy:NSLayoutRelationEqual
              toItem:self.view
              attribute:NSLayoutAttributeCenterX
              multiplier:1.0f
              constant:0.0f];
[self.view addConstraint:constraint];
```

# 垂直居中
```
constraint = [NSLayoutConstraint
              constraintWithItem:button
              attribute:NSLayoutAttributeCenterY
              relatedBy:NSLayoutRelationEqual
              toItem:self.view
              attribute:NSLayoutAttributeCenterY
              multiplier:1.0f
              constant:0.0f];
[self.view addConstraint:constraint];
```

## 设置宽度
```
constraint = [NSLayoutConstraint constraintWithItem:button attribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:nil attribute:NSLayoutAttributeNotAnAttribute multiplier:1.0f constant:130.0f];
[self.view addConstraint:constraint];
```

## 设置高度
```
constraint = [NSLayoutConstraint constraintWithItem:button attribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:nil attribute:NSLayoutAttributeNotAnAttribute multiplier:1.0f constant:70.0f];
[self.view addConstraint:constraint];
```

## 水平方向布局(从左向右)
```
[array addObjectsFromArray:[NSLayoutConstraint
                            constraintsWithVisualFormat:@"|-60-[buttonA(==90)]-30-[buttonB]"
                            options:NSLayoutFormatDirectionLeadingToTrailing
                            metrics:nil
                            views:NSDictionaryOfVariableBindings(buttonA,buttonB)]];                   
```

## 垂直方向布局(从上向下)
```
[array addObjectsFromArray:[NSLayoutConstraint
                            constraintsWithVisualFormat:@"V:|-100-[buttonB]-50-[buttonA]"
                            options:NSLayoutFormatDirectionLeadingToTrailing
                            metrics:nil
                            views:NSDictionaryOfVariableBindings(buttonA,buttonB)]];

[self.view addConstraints:array];
```

---------
## VFL
```
NSDictionary *viewsDictionary = NSDictionaryOfVariableBindings(buttonA,buttonB);
@"|-50-[buttonA(80@100)]-[buttonB(90@200)]-50-|" //左右边距都为50，中间有两个按钮，相隔缺省宽度，一个控件宽度为80，约束优先级为100；另一个控件宽度为90，约束优先级为200
@"V:[buttonA(80)]-20-[buttonB(==buttonA)]" //垂直方向有一个高度为80的buttonA，然后间隔20有一个和buttonA同样高度的buttonB
```
#### apple VFL
```
Standard Space
[button]-[textField]

Width Constraint
[button(>=50)]

Connection to Superview
|-50-[purpleBox]-50-|

Vertical Layout
V:[topField]-10-[bottomField]

Flush Views
[maroonView][blueView]

Priority
[button(100@20)]

Equal Widths
[button1(==button2)]

Multiple Predicates
[flexibleButton(>=70,<=100)]

A Complete Line of Layout
|-[find]-[findNext]-[findField(>=20)]-|

```

### 垂直居中
```
[self.view addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"V:|-[prgrssView]-|" options:NSLayoutFormatAlignAllCenterY metrics:nil views:views]];  
```

### Masonary
```
//.分别设置各个相对边距（superview为view的父类视图，下同）
make.left.mas_equalTo(superView.mas_left).mas_offset(10);
make.right.mas_equalTo(superView.mas_right).mas_offset(-10);
make.top.mas_equalTo(superView.mas_top).mas_offset(10);
make.bottom.mas_equalTo(superView.mas_bottom).offset(-10);
```

```
//直接连接使用left大于等于每个值
make.left.mas_greaterThanOrEqualTo(10);
```

```
//设置宽和高
make.width.mas_equalTo(60);
make.height.mas_equalTo(60);
```

```
//.设置center和款高比
make.center.mas_equalTo(superView);
make.width.mas_equalTo(superView).multipliedBy(1.00/3);
make.height.mas_equalTo(superView).multipliedBy(0.25);
```

```
//.关于约束优先级,此处要注意约束冲突的问题，统一约束优先级大的生效
make.left.mas_equalTo(100);
make.left.mas_equalTo(view.superview.mas_left).offset(10);
make.left.mas_equalTo(20).priority(700);
make.left.mas_equalTo(40).priorityHigh();
make.left.mas_equalTo(60).priorityMedium();
make.left.mas_equalTo(80).priorityLow();
```

```
//.如果你想让view的（x坐标）左边大于等于label的左边，以下两个约束的写法效果一样
 make.left.greaterThanOrEqualTo(label);
 make.left.greaterThanOrEqualTo(label.mas_left);
```

```
make.width.greaterThanOrEqualTo(@200);
make.width.lessThanOrEqualTo(@400)
```

```
make.top.mas_equalTo(42);
make.height.mas_equalTo(20);
make.size.mas_equalTo(CGSizeMake(50, 100));
make.edges.mas_equalTo(UIEdgeInsetsMake(10, 0, 10, 0));
make.left.mas_equalTo(view).mas_offset(UIEdgeInsetsMake(10, 0, 10, 0));
```

```
make.height.equalTo(@[view1.mas_height, view2.mas_height]);
make.height.equalTo(@[view1, view2]);
make.left.equalTo(@[view1, @100, view3.right]);
```

```
make.left.greaterThanOrEqualTo(label.mas_left).with.priorityLow();
make.top.equalTo(label.mas_top).with.priority(600);
```

```
edges
// 使一个view的top, left, bottom, right 等于view2的
make.edges.equalTo(view2)；

//相对于superviewde上左下右边距分别为5，10，15，20
make.edges.equalTo(superview).insets(UIEdgeInsetsMake(5, 10, 15, 20))
```


```
size
// 使得宽度和高度大于等于 titleLabel
make.size.greaterThanOrEqualTo(titleLabel)

// 相对于superview宽度大100，高度小50
make.size.equalTo(superview).sizeOffset(CGSizeMake(100, -50))
```


```
center
//中心与button1对齐
make.center.equalTo(button1)

//水平方向中心相对向左偏移5，竖直方向中心向下偏移10
make.center.equalTo(superview).centerOffset(CGPointMake(-5, 10))
```

### 你可以在约束链里添加相应的view来增加代码的可读性:
```
// 除了top，所有的边界与superview对齐
make.left.right.and.bottom.equalTo(superview);
make.top.equalTo(otherView);
```

```
@property (nonatomic, strong) MASConstraint *topConstraint;

...

// 添加约束
[view1 mas_makeConstraints:^(MASConstraintMaker *make) {
self.topConstraint = make.top.equalTo(superview.mas_top).with.offset(padding.top);
make.left.equalTo(superview.mas_left).with.offset(padding.left);
}];

...

// 然后可以调用
//该约束移除
[self.topConstraint uninstall];
//重新设置value,最常用
self.topConstraint.mas_equalTo(20);
//该约束失效
[self.topConstraint deactivate];
//该约束生效
[self.topConstraint activate];
```


```
- (void)updateConstraints {

[self.growingButton mas_updateConstraints:^(MASConstraintMaker *make) {
make.center.equalTo(self);
make.width.equalTo(@(self.buttonSize.width)).priorityLow();
make.height.equalTo(@(self.buttonSize.height)).priorityLow();
make.width.lessThanOrEqualTo(self);
make.height.lessThanOrEqualTo(self);
}];

//调用super
[super updateConstraints];
}
```

```
- (void)changeButtonPosition {
      [self.button mas_remakeConstraints:^(MASConstraintMaker *make) {
      make.size.equalTo(self.buttonSize);
     if (topLeft) {
          make.top.and.left.offset(10);
     } else {
     make.bottom.and.right.offset(-10); 
   }
  }];
```
  

```
        //添加动画
        [UIView animateWithDuration:0.5 animations:^{
            
            [bself.view5 mas_updateConstraints:^(MASConstraintMaker *make) {
                //更改距顶上的高度
                make.top.equalTo(bself.view).with.offset(300);
            }];
            //必须调用此方法，才能出动画效果
           [bself.view5 layoutIfNeeded];
        }];
```

* Masonry设置长宽比

```
    [aview makeConstraints:^(MASConstraintMaker *make) {
        make.left.mas_equalTo(self.view);
        make.bottom.mas_equalTo(self.view);
        make.right.mas_equalTo(WeSelf.InputYuYinbtn.left);
        make.height.mas_equalTo(aview.width).multipliedBy(0.6);// 高/宽 == 0.6
    }];
```

-------------------------------
怎么Debug constrains?

```

2016-01-06 14:54:25.979 CTRIP_WIRELESS[37253:377433] Unable to simultaneously satisfy constraints.
	Probably at least one of the constraints in the following list is one you don't want. 
	Try this: 
		(1) look at each constraint and try to figure out which you don't expect; 
		(2) find the code that added the unwanted constraint or constraints and fix it. 
(
    "<NSLayoutConstraint:0x7fe43c8834f0 UILabel:0x7fe43c882600.top == UITableViewCellContentView:0x7fe43c881650.top + 10>",
    "<NSLayoutConstraint:0x7fe43c883590 UITableViewCellContentView:0x7fe43c881650.bottom == UILabel:0x7fe43c882600.bottom + 10>",
    "<NSLayoutConstraint:0x7fe43c2d2d00 UITableViewCellContentView:0x7fe43c881650.height == 0>"
)

Will attempt to recover by breaking constraint 
<NSLayoutConstraint:0x7fe43c883590 UITableViewCellContentView:0x7fe43c881650.bottom == UILabel:0x7fe43c882600.bottom + 10>

Make a symbolic breakpoint at UIViewAlertForUnsatisfiableConstraints to catch this in the debugger.
The methods in the UIConstraintBasedLayoutDebugging category on UIView listed in <UIKit/UIView.h> may also be helpful.


```


```

1.加一个符号断点：UIViewAlertForUnsatisfiableConstraints
2.可以输出constrains看看
(lldb) po 0x7fe43c883590
<NSLayoutConstraint:0x7fe43c883590 UITableViewCellContentView:0x7fe43c881650.bottom == UILabel:0x7fe43c882600.bottom + 10>
3.也可以输出出问题的视图看看
(lldb) po 0x7fe43c881650
<UITableViewCellContentView: 0x7fe43c881650; frame = (0 0; 375 0); opaque = NO; gestureRecognizers = <NSArray: 0x7fe43c884280>; layer = <CALayer: 0x7fe43c8817d0>>
4.也可以输出出问题的子视图看看
(lldb) po 0x7fe43c882600
<UILabel: 0x7fe43c882600; frame = (20 10; 285 24); text = '内容内容内容内容内容内容内容内容内容内容内容内容内...'; opaque = NO; autoresize = RM+BM; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x7fe43c882810>>
5.也可以输出所有子视图看看：
(lldb) po [0x7fe43c881650 recursiveDescription]
<UITableViewCellContentView: 0x7fe43c881650; frame = (0 0; 375 0); opaque = NO; gestureRecognizers = <NSArray: 0x7fe43c884280>; layer = <CALayer: 0x7fe43c8817d0>>
   | <UIImageView: 0x7fe43c8817f0; frame = (8 -1; 304 45); hidden = YES; autoresize = RM+BM; userInteractionEnabled = NO; layer = <CALayer: 0x7fe43c8819a0>>
   | <UIImageView: 0x7fe43c881d80; frame = (8 -1; 304 43); autoresize = RM+BM; userInteractionEnabled = NO; layer = <CALayer: 0x7fe43c881c60>>
   | <CTDashLineView: 0x7fe43c8822a0; frame = (8 0; 304 1); clipsToBounds = YES; autoresize = RM+BM; layer = <CALayer: 0x7fe43c8821c0>>
   | <UIButton: 0x7fe43c880a90; frame = (276 0; 44 44); hidden = YES; opaque = NO; autoresize = RM+BM; layer = <CALayer: 0x7fe43c880d30>>
   |    | <UIImageView: 0x7fe43c2d0be0; frame = (15 15; 14 14); clipsToBounds = YES; opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x7fe43c2d0900>>
   | <UILabel: 0x7fe43c882600; frame = (20 10; 285 24); text = '内容内容内容内容内容内容内容内容内容内容内容内容内...'; opaque = NO; autoresize = RM+BM; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x7fe43c882810>>
6.也可以输出父视图的所有子视图看看：
(lldb) po [[0x7fe43c881650 superview] recursiveDescription]
<CTInternationalFlightsStudentsCell: 0x7fe45489a000; baseClass = UITableViewCell; frame = (0 209; 375 0); clipsToBounds = YES; autoresize = W; layer = <CALayer: 0x7fe43c881630>>
   | <UITableViewCellContentView: 0x7fe43c881650; frame = (0 0; 375 0); opaque = NO; gestureRecognizers = <NSArray: 0x7fe43c884280>; layer = <CALayer: 0x7fe43c8817d0>>
   |    | <UIImageView: 0x7fe43c8817f0; frame = (8 -1; 304 45); hidden = YES; autoresize = RM+BM; userInteractionEnabled = NO; layer = <CALayer: 0x7fe43c8819a0>>
   |    | <UIImageView: 0x7fe43c881d80; frame = (8 -1; 304 43); autoresize = RM+BM; userInteractionEnabled = NO; layer = <CALayer: 0x7fe43c881c60>>
   |    | <CTDashLineView: 0x7fe43c8822a0; frame = (8 0; 304 1); clipsToBounds = YES; autoresize = RM+BM; layer = <CALayer: 0x7fe43c8821c0>>
   |    | <UIButton: 0x7fe43c880a90; frame = (276 0; 44 44); hidden = YES; opaque = NO; autoresize = RM+BM; layer = <CALayer: 0x7fe43c880d30>>
   |    |    | <UIImageView: 0x7fe43c2d0be0; frame = (15 15; 14 14); clipsToBounds = YES; opaque = NO; userInteractionEnabled = NO; layer = <CALayer: 0x7fe43c2d0900>>
   |    | <UILabel: 0x7fe43c882600; frame = (20 10; 285 24); text = '内容内容内容内容内容内容内容内容内容内容内容内容内...'; opaque = NO; autoresize = RM+BM; userInteractionEnabled = NO; layer = <_UILabelLayer: 0x7fe43c882810>>
   | <_UITableViewCellSeparatorView: 0x7fe43c883980; frame = (15 43; 305 1); layer = <CALayer: 0x7fe43c883810>>
这样就基本可以定位了。
源文链接：http://staxmanade.com/2015/06/debugging-ios-autolayout-issues/
      
```

--------------------------------