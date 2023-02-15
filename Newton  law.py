law = ("If a body is at rest or moving at a constant speed in a straight line, it will remain at rest or keep moving in a straight line at constant speed unless it is acted upon by a force",
       "It states that the time rate of change of the momentum of a body is equal in both magnitude and direction to the force imposed on it. ",
       "It states that when two bodies interact, they apply forces to one another that are equal in magnitude and opposite in direction. The third law is also known as the law of action and reaction")
print("The first law of Newton is :\n",law[0])
print("\nThe second law of Newton is :\n",law[1])
print("\nThe third law of Newton is :\n",law[2])
m = float(input("enter the mass "))
a= int(input("enter the acceleration"))
v = int(input("enter the velocity\n"))
F = m *a
P = m *v
print("the total force exterted by body of mass {0} is {1}".format(m,F))
print("the total momentum exterted by body of mass {0} and velocity {1} is {2}".format(m,v,P))
