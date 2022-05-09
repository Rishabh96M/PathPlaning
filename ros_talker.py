import rospy
from geometry_msgs.msg import Twist
import time


def send_vel(actions, radius, w_dist, step):
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
    for _, move in actions:
        cnt = 0
        publishMsg(msg, 0, 0, pub)
        print('Sending RPM\'s to robot: ', (move[0], move[1]))
        while cnt < 50:
            cnt += 1
            ang_v = (radius / w_dist) * (move[1] - move[0])
            lin_v = 0.5 * radius * (move[0] + move[1])
            publishMsg(msg, lin_v, ang_v, pub)
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
    msg.angular.z = ang_v / 4.5
    msg.angular.x = 0
    msg.angular.y = 0
    msg.linear.x = lin_v / 455
    msg.linear.y = 0
    msg.linear.z = 0
    pub.publish(msg)
    time.sleep(0.1)
