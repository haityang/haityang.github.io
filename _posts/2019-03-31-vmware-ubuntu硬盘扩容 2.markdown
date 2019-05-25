1.先在VMWare设置里扩展硬盘尺寸。

2.打开终端

```
sudo fdisk -l				//查看fdisk
sudo fdisk /dev/sda		//处理sda
p							//主分区
n							//新建分区
p							//主分区
2
p
w							//写入更改
sudo reboot
df -h
sudo mkfs.ext3 /dev/sda2		//格式化
sudo mkdir /cm
sudo mount /dev/sda2 /cm		//挂接
df -h
sudo vi /etc/fstab			//写入分区表文件，开机自动挂接
最后加上这行：
/dev/sda2 /cm ext3 defaults 0 0

```


Done!