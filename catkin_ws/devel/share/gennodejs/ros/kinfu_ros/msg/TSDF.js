// Auto-generated. Do not edit!

// (in-package kinfu_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class TSDF {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.size_x = null;
      this.size_y = null;
      this.size_z = null;
      this.num_voxels_x = null;
      this.num_voxels_y = null;
      this.num_voxels_z = null;
      this.truncation_dist = null;
      this.max_weight = null;
      this.pose = null;
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('size_x')) {
        this.size_x = initObj.size_x
      }
      else {
        this.size_x = 0.0;
      }
      if (initObj.hasOwnProperty('size_y')) {
        this.size_y = initObj.size_y
      }
      else {
        this.size_y = 0.0;
      }
      if (initObj.hasOwnProperty('size_z')) {
        this.size_z = initObj.size_z
      }
      else {
        this.size_z = 0.0;
      }
      if (initObj.hasOwnProperty('num_voxels_x')) {
        this.num_voxels_x = initObj.num_voxels_x
      }
      else {
        this.num_voxels_x = 0;
      }
      if (initObj.hasOwnProperty('num_voxels_y')) {
        this.num_voxels_y = initObj.num_voxels_y
      }
      else {
        this.num_voxels_y = 0;
      }
      if (initObj.hasOwnProperty('num_voxels_z')) {
        this.num_voxels_z = initObj.num_voxels_z
      }
      else {
        this.num_voxels_z = 0;
      }
      if (initObj.hasOwnProperty('truncation_dist')) {
        this.truncation_dist = initObj.truncation_dist
      }
      else {
        this.truncation_dist = 0.0;
      }
      if (initObj.hasOwnProperty('max_weight')) {
        this.max_weight = initObj.max_weight
      }
      else {
        this.max_weight = 0;
      }
      if (initObj.hasOwnProperty('pose')) {
        this.pose = initObj.pose
      }
      else {
        this.pose = new geometry_msgs.msg.Pose();
      }
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TSDF
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [size_x]
    bufferOffset = _serializer.float32(obj.size_x, buffer, bufferOffset);
    // Serialize message field [size_y]
    bufferOffset = _serializer.float32(obj.size_y, buffer, bufferOffset);
    // Serialize message field [size_z]
    bufferOffset = _serializer.float32(obj.size_z, buffer, bufferOffset);
    // Serialize message field [num_voxels_x]
    bufferOffset = _serializer.int32(obj.num_voxels_x, buffer, bufferOffset);
    // Serialize message field [num_voxels_y]
    bufferOffset = _serializer.int32(obj.num_voxels_y, buffer, bufferOffset);
    // Serialize message field [num_voxels_z]
    bufferOffset = _serializer.int32(obj.num_voxels_z, buffer, bufferOffset);
    // Serialize message field [truncation_dist]
    bufferOffset = _serializer.float32(obj.truncation_dist, buffer, bufferOffset);
    // Serialize message field [max_weight]
    bufferOffset = _serializer.int32(obj.max_weight, buffer, bufferOffset);
    // Serialize message field [pose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.pose, buffer, bufferOffset);
    // Serialize message field [data]
    bufferOffset = _arraySerializer.uint32(obj.data, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TSDF
    let len;
    let data = new TSDF(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [size_x]
    data.size_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [size_y]
    data.size_y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [size_z]
    data.size_z = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [num_voxels_x]
    data.num_voxels_x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [num_voxels_y]
    data.num_voxels_y = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [num_voxels_z]
    data.num_voxels_z = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [truncation_dist]
    data.truncation_dist = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [max_weight]
    data.max_weight = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [pose]
    data.pose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    // Deserialize message field [data]
    data.data = _arrayDeserializer.uint32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 4 * object.data.length;
    return length + 92;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kinfu_ros/TSDF';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '36b8bc6c23079034a0c8fa5f89593482';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TSDF(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.size_x !== undefined) {
      resolved.size_x = msg.size_x;
    }
    else {
      resolved.size_x = 0.0
    }

    if (msg.size_y !== undefined) {
      resolved.size_y = msg.size_y;
    }
    else {
      resolved.size_y = 0.0
    }

    if (msg.size_z !== undefined) {
      resolved.size_z = msg.size_z;
    }
    else {
      resolved.size_z = 0.0
    }

    if (msg.num_voxels_x !== undefined) {
      resolved.num_voxels_x = msg.num_voxels_x;
    }
    else {
      resolved.num_voxels_x = 0
    }

    if (msg.num_voxels_y !== undefined) {
      resolved.num_voxels_y = msg.num_voxels_y;
    }
    else {
      resolved.num_voxels_y = 0
    }

    if (msg.num_voxels_z !== undefined) {
      resolved.num_voxels_z = msg.num_voxels_z;
    }
    else {
      resolved.num_voxels_z = 0
    }

    if (msg.truncation_dist !== undefined) {
      resolved.truncation_dist = msg.truncation_dist;
    }
    else {
      resolved.truncation_dist = 0.0
    }

    if (msg.max_weight !== undefined) {
      resolved.max_weight = msg.max_weight;
    }
    else {
      resolved.max_weight = 0
    }

    if (msg.pose !== undefined) {
      resolved.pose = geometry_msgs.msg.Pose.Resolve(msg.pose)
    }
    else {
      resolved.pose = new geometry_msgs.msg.Pose()
    }

    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = []
    }

    return resolved;
    }
};

module.exports = TSDF;
