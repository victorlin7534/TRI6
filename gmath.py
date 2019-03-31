import math
from display import *


#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    mag = math.sqrt(vector[0]**2 + vector[1]**2 +vector[2]**2)
    return [vector[0]/mag,vector[1]/mag,vector[2]/mag]

#Return the dot porduct of a . b
def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def norm(polygons, index):
    vec1 = [polygons[index+1][0]-polygons[index][0],polygons[index+1][1]-polygons[index][1],polygons[index+1][2]-polygons[index][2]]
    vec2 = [polygons[index+2][0]-polygons[index][0],polygons[index+2][1]-polygons[index][1],polygons[index+2][2]-polygons[index][2]]
    return [vec1[1]*vec2[2]-vec1[2]*vec2[1],vec1[2]*vec2[0]-vec1[0]*vec2[2],vec1[0]*vec2[1]-vec1[1]*vec2[0]]
