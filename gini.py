from collectins import Counter
def gini(features):
  ret = 1.0
  counters = Counter(features)
  for num in counters.values():
    p = num / len(features)
    ret -= p ** 2
  return ret
