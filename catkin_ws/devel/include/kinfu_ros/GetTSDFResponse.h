// Generated by gencpp from file kinfu_ros/GetTSDFResponse.msg
// DO NOT EDIT!


#ifndef KINFU_ROS_MESSAGE_GETTSDFRESPONSE_H
#define KINFU_ROS_MESSAGE_GETTSDFRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <kinfu_ros/TSDF.h>

namespace kinfu_ros
{
template <class ContainerAllocator>
struct GetTSDFResponse_
{
  typedef GetTSDFResponse_<ContainerAllocator> Type;

  GetTSDFResponse_()
    : tsdf()  {
    }
  GetTSDFResponse_(const ContainerAllocator& _alloc)
    : tsdf(_alloc)  {
  (void)_alloc;
    }



   typedef  ::kinfu_ros::TSDF_<ContainerAllocator>  _tsdf_type;
  _tsdf_type tsdf;





  typedef boost::shared_ptr< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetTSDFResponse_

typedef ::kinfu_ros::GetTSDFResponse_<std::allocator<void> > GetTSDFResponse;

typedef boost::shared_ptr< ::kinfu_ros::GetTSDFResponse > GetTSDFResponsePtr;
typedef boost::shared_ptr< ::kinfu_ros::GetTSDFResponse const> GetTSDFResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace kinfu_ros

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'kinfu_ros': ['/home/karo/Desktop/DeepLeaveSegmentation/catkin_ws/src/kinfu_ros-master/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5396807193e5f6302680576158283a3a";
  }

  static const char* value(const ::kinfu_ros::GetTSDFResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5396807193e5f630ULL;
  static const uint64_t static_value2 = 0x2680576158283a3aULL;
};

template<class ContainerAllocator>
struct DataType< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "kinfu_ros/GetTSDFResponse";
  }

  static const char* value(const ::kinfu_ros::GetTSDFResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "TSDF tsdf\n\
\n\
\n\
================================================================================\n\
MSG: kinfu_ros/TSDF\n\
Header header\n\
\n\
#Volume dimension, in meters\n\
float32 size_x\n\
float32 size_y\n\
float32 size_z\n\
\n\
#number of voxels in each dimension\n\
int32 num_voxels_x\n\
int32 num_voxels_y\n\
int32 num_voxels_z\n\
\n\
#Truncation distance, in meters\n\
float32 truncation_dist\n\
\n\
#Maximum tsdf weight\n\
int32 max_weight\n\
\n\
#Pose of the TSDF with respect to the camera origin\n\
geometry_msgs/Pose pose\n\
\n\
#Binary serialization of distances/weights. \n\
# The first 16 bits are a half-precision floating point value representing the TSDF. The second 16 bits are\n\
# an unsigned 16 bit weight value.\n\
uint32[] data\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of position and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::kinfu_ros::GetTSDFResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.tsdf);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetTSDFResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::kinfu_ros::GetTSDFResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::kinfu_ros::GetTSDFResponse_<ContainerAllocator>& v)
  {
    s << indent << "tsdf: ";
    s << std::endl;
    Printer< ::kinfu_ros::TSDF_<ContainerAllocator> >::stream(s, indent + "  ", v.tsdf);
  }
};

} // namespace message_operations
} // namespace ros

#endif // KINFU_ROS_MESSAGE_GETTSDFRESPONSE_H
