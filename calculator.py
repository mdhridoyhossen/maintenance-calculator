total_time = float(input("Total running time (hours): "))
failures = int(input("Number of failures: "))
repair_time = float(input("Total repair time (hours):"))
mtbf = total_time / failures
mttr = repair_time / failures
availability = mtbf / (mtbf + mttr) * 100
print("MTBF:", round(mtbf, 2), "hours")
print("MTTR:", round(mttr, 2), "hours")
print("Availability:", round(availability, 2), "%")