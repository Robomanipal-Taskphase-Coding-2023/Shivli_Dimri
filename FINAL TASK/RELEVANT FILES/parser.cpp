








// #include <urdf/model.h>
// #include "ros/ros.h"

// int main(int argc, char** argv){
//   ros::init(argc, argv, "parser");
//   if (argc != 2){
//     ROS_ERROR("Need a urdf file as argument");
//     return -1;
//   }
//   std::string urdf_file = argv[1];

//   urdf::Model model;
//   if (!model.initFile(urdf_file)){
//     ROS_ERROR("Failed to parse urdf file");
//     return -1;
//   }
//   ROS_INFO("Successfully parsed urdf file");

//   // Extract ball positions
//   std::vector<std::pair<double, double>> ball_positions;
//   for (const auto& link : model.links_) {
//     if (link.first.find("ball") == 0) { // Assuming ball links start with "ball"
//       auto visual = link.second->visual;
//       if (visual) {
//         auto origin = visual->origin;
//         // if (!origin.position.empty()) {
//         //         double x = origin.position.x;
//         //         double y = origin.position.y;
//         //         ball_positions.push_back(std::make_pair(x, y));
//         //     }
//         if (origin) {
//           double x = origin.position.x;
//           double y = origin.position.y;
//           ball_positions.push_back(std::make_pair(x, y));
//         }
//       }
//     }
//   }

//   // Print ball positions
//   ROS_INFO("Ball Positions:");
//   for (size_t i = 0; i < ball_positions.size(); ++i) {
//     ROS_INFO("Ball %zu: x = %f, y = %f", i+1, ball_positions[i].first, ball_positions[i].second);
//   }

//   return 0;
// }






#include <urdf/model.h>
#include "ros/ros.h"

int main(int argc, char** argv){
  ros::init(argc, argv, "my_parser");
  if (argc != 2){
    ROS_ERROR("Need a urdf file as argument");
    return -1;
  }
  std::string urdf_file = argv[1];

  urdf::Model model;
  if (!model.initFile(urdf_file)){
    ROS_ERROR("Failed to parse urdf file");
    return -1;
  }
  ROS_INFO("Successfully parsed urdf file");
  return 0;
}
