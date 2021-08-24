# How to run

Requirements: 
 - Python 
	 - Already tested on 2.7 and 3.7 and 3.8.5
 - Pytest for run tests only

The file datacapture.py has only logic classes, so to check the code really works you can run tests or skeleton

    python -m pytest test_dc.py

To run the skeleton given you can run 

    python skeleton.py

For profiling and checking the performance you can also run skeleton.py file with cpython profiler but aditionally using a number of extra iterations with random numbers on captures.

    python3 -m cProfile skeleton.py 1000000

Where `1000000` is run with 1 million captures, when it finish you can check all the code behavior and performance pretty detailed.
