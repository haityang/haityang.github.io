### 1. find查找:

```
find / -name httpd.conf  
find /etc -name '*srm*'  
find / -amin -10 #查找在系统中最后10分钟访问的文件  
find / -atime -2 #查找在系统中最后48小时访问的文件  
find / -empty #查找在系统中为空的文件或者文件夹  
find / -group cat #查找在系统中属于groupcat的文件  
find / -mmin -5 #查找在系统中最后5分钟里修改过的文件  
find / -mtime -1 #查找在系统中最后24小时里修改过的文件  
find / -nouser #查找在系统中属于作废用户的文件  
find / -user fred #查找在系统中属于FRED这个用户的文件  
```


### 2.计算代码行数:

```
wc -c a.txt   //计算字符数
wc -l a.txt    //   20628 total
```


### 3.awk数值计算

```
echo | awk '{print 19+7}'

```


### 4.批量改名，删除

```
1.批量改名. 把-hd.*的文件批量改名为-ipd.*
ls -l *-hd.*|awk '{m=$9; gsub(/-hd./,"-ipd.",$9);print "mv "m " "$9}'|sh

2.批量删除。 把不包含-hd.的文件都删除掉
find . ! -name "*-hd.*" -exec rm -f {} \;


ls -l *.jpg|awk '{m=$9; gsub(/.jpg/,"-ipd.jpg",$9);print "mv "m " "$9}'|sh

3.删除某行，包含字符串
sed '/ABCD/d' file1 >file2

```

###  5.文本分析几大工具

```
tail -n 3 jan2017articles.csv
head -n 1 jan2017articles.csv
wc -l jan2017articles.csv
grep -i "security" jan2017articles.csv
grep -i "security" jan2017articles.csv | wc -l
grep "20 Jan 2017" jan2017articles.csv | tr ',' '\t' > jan20only.tsv
sort -nr -t$'\t' -k8 jan20only.tsv | head -n 1
sed '1 d' jan2017articles.csv > jan17no_headers.csv
sort authors.txt | uniq -c > authors-sorted.txt
awk -F "\t" '{print $3 "  " $NF}' jan20only.tsv
grep "authentication failure" /var/log/auth.log | cut -d '=' -f 8


```

### 6.shell练习

```
$ file /bin/ls //文件信息
$ alias c='cal;date' //别名
$ type c
$ echo $0 //登录的shell
$ 	test -r ~/.bashrc && . ~/.bashrc //If .bashrc exists and is readable (test ...), then (&&) the .bashrc file will be processed

$ cat script.sh 
echo Hello World 
$ bash script.sh 
Hello World
$ chmod u+x script.sh
$ ./script.sh
$ set  //查看环境变量


```

-------------------------------
### 7. cut的用法：

```
主要参数
-b ：以字节为单位进行分割。这些字节位置将忽略多字节字符边界，除非也指定了 -n 标志。
-c ：以字符为单位进行分割。
-d ：自定义分隔符，默认为制表符。
-f  ：与-d一起使用，指定显示哪个区域。
-n ：取消分割多字节字符。仅和 -b 标志一起使用。如果字符的最后一个字节落在由 -b 标志的 List 参数指示的<br />范围之内，该字符将被写出；否则，该字符将被排除。

cat test.txt |cut -b 1-5	//以字节截取
cat test.txt | cut -c 1-5   //以字符截取
cat /etc/passwd|head -n 5|cut -d : -f 1,3-5 //以:分隔，取1，3，4，5列
cat test.txt |cut -f 3-4,5  //以tab分隔，取3，4，5列
cat test.txt |cut -f 3-4,5|uniq		//去重

```

### 8. grep 用法：

```
grep的规则表达式:

^  #锚定行的开始 如：'^grep'匹配所有以grep开头的行。    
$  #锚定行的结束 如：'grep$'匹配所有以grep结尾的行。    
.  #匹配一个非换行符的字符 如：'gr.p'匹配gr后接一个任意字符，然后是p。    
*  #匹配零个或多个先前字符 如：'*grep'匹配所有一个或多个空格后紧跟grep的行。    
.*   #一起用代表任意字符。   
[]   #匹配一个指定范围内的字符，如'[Gg]rep'匹配Grep和grep。    
[^]  #匹配一个不在指定范围内的字符，如：'[^A-FH-Z]rep'匹配不包含A-R和T-Z的一个字母开头，紧跟rep的行。    
\(..\)  #标记匹配字符，如'\(love\)'，love被标记为1。    
\<      #锚定单词的开始，如:'\<grep'匹配包含以grep开头的单词的行。    
\>      #锚定单词的结束，如'grep\>'匹配包含以grep结尾的单词的行。    
x\{m\}  #重复字符x，m次，如：'0\{5\}'匹配包含5个o的行。    
x\{m,\}  #重复字符x,至少m次，如：'o\{5,\}'匹配至少有5个o的行。    
x\{m,n\}  #重复字符x，至少m次，不多于n次，如：'o\{5,10\}'匹配5--10个o的行。   
\w    #匹配文字和数字字符，也就是[A-Za-z0-9]，如：'G\w*p'匹配以G后跟零个或多个文字或数字字符，然后是p。   
\W    #\w的反置形式，匹配一个或多个非单词字符，如点号句号等。   
\b    #单词锁定符，如: '\bgrep\b'只匹配grep。  

POSIX字符:

为了在不同国家的字符编码中保持一至，POSIX(The Portable Operating System Interface)增加了特殊的字符类，如[:alnum:]是[A-Za-z0-9]的另一个写法。要把它们放到[]号内才能成为正则表达式，如[A- Za-z0-9]或[[:alnum:]]。在linux下的grep除fgrep外，都支持POSIX的字符类。

[:alnum:]    #文字数字字符   
[:alpha:]    #文字字符   
[:digit:]    #数字字符   
[:graph:]    #非空字符（非空格、控制字符）   
[:lower:]    #小写字符   
[:cntrl:]    #控制字符   
[:print:]    #非空字符（包括空格）   
[:punct:]    #标点符号   
[:space:]    #所有空白字符（新行，空格，制表符）   
[:upper:]    #大写字符   
[:xdigit:]   #十六进制数字（0-9，a-f，A-F）

命令参数：

-a   --text   #不要忽略二进制的数据。   
-A<显示行数>   --after-context=<显示行数>   #除了显示符合范本样式的那一列之外，并显示该行之后的内容。   
-b   --byte-offset   #在显示符合样式的那一行之前，标示出该行第一个字符的编号。   
-B<显示行数>   --before-context=<显示行数>   #除了显示符合样式的那一行之外，并显示该行之前的内容。   
-c    --count   #计算符合样式的列数。   
-C<显示行数>    --context=<显示行数>或-<显示行数>   #除了显示符合样式的那一行之外，并显示该行之前后的内容。   
-d <动作>      --directories=<动作>   #当指定要查找的是目录而非文件时，必须使用这项参数，否则grep指令将回报信息并停止动作。   
-e<范本样式>  --regexp=<范本样式>   #指定字符串做为查找文件内容的样式。   
-E      --extended-regexp   #将样式为延伸的普通表示法来使用。   
-f<规则文件>  --file=<规则文件>   #指定规则文件，其内容含有一个或多个规则样式，让grep查找符合规则条件的文件内容，格式为每行一个规则样式。   
-F   --fixed-regexp   #将样式视为固定字符串的列表。   
-G   --basic-regexp   #将样式视为普通的表示法来使用。   
-h   --no-filename   #在显示符合样式的那一行之前，不标示该行所属的文件名称。   
-H   --with-filename   #在显示符合样式的那一行之前，表示该行所属的文件名称。   
-i    --ignore-case   #忽略字符大小写的差别。   
-l    --file-with-matches   #列出文件内容符合指定的样式的文件名称。   
-L   --files-without-match   #列出文件内容不符合指定的样式的文件名称。   
-n   --line-number   #在显示符合样式的那一行之前，标示出该行的列数编号。   
-q   --quiet或--silent   #不显示任何信息。   
-r   --recursive   #此参数的效果和指定“-d recurse”参数相同。   
-s   --no-messages   #不显示错误信息。   
-v   --revert-match   #显示不包含匹配文本的所有行。   
-V   --version   #显示版本信息。   
-w   --word-regexp   #只显示全字符合的列。   
-x    --line-regexp   #只显示全列符合的列。   
-y   #此参数的效果和指定“-i”参数相同。

```

### 9. shell 重定向：

```
>  默认为标准输出重定向，与 1> 相同
2>&1  意思是把 标准错误输出 重定向到 标准输出.
/dev/null是一个文件，这个文件比较特殊，所有传给它的东西它都丢弃掉
1>&2 正确返回值传递给2输出通道 &2表示2输出通道
2>&1 错误返回值传递给1输出通道, 同样&1表示1输出通道.

```

### 10. shell中$0,$?,$!等的特殊用法

```
$$
Shell本身的PID（ProcessID）
$!
Shell最后运行的后台Process的PID
$?
最后运行的命令的结束代码（返回值）
$-
使用Set命令设定的Flag一览
$*
所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
$@
所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。
$#
添加到Shell的参数个数
$0
Shell本身的文件名
$1～$n
${!⟨name⟩} //name的value也是一个变量名，输出最终值

```

### 12. tr用法
```
tr -c -d -s ["string1_to_translate_from"]["string2_to_translate_to"] < input-file

-c 用字符串1中字符集的补集替换此字符集，要求字符集为ASCII。
-d 删除字符串1中所有出现的字符。
-s 删除“连续着的”重复字母，只保留第一个
input-file是转换文件名。虽然可以使用其他格式输入，但这种格式最常用。

2、字符范围
指定字符串1或字符串2的内容时，只能使用单字符或字符串范围或列表。
[a-z] a-z内的字符组成的字符串。
[A-Z] A-Z内的字符组成的字符串。
[0-9] 数字串。
\octal 一个三位的八进制数，对应有效的ASCII字符。
[O*n] 表示字符O重复出现指定次数n。因此[O*2]匹配OO的字符串。
tr中特定控制字符的不同表达方式
速记符含义八进制方式
\a Ctrl-G  铃声\007
\b Ctrl-H  退格符\010
\f Ctrl-L  走行换页\014
\n Ctrl-J  新行\012
\r Ctrl-M  回车\015
\t Ctrl-I  tab键\011
\v Ctrl-X  \030

cat file | tr [a-z] [A-Z] > new_file //小写变大写

```

### 13. sort 用法
```
-u: 忽略相同行使用-u选项或者uniq：
-b：忽略每行前面开始出的空格字符；
-c：检查文件是否已经按照顺序排序；
-d：排序时，处理英文字母、数字及空格字符外，忽略其他的字符；
-f：排序时，将小写字母视为大写字母；
-i：排序时，除了040至176之间的ASCII字符外，忽略其他的字符；
-m：将几个排序号的文件进行合并；
-M：将前面3个字母依照月份的缩写进行排序；
-n：依照数值的大小排序；
-o<输出文件>：将排序后的结果存入制定的文件；
-r：以相反的顺序来排序；
-t<分隔字符>：指定排序时所用的栏位分隔字符；
+<起始栏位>-<结束栏位>：以指定的栏位来排序，范围由起始栏位到结束栏位的前一栏位。

$ sort -nrk 3 -t: sort.txt
-n是按照数字大小排序，-r是以相反顺序，-k是指定需要爱排序的栏位，-t指定栏位分隔符为冒号
$ sort -t ' ' -k 1.2,1.2 -nrk 3,3 facebook.txt
对第一列的第2个字符进行排序，然后按第3列进行降序排列。

```

### 14.sed流编辑器

```
$ sed [-nefr] [动作]
选项与参数：
-n ：使用安静(silent)模式。在一般 sed 的用法中，所有来自 STDIN 的数据一般都会被列出到终端上。但如果加上 -n 参数后，则只有经过sed 特殊处理的那一行(或者动作)才会被列出来。
-e ：直接在命令列模式上进行 sed 的动作编辑；
-f ：直接将 sed 的动作写在一个文件内， -f filename 则可以运行 filename 内的 sed 动作；
-r ：sed 的动作支持的是延伸型正规表示法的语法。(默认是基础正规表示法语法)
-i ：直接修改读取的文件内容，而不是输出到终端。

动作说明： [n1[,n2]]function
n1, n2 ：不见得会存在，一般代表『选择进行动作的行数』，举例来说，如果我的动作是需要在 10 到 20 行之间进行的，则『 10,20[动作行为] 』

function：
a ：新增， a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)～
c ：取代， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行！
d ：删除，因为是删除啊，所以 d 后面通常不接任何咚咚；
i ：插入， i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)；
p ：列印，亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行～
s ：取代，可以直接进行取代的工作哩！通常这个 s 的动作可以搭配正规表示法！例如 1,20s/old/new/g 就是啦！

$ nl /etc/passwd | sed '2,5d'   //删除2到5行
$ nl /etc/passwd | sed '3,$d'  //要删除第 3 到最后一行
$ nl /etc/passwd | sed '2a drink tea' //追回到第3行上
$ nl /etc/passwd | sed -n '5,7p' //仅列出 /etc/passwd 文件内的第 5-7 行
$ nl /etc/passwd | sed -n '/root/p' //使用-n的时候将只打印包含模板的行。
$nl /etc/passwd | sed  '/root/d'  //删除/etc/passwd所有包含root的行，其他行输出
$ nl /etc/passwd | sed -n '/root/{s/bash/blueshell/;p}'  //搜索/etc/passwd,找到root对应的行，执行后面花括号中的一组命令，每个命令之间用分号分隔，这里把bash替换为blueshell，再输出这行：
$ nl /etc/passwd | sed -n '/bash/{s/bash/blueshell/;p;q}'      //如果只替换/etc/passwd的第一个bash关键字为blueshell，就退出
$ sed 's/要被取代的字串/新的字串/g' //sed 的搜寻与替代的与 vi 相当的类似
$ ifconfig en0 |grep 'inet '|sed 's/^.*inet //g'|sed 's/ net.*$//g' //提到ip地址
$ nl /etc/passwd | sed -e '3,$d' -e 's/bash/blueshell/' //一条sed命令，删除/etc/passwd第三行到末尾的数据，并把bash替换为blueshell
$ sed -i 's/\.$/\!/g' regular_express.txt //利用 sed 将 regular_express.txt 内每一行结尾若为 . 则换成 !
$ sed -i '$a # This is a test' regular_express.txt //利用 sed 直接在 regular_express.txt 最后一行加入『# This is a test』
```

### 15. awk用法

```
内置变量
ARGC               命令行参数个数
ARGV               命令行参数排列
ENVIRON            支持队列中系统环境变量的使用
FILENAME           awk浏览的文件名
FNR                浏览文件的记录数
FS                 设置输入域分隔符，等价于命令行 -F选项
NF                 浏览记录的域的个数
NR                 已读的记录数
OFS                输出域分隔符,输出字段的分隔符，用于打印时分隔字段，默认为空格。
ORS                输出记录分隔符,用于打印时分隔记录，默认为换行符
RS                 控制记录分隔符,行分隔符，用于分割每一行，默认是换行符。
OFMT			数字输出的格式，默认为％.6g。

内置函数
toupper()
$ awk -F ':' '{ print toupper($1) }' demo.txt
$ awk '条件 动作' 文件名
$ awk -F ':' '/usr/ {print $1}' demo.txt
$ awk -F ':' 'NR % 2 == 1 {print $1}' demo.txt
$ awk -F ':' '$1 == "root" {print $1}' demo.txt

if 语句
$ awk -F ':' '{if ($1 > "m") print $1}' demo.txt
$ awk -F ':' '{if ($1 > "m") print $1; else print "---"}' demo.txt

$ awk -F ':' '{ print $1 }' demo.txt //用-F参数指定分隔符为冒号。然后提取第一个字段
$ echo 'this is a test' | awk '{print $NF}' //$NF就代表最后一个字段

```




