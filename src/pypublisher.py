#!/usr/bin/env python

# Import required Python code.

import rospy
import time
# Give ourselves the ability to run a dynamic reconfigure server.
from dynamic_reconfigure.server import Server as DynamicReconfigureServer

# Import custom message data and dynamic reconfigure variables.
from performance_test.msg import SuperAwesome
from performance_test.cfg import performanceTestConfig as ConfigType

# Node example class.
class PerformanceTest(object):
    # Must have __init__(self) function for a class, similar to a C++ class constructor


    def __init__(self):
        # Get the ~private namespace parameters from command line or launch file.
        init_message = rospy.get_param('~data', 'hola')
        rate = float(rospy.get_param('~rate', '1.0'))
        topic = rospy.get_param('~topic', 'message')
        rospy.loginfo('rate = %d', rate)
        rospy.loginfo('topic = %s', topic)
        # Create a dynamic reconfigure server.
        self.server = DynamicReconfigureServer(ConfigType, self.reconfigure)
        # Create a publisher for our custom message.
        pub = rospy.Publisher(topic, SuperAwesome,10)
        # Set the message to publish as our custom message.
        msg = SuperAwesome()
        # Initialize message variables.
        
        msg.data = init_message
        count = 1
        elapsed = 0
        # Main while loop.
        while not rospy.is_shutdown():

            start = time.time()

            # Fill in custom message variables with values from dynamic reconfigure server.
            msg.data = self.data
       
            # Publish our custom message.
            pub.publish(msg)
            # Sleep for a while before publishing new messages. Division is so rate != period.
            if rate:
                rospy.sleep(1/rate)
            else:
                rospy.sleep(1.0)

            end = time.time()
            elapsed += end - start
            print 'time ', elapsed/count ,' of ', count, 'loops'
            count += 1;

            if count == 101: break 


    

    # Create a callback function for the dynamic reconfigure server.
    def reconfigure(self, config, level):
        # Fill in local variables with values received from dynamic reconfigure clients (typically the GUI).
        self.data = config["data"]
        # self.a = config["a"]
        # self.b = config["b"]
        # Return the new variables.
        return config

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('pypublisher')
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        ne = PerformanceTest()
    except rospy.ROSInterruptException: pass

    rospy.spin()

