#!/usr/bin/env python

import rospy
import json
from bin_projet.srv import *
from std_msgs.msg import String

class bin_server:
    def __init__(self):
	rospy.init_node("bin_state")
	rospy.Service("bin_state_server", state_msg, self.change_state)
	self.pub = rospy.Publisher('bin_state', String, queue_size=10)
	self.rate = rospy.Rate(15) # 15hz
	self.bin_state = {
	"bin1" : 0,
	"bin2" : 0,
	"bin3" : 0,
	"bin4" : 0,
	"bin5" : 0 }

    def change_state(self,request):
	self.bin_state["bin%d"%(request.id_poubelle.data)]=request.state.data
	response=state_msgResponse()
	response.res.data=True
	return response
	print(bin_state)
	
    def run(self):
	while not rospy.is_shutdown():
		json_bin=json.dumps(self.bin_state)
		self.pub.publish(json_bin)
		self.rate.sleep()

if __name__ == '__main__':
    try:
	node=bin_server()
	node.run()
    except rospy.ROSInterruptException:
	pass
