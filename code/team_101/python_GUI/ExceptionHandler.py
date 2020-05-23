from motion import move
class Exception:
    def __init__(self,type,current):
        self.ExceptionType = type #异常类型
        self.current = current #记录当前行为
    '''
    Different types of defects:
    0 : 停止机器人[使用场景: 撞到物体时等]
    1 : 停止机器人10s, 再次检测是否适宜移动.是则恢复原事件,否则停止机器人[使用场景: 激光雷达监测到障碍物时]
    2 : 机械臂归位[使用场景: 抓取失败时]
    3 : 重启程序[使用场景: gazebo软件异常]
    '''
    def ExceptionHandler(self):
        if self.ExceptionType == 0 :
            m = move(0,'stop')
            m.move()
        elif self.ExceptionType == 1 :

