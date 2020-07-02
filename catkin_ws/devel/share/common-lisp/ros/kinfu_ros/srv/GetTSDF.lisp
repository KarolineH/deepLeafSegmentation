; Auto-generated. Do not edit!


(cl:in-package kinfu_ros-srv)


;//! \htmlinclude GetTSDF-request.msg.html

(cl:defclass <GetTSDF-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass GetTSDF-request (<GetTSDF-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetTSDF-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetTSDF-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kinfu_ros-srv:<GetTSDF-request> is deprecated: use kinfu_ros-srv:GetTSDF-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetTSDF-request>) ostream)
  "Serializes a message object of type '<GetTSDF-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetTSDF-request>) istream)
  "Deserializes a message object of type '<GetTSDF-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetTSDF-request>)))
  "Returns string type for a service object of type '<GetTSDF-request>"
  "kinfu_ros/GetTSDFRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetTSDF-request)))
  "Returns string type for a service object of type 'GetTSDF-request"
  "kinfu_ros/GetTSDFRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetTSDF-request>)))
  "Returns md5sum for a message object of type '<GetTSDF-request>"
  "5396807193e5f6302680576158283a3a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetTSDF-request)))
  "Returns md5sum for a message object of type 'GetTSDF-request"
  "5396807193e5f6302680576158283a3a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetTSDF-request>)))
  "Returns full string definition for message of type '<GetTSDF-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetTSDF-request)))
  "Returns full string definition for message of type 'GetTSDF-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetTSDF-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetTSDF-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GetTSDF-request
))
;//! \htmlinclude GetTSDF-response.msg.html

(cl:defclass <GetTSDF-response> (roslisp-msg-protocol:ros-message)
  ((tsdf
    :reader tsdf
    :initarg :tsdf
    :type kinfu_ros-msg:TSDF
    :initform (cl:make-instance 'kinfu_ros-msg:TSDF)))
)

(cl:defclass GetTSDF-response (<GetTSDF-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetTSDF-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetTSDF-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kinfu_ros-srv:<GetTSDF-response> is deprecated: use kinfu_ros-srv:GetTSDF-response instead.")))

(cl:ensure-generic-function 'tsdf-val :lambda-list '(m))
(cl:defmethod tsdf-val ((m <GetTSDF-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-srv:tsdf-val is deprecated.  Use kinfu_ros-srv:tsdf instead.")
  (tsdf m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetTSDF-response>) ostream)
  "Serializes a message object of type '<GetTSDF-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'tsdf) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetTSDF-response>) istream)
  "Deserializes a message object of type '<GetTSDF-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'tsdf) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetTSDF-response>)))
  "Returns string type for a service object of type '<GetTSDF-response>"
  "kinfu_ros/GetTSDFResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetTSDF-response)))
  "Returns string type for a service object of type 'GetTSDF-response"
  "kinfu_ros/GetTSDFResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetTSDF-response>)))
  "Returns md5sum for a message object of type '<GetTSDF-response>"
  "5396807193e5f6302680576158283a3a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetTSDF-response)))
  "Returns md5sum for a message object of type 'GetTSDF-response"
  "5396807193e5f6302680576158283a3a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetTSDF-response>)))
  "Returns full string definition for message of type '<GetTSDF-response>"
  (cl:format cl:nil "TSDF tsdf~%~%~%================================================================================~%MSG: kinfu_ros/TSDF~%Header header~%~%#Volume dimension, in meters~%float32 size_x~%float32 size_y~%float32 size_z~%~%#number of voxels in each dimension~%int32 num_voxels_x~%int32 num_voxels_y~%int32 num_voxels_z~%~%#Truncation distance, in meters~%float32 truncation_dist~%~%#Maximum tsdf weight~%int32 max_weight~%~%#Pose of the TSDF with respect to the camera origin~%geometry_msgs/Pose pose~%~%#Binary serialization of distances/weights. ~%# The first 16 bits are a half-precision floating point value representing the TSDF. The second 16 bits are~%# an unsigned 16 bit weight value.~%uint32[] data~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetTSDF-response)))
  "Returns full string definition for message of type 'GetTSDF-response"
  (cl:format cl:nil "TSDF tsdf~%~%~%================================================================================~%MSG: kinfu_ros/TSDF~%Header header~%~%#Volume dimension, in meters~%float32 size_x~%float32 size_y~%float32 size_z~%~%#number of voxels in each dimension~%int32 num_voxels_x~%int32 num_voxels_y~%int32 num_voxels_z~%~%#Truncation distance, in meters~%float32 truncation_dist~%~%#Maximum tsdf weight~%int32 max_weight~%~%#Pose of the TSDF with respect to the camera origin~%geometry_msgs/Pose pose~%~%#Binary serialization of distances/weights. ~%# The first 16 bits are a half-precision floating point value representing the TSDF. The second 16 bits are~%# an unsigned 16 bit weight value.~%uint32[] data~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetTSDF-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'tsdf))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetTSDF-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GetTSDF-response
    (cl:cons ':tsdf (tsdf msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GetTSDF)))
  'GetTSDF-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GetTSDF)))
  'GetTSDF-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetTSDF)))
  "Returns string type for a service object of type '<GetTSDF>"
  "kinfu_ros/GetTSDF")