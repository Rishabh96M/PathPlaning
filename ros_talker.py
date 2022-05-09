import rospy
from geometry_msgs.msg import Twist
import time
import math


def send_vel(path, radius, w_dist, step):
    """
    Definition
    ---
    Method to move turtlebot on ROS Gazebo with cmd_vel topic

    Parameters
    ---
    actions : list of actions to follow
    radius : radius of the robot
    w_dist : distance between the wheels of the robot
    step : step size for each movement

    Returns
    ---
    Bool : True when done
    """
    rospy.init_node('robot_talker', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    msg = Twist()
    dir = [1, 0]

    for i in range(1, len(path)):
        new_dir = [path[i][0] - path[i-1][0], path[i][1] - path[i-1][1]]
        th = math.asin(((new_dir[0] * dir[1]) - (new_dir[1] * dir[0]))
                       / (math.sqrt(new_dir[0]**2 + new_dir[1]**2)
                       * math.sqrt(dir[0]**2 + dir[1]**2)))

        th = -round(th * 180/3.14)
        dist = round(math.dist(path[i], path[i-1]))
        print('goint to point: ', path[i])
        cnt = 0
        while cnt < abs(th*1.9):
            cnt += 1
            if th < 0:
                ang_v = -0.105
            else:
                ang_v = 0.105
            publishMsg(msg, 0, ang_v, pub)
        cnt = 0
        while cnt < dist*10:
            cnt += 1
            lin_v = 0.1
            publishMsg(msg, lin_v, 0, pub)
        publishMsg(msg, 0, 0, pub)
        dir = new_dir
    return True


def publishMsg(msg, lin_v, ang_v, pub):
    """
    Definition
    ---
    Method to publish msg to cmd_vel

    Parameters
    ---
    msg : Twist()
    lin_v : linear velocity
    ang_v : angular velocity
    pub : ROS publisher topic
    """
    msg.angular.z = ang_v
    msg.angular.x = 0
    msg.angular.y = 0
    msg.linear.x = lin_v
    msg.linear.y = 0
    msg.linear.z = 0
    pub.publish(msg)
    time.sleep(0.1)
