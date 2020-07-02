
(cl:in-package :asdf)

(defsystem "kinfu_ros-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :kinfu_ros-msg
)
  :components ((:file "_package")
    (:file "GetTSDF" :depends-on ("_package_GetTSDF"))
    (:file "_package_GetTSDF" :depends-on ("_package"))
  ))