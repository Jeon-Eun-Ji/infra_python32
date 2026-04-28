cpu_log = [75,55,96,51,41]

warning_cpu = [str(cpu_usage) + "%" for cpu_usage in cpu_log if cpu_usage >= 80]
print(warning_cpu)