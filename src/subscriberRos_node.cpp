// ROS includes.
#include <ros/ros.h>
#include <ros/time.h>
#include <std_msgs/String.h>
#include <sstream>
#include <performance_test/SuperAwesome.h>
/*
 * subscriberRos_node.cpp
 *
 *  Created on: April, 2018
 *  Author: Agustin Ortega 
 *  Email: aortega.jim@gmail.com
 */


class subscriberRos
{

public:
	explicit subscriberRos(ros::NodeHandle nh):nh_(nh){
      
      sub_ = nh_.subscribe("message", 10, &subscriberRos::callback,this);

    };


  
  void callback(const performance_test::SuperAwesome& msg){
  	  ROS_INFO("I heard: [%s]", msg.data.c_str());
  }
 
 private:
  //! ROS node handle.
  ros::NodeHandle nh_;
  ros::Subscriber sub_;


};


int main(int argc, char **argv)
{
  ros::init(argc, argv, "subscriberCPP");
  ros::NodeHandle n;


  subscriberRos subscriber(n);

  ros::spin();

  
  return 0;
}

