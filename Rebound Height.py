'''Rebound Height
Daniel has a bsll. He wants to find the ball's rebound height, which he dropped from height H with an initial velocity V. After the Nth rebound the final velocity of the ball is Vn YOur task is to help him find and return an integer an integer value representing the height to which the ball rebounds after N bounces.
Note:
H' = H*e^2n where H' is the rebound height H is the initial height e is the coefficient of restitution and is the number of bounces.
e^n = V/Vn, where V is the initial velocity and Vn is the final velocity

Input Specification:
input1:An integer H, representing initial height
input2:An integer V, representing initial velocity
input3:An integer Vn, representing final velocity

Output Specification:Return an integer value representing the height to which the ball rebounds after N bounces

Example:
input1:10
input2:20
input3:5

Output:160
'''
def rebound_height(H, V, Vn):
    e_squared = (V / Vn) ** 2
    
    rebound_height = int(H * e_squared)
    return rebound_height

H = 10
V = 20
Vn = 5
print(rebound_height(H, V, Vn))  

