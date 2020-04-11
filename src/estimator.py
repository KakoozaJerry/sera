def estimator(data):
  return data
#Challenge 1
class Impact:
  def __init__(self, reportedCases):
    self.currentlyInfected = reportedCases * 10
  def infectionsByRequestedTime(self,T):
    return self.currentlyInfected*(pow(2,(T//3)))
  pass

class SevereImpact:
  def __init__(self, reportedCases):
    self.currentlyInfected = reportedCases * 50
  def infectionsByRequestedTime(self,T):
    return self.currentlyInfected*(pow(2,(T//3)))
  pass