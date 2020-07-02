
(cl:in-package :asdf)

(defsystem "kinfu_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "TSDF" :depends-on ("_package_TSDF"))
    (:file "_package_TSDF" :depends-on ("_package"))
  ))