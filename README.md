# Robotics-Python
# Machine learning models

# Machine learning research for robotics and mathematics

#In this document are the main objetives of the project
-BUILD MODELS FOR DATA ANALYSIS
-CALCULATE ERRORS WITH MODELS
-MACHINE LEARNING RESEARCH
-DATA MODELING

#DOCUMENTATION FOR ROBOTICS:
(PYDY)
https://pydy.readthedocs.io/en/stable/models.html
(PYBOTICS)
https://github.com/engnadeau/pybotics/blob/master/examples/dynamics.ipynb

#EXAMPLE
Create the Robot Model
from pybotics.robot import Robot
from pybotics.predefined_models import ur10

robot = Robot.from_parameters(ur10())
Define the Forces/Torques Acting on the TCP

#Calculate Joint Torques
What are the joint torques required to counteract this payload?
This calculation can be repeated at each discrete pose in a trajectory for trajectory dynamics
