#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example Python node to listen on a specific topic."""

# Import required Python code.
# pysubscriber.py
 
# Created on: April, 2018
# Author: Agustin Ortega 
# Email: aortega.jim@gmail.com
import rospy


# Import custom message data and dynamic reconfigure variables.
from performance_test.msg import SuperAwesome


def callback(data):
    """Handle subscriber data."""
    # Simply print out values in our custom message.
    rospy.loginfo(rospy.get_name() + " I heard %s", data.data)


def subscriber():
    """Configure subscriber."""
    # Create a subscriber with appropriate topic, custom message and name of
    # callback function.
    rospy.Subscriber('message', SuperAwesome, callback)


# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('pysubscriber')
    # Go to the main loop.
    subscriber()
    # Wait for messages on topic, go to callback function when new messages
    # arrive.
    rospy.spin()