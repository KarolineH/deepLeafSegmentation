# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kinfu_ros/TSDF.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class TSDF(genpy.Message):
  _md5sum = "36b8bc6c23079034a0c8fa5f89593482"
  _type = "kinfu_ros/TSDF"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

#Volume dimension, in meters
float32 size_x
float32 size_y
float32 size_z

#number of voxels in each dimension
int32 num_voxels_x
int32 num_voxels_y
int32 num_voxels_z

#Truncation distance, in meters
float32 truncation_dist

#Maximum tsdf weight
int32 max_weight

#Pose of the TSDF with respect to the camera origin
geometry_msgs/Pose pose

#Binary serialization of distances/weights. 
# The first 16 bits are a half-precision floating point value representing the TSDF. The second 16 bits are
# an unsigned 16 bit weight value.
uint32[] data
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','size_x','size_y','size_z','num_voxels_x','num_voxels_y','num_voxels_z','truncation_dist','max_weight','pose','data']
  _slot_types = ['std_msgs/Header','float32','float32','float32','int32','int32','int32','float32','int32','geometry_msgs/Pose','uint32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,size_x,size_y,size_z,num_voxels_x,num_voxels_y,num_voxels_z,truncation_dist,max_weight,pose,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TSDF, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.size_x is None:
        self.size_x = 0.
      if self.size_y is None:
        self.size_y = 0.
      if self.size_z is None:
        self.size_z = 0.
      if self.num_voxels_x is None:
        self.num_voxels_x = 0
      if self.num_voxels_y is None:
        self.num_voxels_y = 0
      if self.num_voxels_z is None:
        self.num_voxels_z = 0
      if self.truncation_dist is None:
        self.truncation_dist = 0.
      if self.max_weight is None:
        self.max_weight = 0
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.data is None:
        self.data = []
    else:
      self.header = std_msgs.msg.Header()
      self.size_x = 0.
      self.size_y = 0.
      self.size_z = 0.
      self.num_voxels_x = 0
      self.num_voxels_y = 0
      self.num_voxels_z = 0
      self.truncation_dist = 0.
      self.max_weight = 0
      self.pose = geometry_msgs.msg.Pose()
      self.data = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3f3ifi7d().pack(_x.size_x, _x.size_y, _x.size_z, _x.num_voxels_x, _x.num_voxels_y, _x.num_voxels_z, _x.truncation_dist, _x.max_weight, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 88
      (_x.size_x, _x.size_y, _x.size_z, _x.num_voxels_x, _x.num_voxels_y, _x.num_voxels_z, _x.truncation_dist, _x.max_weight, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w,) = _get_struct_3f3ifi7d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.data = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3f3ifi7d().pack(_x.size_x, _x.size_y, _x.size_z, _x.num_voxels_x, _x.num_voxels_y, _x.num_voxels_z, _x.truncation_dist, _x.max_weight, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.data.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 88
      (_x.size_x, _x.size_y, _x.size_z, _x.num_voxels_x, _x.num_voxels_y, _x.num_voxels_z, _x.truncation_dist, _x.max_weight, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w,) = _get_struct_3f3ifi7d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.data = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3f3ifi7d = None
def _get_struct_3f3ifi7d():
    global _struct_3f3ifi7d
    if _struct_3f3ifi7d is None:
        _struct_3f3ifi7d = struct.Struct("<3f3ifi7d")
    return _struct_3f3ifi7d
