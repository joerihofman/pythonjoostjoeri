from Week3.stop_watch import StopWatch
size = 1000000
stopWatch = StopWatch()
stopWatch.starta()
sum = 0
for i in range(1, size + 1):
    sum += i

stopWatch.stopa()
print("The loop time is", stopWatch.get_elapsed_time(), "milliseconds")

"""
De class StopWatch implementeert een eenvoudige stopwatch. De class StopWatch bevat het volgende:
fields startTime en endTime
(private)

methods
constructor         init start_time
start               reset start_time naar huidige tijd
stop                maakt end_time gelijk aan de huidige tijd
get_elapsed_time    geeft de verstreken tijd, dus end_time - start_time (in
                    milliseconden)
getStartTime
getEndTime

De methode time.time() uit module time geeft de huidige tijd.


"""