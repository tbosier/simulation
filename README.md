# Truck Breakdown Simulator

The purpose of this simulation model is to serve as a study of the SimPy library. I am fascinated by simulation and the power that it holds across a breadth of industries.

# How this simulator works

In its cold-start state, I take a static number of trucks, assign them number of miles driven in a week and increase their probability of break down by 1%. I assign a static cost of breakdown, and the truck resets its probability of breaking down. 

# Things to do

This would be better if it achieved the following
* Rather than have a static number of trucks, assign a mileage to them already and say they retire at 500,000 miles
* Assign a number of trucks we wish to keep
* Assign a probability distribution to the cost associated to breaking down rather than having a static number
* Assign a better probability of break down and a probability increase as each week passes, based on mileage