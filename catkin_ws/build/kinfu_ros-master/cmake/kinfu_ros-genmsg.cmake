# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "kinfu_ros: 1 messages, 1 services")

set(MSG_I_FLAGS "-Ikinfu_ros:/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(kinfu_ros_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv" NAME_WE)
add_custom_target(_kinfu_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "kinfu_ros" "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv" "geometry_msgs/Quaternion:geometry_msgs/Pose:kinfu_ros/TSDF:std_msgs/Header:geometry_msgs/Point"
)

get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg" NAME_WE)
add_custom_target(_kinfu_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "kinfu_ros" "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg" "geometry_msgs/Quaternion:geometry_msgs/Pose:std_msgs/Header:geometry_msgs/Point"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kinfu_ros
)

### Generating Services
_generate_srv_cpp(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kinfu_ros
)

### Generating Module File
_generate_module_cpp(kinfu_ros
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kinfu_ros
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(kinfu_ros_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(kinfu_ros_generate_messages kinfu_ros_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_cpp _kinfu_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_cpp _kinfu_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kinfu_ros_gencpp)
add_dependencies(kinfu_ros_gencpp kinfu_ros_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kinfu_ros_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kinfu_ros
)

### Generating Services
_generate_srv_eus(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kinfu_ros
)

### Generating Module File
_generate_module_eus(kinfu_ros
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kinfu_ros
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(kinfu_ros_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(kinfu_ros_generate_messages kinfu_ros_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_eus _kinfu_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_eus _kinfu_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kinfu_ros_geneus)
add_dependencies(kinfu_ros_geneus kinfu_ros_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kinfu_ros_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kinfu_ros
)

### Generating Services
_generate_srv_lisp(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kinfu_ros
)

### Generating Module File
_generate_module_lisp(kinfu_ros
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kinfu_ros
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(kinfu_ros_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(kinfu_ros_generate_messages kinfu_ros_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_lisp _kinfu_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_lisp _kinfu_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kinfu_ros_genlisp)
add_dependencies(kinfu_ros_genlisp kinfu_ros_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kinfu_ros_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kinfu_ros
)

### Generating Services
_generate_srv_nodejs(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kinfu_ros
)

### Generating Module File
_generate_module_nodejs(kinfu_ros
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kinfu_ros
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(kinfu_ros_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(kinfu_ros_generate_messages kinfu_ros_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_nodejs _kinfu_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_nodejs _kinfu_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kinfu_ros_gennodejs)
add_dependencies(kinfu_ros_gennodejs kinfu_ros_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kinfu_ros_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kinfu_ros
)

### Generating Services
_generate_srv_py(kinfu_ros
  "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kinfu_ros
)

### Generating Module File
_generate_module_py(kinfu_ros
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kinfu_ros
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(kinfu_ros_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(kinfu_ros_generate_messages kinfu_ros_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/srv/GetTSDF.srv" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_py _kinfu_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg/TSDF.msg" NAME_WE)
add_dependencies(kinfu_ros_generate_messages_py _kinfu_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kinfu_ros_genpy)
add_dependencies(kinfu_ros_genpy kinfu_ros_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kinfu_ros_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kinfu_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kinfu_ros
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(kinfu_ros_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kinfu_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kinfu_ros
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(kinfu_ros_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kinfu_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kinfu_ros
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(kinfu_ros_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kinfu_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kinfu_ros
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(kinfu_ros_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kinfu_ros)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kinfu_ros\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kinfu_ros
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(kinfu_ros_generate_messages_py geometry_msgs_generate_messages_py)
endif()
