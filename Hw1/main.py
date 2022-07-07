

# qu 6
# class geometricShape:
#     def __init__(self, rib ):
#         self.rib = rib
#
# class Circle(geometricShape):
#     def AreaAndScope(self):
#         print("the area is",self.rib**2*3.14159265,"the Scope is", 2*self.rib*3.14159265)
#         print("")
#
# class Rect(geometricShape):
#
#     def __init__(self,rib,rib2):
#         geometricShape.__init__(self,rib)
#         self.rib2 = rib2
#     def AreaAndScope(self):
#         print("the area is",self.rib*self.rib2,"the Scope is", self.rib*2+self.rib2*2)
#
# class Triangular(geometricShape):
#
#     def __init__(self,rib1,rib2,rib3,height):
#         geometricShape.__init__(self,rib1)
#         self.rib2 = rib2
#         self.rib3 = rib3
#         self.height=height
#     def AreaAndScope(self):
#         print("the area is",self.rib*self.height,"the Scope is", self.rib2+self.rib2+self.rib3)
#
# class Square(Rect):
#
#     def __init__(self,rib1):
#         Rect.__init__(self,rib1,rib1)
#     def AreaAndScope(self):
#         print("the area is",self.rib*self.rib,"the Scope is", 4*self.rib)
#
#
#
#
#
# if __name__ == '__main__':
#     a=input("enter char for the shape:")
#     if a=='c' or a=='C':
#         radius=int(input("enter the radius of the circle:"))
#         circle=Circle(radius)
#         circle.AreaAndScope()
#
#     if a=='r' or a=='R':
#         length=int(input("enter the length of the rect:"))
#         width = int(input("enter the width of the rect:"))
#         rect=Rect(length,width)
#         rect.AreaAndScope()
#
#     if a == 's' or a == 'S':
#         length = int(input("enter the length of the square:"))
#
#         square = Rect(length,length)
#         square.AreaAndScope()
#
#     if a == 't' or a == 'T':
#         rib1 = int(input("enter the length of the Triangular:"))
#         rib2 = int(input("enter the length of the Triangular:"))
#         rib3 = int(input("enter the length of the Triangular:"))
#         height = int(input("enter the height of the Triangular:"))
#         triangular=Triangular(rib1,rib2,rib3,height)
#         triangular.AreaAndScope()
#

#qu 9
# class Animale:
#     def __init__(self, dataofBirth, kind, name, legs_number):
#         self.dataofBirth = dataofBirth
#         self.kind = kind
#         self.name = name
#         self.legs_number = legs_number
#
#
# class HouseAnimale(Animale):
#     def __init__(self, dataofBirth, kind, name, legs_number, lastCheckIn_Veterinarian):
#         Animale.__init__(self,dataofBirth, kind, name, legs_number)
#         self.lastCheckIn_Veterinarian = lastCheckIn_Veterinarian
#
#
# class Cats(Animale):
#     def __init__(self, dataofBirth, kind, name, legs_number, length_mustache):
#         Animale.__init__(self,dataofBirth, kind, name, legs_number)
#         self.length_mustache = length_mustache
#
#
# class HouseCat(Cats, HouseAnimale):
#     def __init__(self, dataofBirth, kind, name, legs_number, lastCheckIn_Veterinarian, length_mustache, Owners):
#         Cats.__init__(self,dataofBirth, kind, name, legs_number, length_mustache)
#         HouseAnimale.__init__(self,dataofBirth, kind, name, legs_number, lastCheckIn_Veterinarian)
#         self.Owners = Owners
#
#
# class Tigers(Animale):
#     def __init__(self, dataofBirth, kind, name, legs_number, length_claws):
#         Animale.__init__(self,dataofBirth, kind, name, legs_number)
#         self.length_claws = length_claws
#
#
# def Cats_Tigers():
#     tigers = 0
#     cats = 0
#     n = int(input("enter number of animals:"))
#
#     for i in range(n):
#         animal = input("enter the kind of the Tiger or house cat:")
#         if animal == "Tiger" or animal == "tiger":
#             tigers += 1
#             tiger = Tigers("11/02/20", "mammal", "tiger", "4", "10")
#         else:
#             cats += 1
#             cat = HouseCat("11/02/2020", "mammal", "Cat", 4, "27/11/2020", 20, True)
#
#     print("cats:", cats, "tigers:", tigers)
#
#
# if __name__ == '__main__':
#     Cats_Tigers()


 
