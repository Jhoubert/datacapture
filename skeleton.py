from datacapture import DataCapture
import random
import sys

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
print(stats.less(4), "Should return 2 (only two values 3, 3 are less than 4)")
print(stats.between(3, 6), "should return 4 (3, 3, 4 and 6 are between 3 and 6)")
print(stats.greater(4), "should return 2 (6 and 9 are the only two values greater than 4)")


if len(sys.argv) > 1:
    iterations = int(sys.argv[1])
    capture_prof = DataCapture()
    for _ in range(iterations):
        capture_prof.add(random.randint(0, 300))
    stats_prof = capture_prof.build_stats()

    print(stats_prof.less(120))
    print(stats_prof.greater(200))
    print(stats_prof.between(123,212))

