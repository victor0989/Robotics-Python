#1. Let’s assume we have three coordinate systems in our application. (displayed with a green and blue line) prbt_base is the default coordinate system. It was used in the previous sections.
#The prbt_tcp frame is the current position of the gripper.#The third frame pallet is supposed to be an edge of a product 
#tray that we placed somewhere in the robot environment. We then have three possible frames, we can choose to execute our goal 
#in the image above we displayed three move commands. All three commands move the robot to position x = y = 0 and z = 0.2, 
#but use the different frames as reference.
goal=Pose(position=Point(0, 0, 0.2))) or goal=Pose(position=Point(0, 0, 0.2)), reference_frame=”prbt_base”)
goal=Pose(position=Point(0, 0, 0.2)), reference_frame=”prbt_tcp”)
goal=Pose(position=Point(0, 0, 0.2)), reference_frame=”pallet”)
#When adding the relative flag additionally, the goal will be added to the current tcp pose using the chosen frame. 
#This results in the tcp moving in different directions depending on which frame we used.
#In this case we just added the relative flag to the previous goals.
goal=position=Point(0, 0, 0.2)), relative=True)
goal=position=Point(0, 0, 0.2)), reference_frame=”prbt_tcp”, relative=True)
goal=position=Point(0, 0, 0.2)), reference_frame=”pallet”, relative=True)
#As can be seen above, the relative movement used the z axis of the chosen reference frame, which resulted in different movements 
#of the tcp, except for the tcp frame itself. In the case of the tcp frame, relative and absolute movement is the same.
#To get the robot in a position similar to the robot in this image we could use a move command with a custom reference_frame.
r.move(Ptp(goal=[0.1, -0.05, 0.2, 2.3561, 0, 0], reference_frame="pallet"))
#This would result in a scene, that looks somewhat like the image above. 
#(The Rotation around the x axis is necessary to reach the current tcp rotation)
#The next commands in the sequence will be:
#close in to grab the object, move straight up to lift it
#move to the next object
#For the first task we can easily use the tcp ref, since its rotation already fits our goal.
r.move(Ptp(goal=position=Point(0, 0, 0.1)), reference_frame="prbt_tcp"))
