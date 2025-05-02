class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

def merge(intervals):
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    # TODO: Write your code here
    return mergedIntervals
