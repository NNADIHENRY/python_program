""" volume and surface area of a cylinder
 by NNADI HENRY IFEANYI
 08139264713 nnadihenry92@gmail.com """
pi = 3.142857
r = float(input("enter radius: "))
h = float(input("enter height: "))
area = 2*pi*r*r + 2*pi*r*h
volume = pi*r*r*h
print("area = " + str(area))
print("volume = " + str(volume))
