; Auto-generated. Do not edit!


(cl:in-package kinfu_ros-msg)


;//! \htmlinclude TSDF.msg.html

(cl:defclass <TSDF> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (size_x
    :reader size_x
    :initarg :size_x
    :type cl:float
    :initform 0.0)
   (size_y
    :reader size_y
    :initarg :size_y
    :type cl:float
    :initform 0.0)
   (size_z
    :reader size_z
    :initarg :size_z
    :type cl:float
    :initform 0.0)
   (num_voxels_x
    :reader num_voxels_x
    :initarg :num_voxels_x
    :type cl:integer
    :initform 0)
   (num_voxels_y
    :reader num_voxels_y
    :initarg :num_voxels_y
    :type cl:integer
    :initform 0)
   (num_voxels_z
    :reader num_voxels_z
    :initarg :num_voxels_z
    :type cl:integer
    :initform 0)
   (truncation_dist
    :reader truncation_dist
    :initarg :truncation_dist
    :type cl:float
    :initform 0.0)
   (max_weight
    :reader max_weight
    :initarg :max_weight
    :type cl:integer
    :initform 0)
   (pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (data
    :reader data
    :initarg :data
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass TSDF (<TSDF>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TSDF>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TSDF)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kinfu_ros-msg:<TSDF> is deprecated: use kinfu_ros-msg:TSDF instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:header-val is deprecated.  Use kinfu_ros-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'size_x-val :lambda-list '(m))
(cl:defmethod size_x-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:size_x-val is deprecated.  Use kinfu_ros-msg:size_x instead.")
  (size_x m))

(cl:ensure-generic-function 'size_y-val :lambda-list '(m))
(cl:defmethod size_y-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:size_y-val is deprecated.  Use kinfu_ros-msg:size_y instead.")
  (size_y m))

(cl:ensure-generic-function 'size_z-val :lambda-list '(m))
(cl:defmethod size_z-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:size_z-val is deprecated.  Use kinfu_ros-msg:size_z instead.")
  (size_z m))

(cl:ensure-generic-function 'num_voxels_x-val :lambda-list '(m))
(cl:defmethod num_voxels_x-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:num_voxels_x-val is deprecated.  Use kinfu_ros-msg:num_voxels_x instead.")
  (num_voxels_x m))

(cl:ensure-generic-function 'num_voxels_y-val :lambda-list '(m))
(cl:defmethod num_voxels_y-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:num_voxels_y-val is deprecated.  Use kinfu_ros-msg:num_voxels_y instead.")
  (num_voxels_y m))

(cl:ensure-generic-function 'num_voxels_z-val :lambda-list '(m))
(cl:defmethod num_voxels_z-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:num_voxels_z-val is deprecated.  Use kinfu_ros-msg:num_voxels_z instead.")
  (num_voxels_z m))

(cl:ensure-generic-function 'truncation_dist-val :lambda-list '(m))
(cl:defmethod truncation_dist-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:truncation_dist-val is deprecated.  Use kinfu_ros-msg:truncation_dist instead.")
  (truncation_dist m))

(cl:ensure-generic-function 'max_weight-val :lambda-list '(m))
(cl:defmethod max_weight-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:max_weight-val is deprecated.  Use kinfu_ros-msg:max_weight instead.")
  (max_weight m))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:pose-val is deprecated.  Use kinfu_ros-msg:pose instead.")
  (pose m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <TSDF>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinfu_ros-msg:data-val is deprecated.  Use kinfu_ros-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TSDF>) ostream)
  "Serializes a message object of type '<TSDF>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'size_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'size_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'size_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'num_voxels_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'num_voxels_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'num_voxels_z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'truncation_dist))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'max_weight)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TSDF>) istream)
  "Deserializes a message object of type '<TSDF>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'size_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'size_y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'size_z) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_voxels_x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_voxels_y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_voxels_z) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'truncation_dist) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'max_weight) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TSDF>)))
  "Returns string type for a message object of type '<TSDF>"
  "kinfu_ros/TSDF")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TSDF)))
  "Returns string type for a message object of type 'TSDF"
  "kinfu_ros/TSDF")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TSDF>)))
  "Returns md5sum for a message object of type '<TSDF>"
  "36b8bc6c23079034a0c8fa5f89593482")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TSDF)))
  "Returns md5sum for a message object of type 'TSDF"
  "36b8bc6c23079034a0c8fa5f89593482")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TSDF>)))
  "Returns full string definition for message of type '<TSDF>"
  (cl:format cl:nil "Header header~%~%#Volume dimension, in meters~%float32 size_x~%float32 size_y~%float32 size_z~%~%#number of voxels in each dimension~%int32 num_voxels_x~%int32 num_voxels_y~%int32 num_voxels_z~%~%#Truncation distance, in meters~%float32 truncation_dist~%~%#Maximum tsdf weight~%int32 max_weight~%~%#Pose of the TSDF with respect to the camera origin~%geometry_msgs/Pose pose~%~%#Binary serialization of distances/weights. ~%# The first 16 bits are a half-precision floating point value representing the TSDF. The second 16 bits are~%# an unsigned 16 bit weight value.~%uint32[] data~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TSDF)))
  "Returns full string definition for message of type 'TSDF"
  (cl:format cl:nil "Header header~%~%#Volume dimension, in meters~%float32 size_x~%float32 size_y~%float32 size_z~%~%#number of voxels in each dimension~%int32 num_voxels_x~%int32 num_voxels_y~%int32 num_voxels_z~%~%#Truncation distance, in meters~%float32 truncation_dist~%~%#Maximum tsdf weight~%int32 max_weight~%~%#Pose of the TSDF with respect to the camera origin~%geometry_msgs/Pose pose~%~%#Binary serialization of distances/weights. ~%# The first 16 bits are a half-precision floating point value representing the TSDF. The second 16 bits are~%# an unsigned 16 bit weight value.~%uint32[] data~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TSDF>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
     4
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TSDF>))
  "Converts a ROS message object to a list"
  (cl:list 'TSDF
    (cl:cons ':header (header msg))
    (cl:cons ':size_x (size_x msg))
    (cl:cons ':size_y (size_y msg))
    (cl:cons ':size_z (size_z msg))
    (cl:cons ':num_voxels_x (num_voxels_x msg))
    (cl:cons ':num_voxels_y (num_voxels_y msg))
    (cl:cons ':num_voxels_z (num_voxels_z msg))
    (cl:cons ':truncation_dist (truncation_dist msg))
    (cl:cons ':max_weight (max_weight msg))
    (cl:cons ':pose (pose msg))
    (cl:cons ':data (data msg))
))
