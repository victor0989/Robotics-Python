
from geometry_msgs.msg import Point
from pilz_robot_programming.robot import *
from pilz_robot_programming.commands import *
import math
import rospy

__REQUIRED_API_VERSION__ = "1"


def start_program():
    print("Executing " + __file__)

    r = Robot(__REQUIRED_API_VERSION__)

    # Simple ptp movement
    r.move(Ptp(goal=[0, 0.5, 0.5, 0, 0, 0], vel_scale=0.4))

    start_joint_values = r.get_current_joint_states()

    # Relative ptp movement
    r.move(Ptp(goal=[0.1, 0, 0, 0, 0, 0], relative=True, vel_scale=0.2))
    r.move(Ptp(goal=Pose(position=Point(0, 0, -0.1)), relative=True))
    r.move(Ptp(goal=[-0.2, 0, 0, 0, 0, 0], relative=True, acc_scale=0.2))

    pose_after_relative = r.get_current_pose()

    # Simple Lin movement
    r.move(Lin(goal=Pose(position=Point(0.2, 0, 0.8)), vel_scale=0.1, acc_scale=0.1))

    # Relative Lin movement
    r.move(Lin(goal=Pose(position=Point(0, -0.2, 0), orientation=from_euler(0, 0, math.radians(15))), relative=True,
           vel_scale=0.1, acc_scale=0.1))
    r.move(Lin(goal=Pose(position=Point(0, 0.2, 0)), relative=True,
           vel_scale=0.1, acc_scale=0.1))

    # Circ movement
    r.move(Circ(goal=Pose(position=Point(0.2, -0.2, 0.8)), center=Point(0.1, -0.1, 0.8), acc_scale=0.4))

    # Move robot with stored pose
    r.move(Ptp(goal=pose_after_relative, vel_scale=0.2))

    # Repeat the previous steps with a sequence command
    sequence = Sequence()
    sequence.append(Lin(goal=Pose(position=Point(0.2, 0, 0.8)), vel_scale=0.1, acc_scale=0.1))
    sequence.append(Circ(goal=Pose(position=Point(0.2, -0.2, 0.8)), center=Point(0.1, -0.1, 0.8), acc_scale=0.4))
    sequence.append(Ptp(goal=pose_after_relative, vel_scale=0.2))

    r.move(sequence)

    # Move to start goal for sequence demonstration
    r.move(Ptp(goal=start_joint_values))

    # Blend sequence
    blend_sequence = Sequence()
    blend_sequence.append(Lin(goal=Pose(position=Point(0.2, 0, 0.7))), blend_radius=0.01)
    blend_sequence.append(Lin(goal=Pose(position=Point(0.2, 0.1, 0.7))))

    r.move(blend_sequence)

    # Move with custom reference frame
    r.move(Ptp(goal=Pose(position=Point(0, 0, 0.1)), reference_frame="prbt_tcp"))
    r.move(Ptp(goal=Pose(position=Point(0, -0.1, 0)), reference_frame="prbt_link_3", relative=True))

    # Create and execute an invalid ptp command with out of bound joint values
    try:
        r.move(Ptp(goal=[0, 10.0, 0, 0, 0, 0]))
    except RobotMoveFailed:
        rospy.loginfo("Ptp command did fail as expected.")


if __name__ == "__main__":
    # Init a ros node
    rospy.init_node('robot_program_node')

    start_program()
