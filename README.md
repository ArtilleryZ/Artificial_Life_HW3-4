# Artificial_Life_HW3-4

This is the combination of HW3 and HW4 as I made it randomly generate branches and leaves while using functions to create the xml file.  

Now, it will create left branch with uniform(-1.3, -1) and right branch of uniform(-1.1, -0.8)  
Then, it will add a new left branch with an increment in z of uniform(0.4, 0.6) from the last right branch. The same process is for the new right branch.  

Leaves will be generated randomly on the branch with random x_pos(which determines if the leaf is on the top or the bottom of the branch), and random z_pos(which determines the distance from the center of the branch).  

The motion of leaves is the same in hw2, which is just a random pick from a cosine wave.  

To run this, run `hw4_xml_generator.py` first and it will create a xml file called `hw4.xml`, then use `hw4.py` to visualize the result.
