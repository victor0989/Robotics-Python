#Move
r.move(Ptp(goal=[0, 0.5, 0.5, 0, 0, 0]))
r.move(Lin(goal=Pose(position=Point(0.2, 0, 0.8))))
r.move(Circ(goal=Pose(position=Point(0.2, 0.2, 0.8)), center=Point(0.3, 0.1, 0.8)))
#The move() function is the most important part of the robot API. With the help of the move() function the user can execute the different robot motion commands, like shown for Ptp, Lin and Circ.

#All cartesian goals are interpreted as poses of the tool center point (TCP) link. The transformation between the TCP link 
#and the last robot link can be adjusted through the tcp_offset_xyz and tcp_offset_rpy parameters in prbt.xacro.

#Move failure
try:
    r.move(Ptp(goal=[0, 10.0, 0, 0, 0, 0]))
except RobotMoveFailed:
    rospy.loginfo("Ptp command did fail as expected.")
#In case a robot motion command fails during the execution, the move() function throws an RobotMoveFailed exception 
#which can be caught using standard python mechanisms.

#The goal: Joint vs. Cartesian space
r.move(Ptp(goal=[0, 0.5, 0.5, 0, 0, 0]))
r.move(Lin(goal=Pose(position=Point(-0.2, -0.2, 0.6), orientation=from_euler(0.1, 0, 0))))
The goal pose for Ptp and Lin commands can be stated either in joint space or in Cartesian space.

r.move(Circ(goal=Pose(position=Point(0.2, 0.2, 0.8)), center=Point(0.3, 0.1, 0.8)))
#The goal and the auxiliary pose of Circ commands have to be stated in Cartesian space.

#Relative commands
r.move(Ptp(goal=[0.1, 0, 0, 0, 0, 0], relative=True))
r.move(Lin(goal=Pose(position=Point(0, -0.2, -0.2)), relative=True))
#Ptp and Lin commands can also be stated as relative commands indicated by the argument relative=True. Relative commands state the goal as offset relative to the current robot position. As long as no custom reference 
#frame is set, the offset has to be stated with regard to the base coordinate system. 
#The orientation is added as offset to the euler-angles.#
Custom Reference Frame
r.move(Ptp(goal=Pose(position=Point(0, 0, 0.1)), reference_frame="prbt_tcp"))
r.move(Ptp(goal=Pose(position=Point(0, -0.1, 0)), reference_frame="prbt_link_3", relative=True))
#All three move classes Ptp, Lin and Circ can be executed within a custom reference frame. In this case, the passed goal pose will be seen relative to this coordinate system instead of the default system: prbt_base
#The custom reference frame argument (reference_frame="target_frame") has to be a valid tf frame id 
#and can be paired with the relative command. 
#When paired with relative flag, the goal will be applied to the current robot pose in this custom reference frame.
#<img src="https://docs.ros.org/en/kinetic/api/pilz_robot_programming/html/_images/tfs.png" alt="_images/tfs.png"/>
