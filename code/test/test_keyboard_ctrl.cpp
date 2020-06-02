#include<stdio.h>
#include <Windows.h>
#include <stdlib.h>
#include<conio.h>
#include<time.h>
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <termios.h>

static float linear_vel = 0.1;
static float angular_vel = 0.1;
static int k_vel = 3;

int GetCh()
{
  static struct termios oldt, newt;
  tcgetattr( STDIN_FILENO, &oldt);
  newt = oldt;
  newt.c_lflag &= ~(ICANON);
  tcsetattr( STDIN_FILENO, TCSANOW, &newt);
  int c = getchar();
  tcsetattr( STDIN_FILENO, TCSANOW, &oldt);
  return c;
}

int move(int argc, char** argv)
{
  ros::init(argc, argv, "keyboard_vel_cmd");

  printf("���̿���WPR�����ˣ� \n");
  printf("w - ��ǰ���� \n");
  printf("s - ������ \n");
  printf("a - ������� \n");
  printf("d - ���Ҽ��� \n");
  printf("q - �������� \n");
  printf("e - �������� \n");
  printf("�ո� - ɲ�� \n");
  printf("x - �˳� \n");
  printf("------------- \n");

  ros::NodeHandle n;
  ros::Publisher cmd_vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);

  geometry_msgs::Twist base_cmd;
  base_cmd.linear.x = 0;
  base_cmd.linear.y = 0;
  base_cmd.angular.z = 0;

  while(n.ok())
  {
    int cKey = GetCh();
    if(cKey=='w')
    {
      base_cmd.linear.x += linear_vel;
      if(base_cmd.linear.x > linear_vel*k_vel)
        base_cmd.linear.x = linear_vel*k_vel;
      cmd_vel_pub.publish(base_cmd);
      printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",base_cmd.linear.x,base_cmd.linear.y,base_cmd.angular.z);
    } 
    else if(cKey=='s')
    {
      base_cmd.linear.x += -linear_vel;

      if(base_cmd.linear.x < -linear_vel*k_vel)
        base_cmd.linear.x = -linear_vel*k_vel;
      cmd_vel_pub.publish(base_cmd);
      printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",base_cmd.linear.x,base_cmd.linear.y,base_cmd.angular.z);
    } 
    else if(cKey=='a')
    {
      base_cmd.linear.y += linear_vel;
      if(base_cmd.linear.y > linear_vel*k_vel)
        base_cmd.linear.y = linear_vel*k_vel;
      cmd_vel_pub.publish(base_cmd);
      printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",base_cmd.linear.x,base_cmd.linear.y,base_cmd.angular.z);
    }
    else if(cKey=='d')
    {
      base_cmd.linear.y += -linear_vel;
      if(base_cmd.linear.y < -linear_vel*k_vel)
        base_cmd.linear.y = -linear_vel*k_vel;
      cmd_vel_pub.publish(base_cmd);
      printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",base_cmd.linear.x,base_cmd.linear.y,base_cmd.angular.z);
    } 
    else if(cKey=='q')
    {
      base_cmd.angular.z += angular_vel;
      if(base_cmd.angular.z > angular_vel*k_vel)
        base_cmd.angular.z = angular_vel*k_vel;
      cmd_vel_pub.publish(base_cmd);
      printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",base_cmd.linear.x,base_cmd.linear.y,base_cmd.angular.z);
    } 
    else if(cKey=='e')
    {
      base_cmd.angular.z += -angular_vel;
      if(base_cmd.angular.z < -angular_vel*k_vel)
        base_cmd.angular.z = -angular_vel*k_vel;
      cmd_vel_pub.publish(base_cmd);
      printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",base_cmd.linear.x,base_cmd.linear.y,base_cmd.angular.z);
    } 
    else if(cKey==' ')
    {
      base_cmd.linear.x = 0;
      base_cmd.linear.y = 0;
      base_cmd.angular.z = 0;
      cmd_vel_pub.publish(base_cmd);
      printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",base_cmd.linear.x,base_cmd.linear.y,base_cmd.angular.z);
    } 
    else if(cKey=='x')
    {
      base_cmd.linear.x = 0;
      base_cmd.linear.y = 0;
      base_cmd.angular.z = 0;
      cmd_vel_pub.publish(base_cmd);
      printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",base_cmd.linear.x,base_cmd.linear.y,base_cmd.angular.z);
      printf("�˳��� \n");
      return 0;
    } 
    else
    {
       printf(" - δ����ָ�� \n");
    }
    
  }
  return 0;
}

//------------------------------------------------------------------------------------------------------------------
//����Ϊ������Բ��֣�����C����û�бȽϹ��ϵĵ�Ԫ���Թ��ߣ���д��һ�����Գ��� 
int get_next_key(){
	char a[9] = "wsadqe x";
	srand((int)time(0));
 	int rand_num = rand();
	char c = a[rand_num%8];//���ȡһ���Ϸ��ַ�
	int num; //c��Ӧ�ļ���ֵ
	if(c==' ')
		num = 20;
	else
		num = 65+c-'a';
	return num;
}

int main(int argc, char** argv){
	int num = 0;
	for(i = 0; i < 10; i++){//������10�����
		while(num != 65+'x'-'a'){ //��δ�����˳���ʱ 
	        num = get_next_key();
			keybd_event(num,0,0,0);
		} 
		move(argc, argv);
	}
	//����һ��Ƿ��ַ�����
	num = rand()%64; //���ȡһ���Ƿ��ַ� 
	if(num == 0)
		num = 64;
	else if (num == 20)
		num = 66;
	keybd_event(num,0,0,0);
	move(argc, argv);
}
