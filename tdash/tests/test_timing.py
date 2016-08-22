import time
from tdash import Stopwatch

def test_stopwatch_times_correctly():
    """
    tests that the start time is set correctly, doesnt check interval
    """
    time_start = time.time()
    stpwtch = Stopwatch()
    assert abs(stpwtch.start_time - time_start) < 1

    time.sleep(3.2)

    time2 = time.time()
    stpwtch.print_time('null msg')
    assert abs(stpwtch.start_time - time2) < 1
