#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == '__main__' :
    rospy.init_node('simple_publishier_py',anonymous=True)
    pub = rospy.Publisher("chatter",String,queue_size=10) #quesize는 메세지 범퍼의 사이즈 
    r = rospy.Rate(10) #10hz 로 퍼블리쉬되게 설정 
    counter = 0 #메세지 전체 개수를 저장 
    while not rospy.is_shutdown(): #꺼지지 않은 경우
        hello_msg = "Hello World from PYhton : %d" % counter
        pub.publish(hello_msg)
        r.sleep()
        counter += 1