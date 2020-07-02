// Auto-generated. Do not edit!

// (in-package kinfu_ros.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

let TSDF = require('../msg/TSDF.js');

//-----------------------------------------------------------

class GetTSDFRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetTSDFRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetTSDFRequest
    let len;
    let data = new GetTSDFRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'kinfu_ros/GetTSDFRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetTSDFRequest(null);
    return resolved;
    }
};

class GetTSDFResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.tsdf = null;
    }
    else {
      if (initObj.hasOwnProperty('tsdf')) {
        this.tsdf = initObj.tsdf
      }
      else {
        this.tsdf = new TSDF();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetTSDFResponse
    // Serialize message field [tsdf]
    bufferOffset = TSDF.serialize(obj.tsdf, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetTSDFResponse
    let len;
    let data = new GetTSDFResponse(null);
    // Deserialize message field [tsdf]
    data.tsdf = TSDF.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += TSDF.getMessageSize(object.tsdf);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'kinfu_ros/GetTSDFResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5396807193e5f6302680576158283a3a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    TSDF tsdf
    
    
    ================================================================================
    MSG: kinfu_ros/TSDF
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
    const resolved = new GetTSDFResponse(null);
    if (msg.tsdf !== undefined) {
      resolved.tsdf = TSDF.Resolve(msg.tsdf)
    }
    else {
      resolved.tsdf = new TSDF()
    }

    return resolved;
    }
};

module.exports = {
  Request: GetTSDFRequest,
  Response: GetTSDFResponse,
  md5sum() { return '5396807193e5f6302680576158283a3a'; },
  datatype() { return 'kinfu_ros/GetTSDF'; }
};
