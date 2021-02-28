from math import *

class Point():
    def __init__(self,pos):
        self.pos = pos
    def Rotate2D(self,center,dg,pt):
        x,y = self.pos[:pt]
        s,c = sin(dg),cos(dg)
        self.pos[:pt] = [x*c-y*s,y*c+x*s]

class Polyedre():

    def ReloadRotation(self):
        rX,rY=self.rot
        x,y,z = self.pos
        for point in self.ListPoints:
            point.Rotate2D((x,y),rX,1)
            point.Rotate2D((y,z),rY,2)

    def __init__(self,listPoints,faces,rot = (0,0)):
        self.ListPoints = listPoints
        self.RotatedPoints = self.ListPoints
        self.rot = rot
        self.ReloadRotation()
        self.faces = faces

class Converter():

    def PointCubePolyedre(self,size,pos):
        x,y,z = pos
        return [Point((x,y,z)),Point((x+size,y,z)),Point((x+size,y+size,z)),Point((x,y+size,z)),Point((x,y,z+size)),Point((x+size,y,z+size)),Point((x+size,y+size,z+size)),Point((x,y+size,z+size))]
    def FacesCube(self):
        return [(0,1,2),(0,2,3),(0,1,4),(1,4,5),(1,2,5),(2,5,6),(2,3,6),(2,3,7),(4,5,6),(5,6,7),(0,3,4),(3,4,7)]

convert = Converter()
Maman = Polyedre(convert.PointCubePolyedre(10,(20,20,20)),convert.FacesCube(),0)


print(Maman.ListPoints)
