## 简单ROS机器人_Team101

----

### 运行环境

---

1. 硬件：

   至少配备以下模块的启智ROS：激光雷达、机械臂、集成编码器的电机、摄像头。

2. 软件：

   * Ubuntu 16.04

   * ROS kinetic

   * IAI-Kinect2

### 使用步骤

---

1. 配置运行环境

2. 获取源码

   ```
   $ git clone git@github.com:sebuaa2020/Team101.git
   ```

3. 编译运行

//补充具体指令

### 项目简介

---

本项目为北京航空航天大学计算机学院2020年春季学期《软件工程》课程开发项目。在课程组提供的ROS机器人等软硬件基础资源上开发一款实现避障、路径规划和检测抓取目标的简单机器人。机器人主要功能有主动控制、动态障碍物避障、实时建立环境地图、动态路径规划以及识别抓取目标物。

### 项目应用

---

本项目力求结合软件与硬件，完成具有在室内环境下进行自主建立地图、识别指令并具有完成指令所对应工作功能的简单ROS机器人。该机器人在物流行业，特别是室内仓库分拣场景中可有较直接的应用。若经过一定调整，也可升级成家庭智能机器人、室内导航机器人等复杂机器人。

### 功能特性（待定）

---

1. 自动建图

   管理员发出“建立地图”指令后，机器人自动绕场一周，使用激光传感器检测障碍物并建立地图模型。

   //补充具体指令

2. 定点巡航

   用户设置目标点后，机器人自动规划路线到达指定地点

3. 目标检测与抓取

   用户设置抓取目标后，机器人自动识别物体并进行目标抓取。

### 项目目录

---

```
.
├─code                          // 代码目录
│  └─GUI                        // GUI部分
│      └─maps
├─docs                          // 文档部分
└─meetings                      // 会议纪要
```

### 项目管理

---

小组使用微信群以及看板模块进行对项目的讨论、推进和修改，每周二为交流进度解决问题的例会时间。

文档部分在组内进行审核后直接push到仓库，代码部分则是各自新建分支开展工作，在审核一致后再merge到master分支。

1. 克隆项目

   ```
   $ git clone git@github.com:sebuaa2020/Team101.git
   ```

2. 创建切换分支并修改提交

   ```
   $ git branch [branchname]
   $ git checkout [branchname]
   ...
   $ git commit -m "..."
   $ git push origin [branchname]
   ```

3. 分支合并

   ```
   $ git checkout master
   $ git pull
   $ git merge [branchname]
   $ git push origin master
   ```

### 参考文献

---

[1] 启智ROS机器人开发手册

[2] RoboWare_Studio_Manual_1.1.0_CHS

[3]  Learning ROS for Robotics Programming