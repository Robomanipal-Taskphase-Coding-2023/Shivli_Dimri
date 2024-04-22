cmake_minimum_required(VERSION 3.0.2)

project(areaurdf_noarea1)

find_package(catkin REQUIRED COMPONENTS
cv_bridge
image_transport
rospy
sensor_msgs
std_msgs
)
find_package(urdf REQUIRED) 


catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

include_directories(include ${catkin_INCLUDE_DIRS})
include_directories(${urdf_INCLUDE_DIRS})
add_executable(parser src/parser.cpp)
target_link_libraries(parser ${catkin_LIBRARIES} ${urdf_LIBRARIES})
