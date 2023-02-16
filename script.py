class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return "A {} school named {} with {} students".format(self.level, self.name, self.numberOfStudents)

  def getName(self):
    return self.name
  
  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudents
  
  def setNumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents,           
pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def getPickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + ". The pickup policy is {}".format(self.pickupPolicy)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def getSportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + ". This are their sports teams: {}".format((self.sportsTeams))
  

h = School("Legacy", "high", 500)
print(h)
print(h.getName())
print(h.getLevel())
h.setNumberOfStudents(200)
print(h.getNumberOfStudents())

b = PrimarySchool("Westlake", 300, "Pickup Allowed")
print(b.getPickupPolicy())
print(b)

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)





  
  
