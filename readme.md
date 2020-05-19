## 简单ROS机器人

[toc]

### 项目简介

本项目为2020年北京航空航天大学软件工程课程所要求项目。

本项目包括三方面：机器人避障、路径规划、目标识别与抓取。本项目力求结合软件与硬件，完成具有在室内环境下进行自主建立地图，识别指令并完成指令所对应工作功能的简单ROS机器人。该机器人在物流行业，特别是室内仓库分拣问题中可有较直接的应用。但经过一定调整，也可适用于家庭智能机器人，室内导航机器人等问题。

### 项目管理

依托群聊和看板进行组内对项目的讨论、推进和修改，每周二晚为例会时间。

文档部分直接在本地修改审核后即可push到仓库，代码部分先新建分支进行单个任务的编写，审核一致通过后再merge到master分支。

* 克隆项目

  ````git
  $ git clone git@github.com:sebuaa2020/Team101.git
  ````

* 创建切换分支并修改提交

  ````git
  $ git branch [branchname]
  $ git checkout [branchname]
  ...
  $ git commit -m "..."
  $ git push origin [branchname]
  ````

* 分支合并

  ```git
  $ git checkout master
  $ git pull
  $ git merge [branchname]
  $ git push origin master
  ```

### 项目目录

````
.
├─code                          // 代码目录
│  └─GUI                        // GUI部分
│      └─maps
├─docs                          // 文档部分
└─meetings                      // 会议纪要
````

### 项目进度

#### 已完成

* **文档部分**
  * SRS 需求规格说明书
  * SDP 开发计划
  * SDD 软件设计说明书

* **代码部分**
  * GUI 初版
  * 地图建立
  * 定点巡航

#### 待完成

* **文档部分**
  * STD软件测试说明
  * 各文档跟进迭代
* **代码部分**
  * 识别抓取
  * 代码整合