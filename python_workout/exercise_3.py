def run_timing():
	number_of_runs = 0
	total_time = 0

	while True:
		one_run = input("Enter the 10 km run time: ")

		if not one_run:
			break

		number_of_runs += 1
		total_time += float(one_run)

	avg_time = total_time/ number_of_runs

	print(f"Average time is {avg_time: .2f} of {number_of_runs} runs")

#run_timing()

def before_and_after(x: float, y: int, z: int):
	temp = str(x).split(".")
	result = float(f"{temp[0][-y:]}.{temp[1][:z]}")
	return result

print(before_and_after(1234.567, 2, 3))
