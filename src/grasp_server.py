#!/usr/bin/env python 

import rospy
import numpy as np
import time
from send_command_to_robot.srv import data, dataResponse

def grasping(req):

    print(req.pose.position.x)
    print(req.pose.position.y)
    print(req.pose.position.z)
    print(req.pose.orientation.x)
    print(req.pose.orientation.y)
    print(req.pose.orientation.z)
    print(req.pose.orientation.w)
    print(req.id)
	# receive data
	

if __name__ == "__main__":

	rospy.init_node("grasp_server")
	pick = rospy.Service("grasp", data, grasping)
	print("grasp server")
	rospy.spin()