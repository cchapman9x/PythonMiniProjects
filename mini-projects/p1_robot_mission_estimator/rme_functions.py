import lib1_basic_math as bm

# runtime in hours = battery energy / power consumption = (be / pc)
def runtime_in_hours(be, pc):
    runtime = bm.divide(be, pc)
    return runtime

# maximum distance = speed * runtime in seconds = (sp * rt_s)
def maximum_distance(sp, rt_s):
    max_d = bm.multiply(sp, rt_s)
    return max_d

# trip time in seconds = planned distance / speed = (pd / sp)
def trip_time(pd, sp):
    duration = bm.divide(pd, sp)
    return duration
