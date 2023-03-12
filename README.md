# PathPlaning
Using Informed RRT* algorithm to find optimal path from start node to end node for a predefined map. Simulating turtlebot-3 to reach the end node following the generated path using ROS, RViz and Gazebo.

## Steps to clone and setup the project
```
git clone https://github.com/Rishabh96M/PathPlaning.git
```
copy the assignment.launch file in the <catkin_ws>/src/turtlebot3_simulations/turtlebot3_gazebo/launch folder <br>
copy the map.world file in the <catkin_ws>/src/turtlebot3_simulations/turtlebot3_gazebo/world folder <br>

build the catkin-ws
```
cd <catkin_ws>
catkin_make
```

In a terminal run the turtlebot3 in the world
```
roslaunch turtlebot3_gazebo assignment.launch
```

In a new terminal run the Informed RRT star algorithm
```
cd PathPlaning
python3 informed_rrt_star.py
```

To see the simulation, close the matplotlib screen after the plotting is complete.<br>
You will be notified on the terminal after the simulation is completed.<br>
<br>
**Videos** folder contains two test videos of the working project<br>
test1.mp4 - start point = 60,10 - end point = 80,80 <br>
test2.mp4 - start point = 30,50 - end point = 90,90
