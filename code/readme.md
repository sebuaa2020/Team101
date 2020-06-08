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






### 项目目录

---

```
.
├─code                          // 代码目录
│  └─Team_101                   // 项目代码
│  └─test                       // 测试代码
```


### 参考文献

---

[1] 启智ROS机器人开发手册

[2] RoboWare_Studio_Manual_1.1.0_CHS

[3]  Learning ROS for Robotics Programming