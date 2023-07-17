# Robotics-Python
# Machine learning models

# Machine learning research for robotics and mathematics

#In this document are the main objetives of the project
-build models 
-calculate errors
-machine learning research


#Documentation for robotics research:
(PYDY)
https://pydy.readthedocs.io/en/stable/models.html
(PYBOTICS)
https://github.com/engnadeau/pybotics/blob/master/examples/dynamics.ipynb

#EXAMPLES
Create the Robot Model
from pybotics.robot import Robot
from pybotics.predefined_models import ur10

robot = Robot.from_parameters(ur10())
Define the Forces/Torques Acting on the TCP

#Calculate Joint Torques
What are the joint torques required to counteract this payload?
This calculation can be repeated at each discrete pose in a trajectory for trajectory dynamics
The degrees of freedom of the system are n + 1, i.e. one for each pendulum link and one for the lateral motion of the cart.

M x’ = F, where x = [u0, …, un+1, q0, …, qn+1]

The joint angles are all defined relative to the ground where the x axis defines the ground line and the y axis points up. The joint torques are applied between each adjacent link and the between the cart and the lower link where a positive torque corresponds to positive angle.

forces = [0, 0, 10]
torques = [0, 0, 0]
wrench = [*forces, *torques]

