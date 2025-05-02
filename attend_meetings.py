# if earlier meetings end time is greater than later meeting start time
# return 0
# otherwise return 1
def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """

    for index in range(len(intervals) - 1):
      curr_end = intervals[index][1]
      next_meeting = intervals[index + 1]
      next_start = next_meeting[0]

      if curr_end > next_start:
        return 0

    return 1

print(can_attend_all_meetings([
[1, 5],
[5, 8],
[10, 15]
]))

print(can_attend_all_meetings([
[1, 5],
[4, 8]
]))
