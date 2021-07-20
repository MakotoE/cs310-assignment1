import sys
from typing import List, Tuple


def findMinRooms(*schedule: List[float]) -> int:
	"""
	:param schedule: list of start and end times of time slots
	:return: minimum number of conference rooms needed
	"""
	try:
		return findMinRoomsWithError([(item[0], item[1]) for item in schedule])
	except Exception as e:
		print(e, file=sys.stderr)


def findMinRoomsWithError(schedule: List[Tuple[float, float]]) -> int:
	"""
	:return: minimum number of conference rooms needed
	"""
	sorted_schedule = sorted(schedule, key=lambda item: item[0])

	max_overlap = 0
	for i in range(len(sorted_schedule)):
		n = overlapping(sorted_schedule, i)
		if n > max_overlap:
			max_overlap = n

	return max_overlap


def overlapping(schedule: List[Tuple[float, float]], index: int) -> int:
	"""
	:param schedule: time slots, sorted by start time
	:param index: index of schedule to find overlapping slots
	:return: Number of overlapping time slots of time slot at index
	:raises Exception: schedule includes a start time that is greater than end time
	"""
	overlapping_count = 0
	for i in range(index, len(schedule)):
		if schedule[index][0] > schedule[index][1]:
			raise Exception('start time is greater than end time')

		if (schedule[index][0] <= schedule[i][0] <= schedule[index][1]) \
				or (schedule[index][0] <= schedule[i][1] <= schedule[index][1]):
			overlapping_count += 1
		elif schedule[i][0] > schedule[index][1]:
			break
	return overlapping_count
