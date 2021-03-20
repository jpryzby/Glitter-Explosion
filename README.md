# Glitter-Explosion

Made by: Jon Pryzby
Last Updated: 3/19/2021
Primary language: Python

##################################################################
###                                                            ###
###  Run this program at https://trinket.io/python/5c4ad1b6fb  ###
###                                                            ###
##################################################################

A colorful explosion made with the python turtle package. 

A class "glitt" is declared as a circle of some color, with some x and y coordinates, and some x and y velocity. All glitts are stored in an array and, once per game tick, their coordinates are changed based on their velocities, and a physics function.

A glitt is launched into the air. at the moment it reaches y=0, 100 new glitts are spawned, each with a random color, x velocity, and y velocity, resulting in a color explosion.