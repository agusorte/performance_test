// ROS includes.
#include <ros/ros.h>
#include <ros/time.h>
#include <std_msgs/String.h>
#include <sstream>

// Custom message includes. Auto-generated from msg/ directory.
#include "performance_test/SuperAwesome.h"

// Dynamic reconfigure includes.
#include <dynamic_reconfigure/server.h>
// Auto-generated from cfg/pdirectory.
#include <performance_test/performanceTestConfig.h>

//#include <performance_test/SuperAwesome.h>
/*
 * publisherRos_node.cpp
 *
 *  Created on: April, 2018
 *  Author: Agustin Ortega 
 *  Email: aortega.jim@gmail.com
 */

class publisherRos
{

public:
  
  explicit publisherRos(ros::NodeHandle nh, int rate = 10):nh_(nh),message_("hola"),rate_(rate){

  	pub_ = nh_.advertise<performance_test::SuperAwesome>("message", 10);

    ROS_INFO ("rate :%d", rate_);

  	ros::Rate loop_rate(rate_);

    count = 1;
    ros::Duration diffAcc;
    while (ros::ok()){
    

      ros::Time lasttime=ros::Time::now();


      performance_test::SuperAwesome msg;
      msg.data = message_;
  
      pub_.publish(msg);

      ros::spinOnce();
      loop_rate.sleep();
      //ros::sleep(1 / rate);

      ros::Time currtime = ros::Time::now();
      ros::Duration diff = currtime-lasttime;

     
      diffAcc += diff;
      
      ROS_INFO("average time %f of %d loops",diffAcc.toSec()*1.0/count, count);

    

      count++;

      if (count == 101) return;

      
    }


   
  };
 

private:
 //! ROS node handle.
  ros::NodeHandle nh_;

  //! The timer variable used to go to callback function at specified rate.
  ros::Timer timer_;

  //! Message publisher.
  ros::Publisher pub_;


  //! The actual message.
  std::string message_;

  performance_test::SuperAwesome mes2;

  int rate_;

  int count;



  	
};

int main(int argc, char **argv)
{
  ros::init(argc, argv, "publisherCPP");
  ros::NodeHandle n;

   int rate = 10;
  if (argc >1){

  	rate = atoi(argv[1]);
  }

  publisherRos publisher(n, rate);

  ros::spin();

  
  return 0;
}

