## 简单ROS机器人_Team101：代码部分

----

### 运行环境

---

1. 硬件：

   至少配备以下模块的启智ROS：激光雷达、机械臂、集成编码器的电机、摄像头。

2. 软件：

   * Ubuntu 16.04

   * ROS kinetic

   * IAI-Kinect2
   * python3.5
   * python libs: tklinker, matpoltlib, time, subprocess

### 使用步骤

---

1. 配置运行环境
    * 配置ubuntu16.04：https://ubuntu.com/tutorials/tutorial-install-ubuntu-desktop#1-overview
    * 安装ROS（kinetic）：https://wiki.ros.org/kinetic/Installation/Ubuntu
    * 获取IAI-Kinetic2 ：https://github.com/code-iai/iai_kinect2
    * 安装RoboWare Studio

2. 获取源码

    ```
   $ git clone git@github.com:sebuaa2020/Team101.git
   ```

3. 编译运行
    ```
   $ cd code
   $ cd Team_101
   $ cd python GUI
   $ python -u gui.py
   ```



### 代码说明

---

#### 前端
前端代码主要位于python GUI文件夹中，主要采用python编写。包括GUI界面，机器人总控，以及前端部分对建图、导航、自主行走相关类。

#### 后端

后端内容分为资源和代码。

- src文件夹中保存了ros自主避障行走代码、坐标点导航代码、激光雷达代码、键盘控制行走代码
- launch和nav_lidar文件夹中保存了ros基本硬件与算法调用脚本和历史参数
- urdf、rviz、config、worlds为运行ros场景所需要的必要文件

### 项目目录

---

```
.
├─config                         //场景参数
├─launch                         //ros启动功能、机器人脚本
├─maps                           //保存地图
├─nav_lidar                      //导航、避障算法和参数设置
├─python GUI                     //前段控制程序
├─rviz                           //软件参数设置
├─src                            //自主行走控制
├─urdf                           //软件模块参数设置
├─database                       //存储用户名及密码的小型数据库
└─worlds                         //场景
```


### 参考文献

---

[1] 启智ROS机器人开发手册

[2] RoboWare_Studio_Manual_1.1.0_CHS

[3]  Learning ROS for Robotics Programming