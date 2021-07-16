import sys
from typing import List, Tuple


def findMinRooms(*schedule: List[float]) -> int:
	try:
		return findMinRoomsWithError([(item[0], item[1]) for item in schedule])
	except Exception as e:
		print(e, file=sys.stderr)


def findMinRoomsWithError(schedule: List[Tuple[float, float]]) -> int:
	sorted_schedule = sorted(schedule, key=lambda item: item[0])

	max_overlap = 0
	for i, _ in enumerate(sorted_schedule):
		n = overlapping(sorted_schedule, i)
		if n > max_overlap:
			max_overlap = n

	return max_overlap


def overlapping(schedule: List[Tuple[float, float]], index: int) -> int:
	overlapping_count = 0
	for i in range(index, len(schedule)):
		if (schedule[index][0] <= schedule[i][0] <= schedule[index][1]) or (
				schedule[index][0] <= schedule[i][1] <= schedule[index][1]):
			overlapping_count += 1
		elif schedule[i][0] > schedule[index][1]:
			break
	return overlapping_count
