def flow_control(m):
	if(m == 0):
		s = "Variable m = %d equals 0." % m 
	elif(m == 1):
		s = "Variable m = %d equals 1." % m
	else:
		s = "Variable m = %d does not equal 0 or 1." % m
	print(s)


def main():
	i = 0
	flow_control(i)
	i = 1
	flow_control(i)
	i = 2
	flow_control(i)


if __name__ == "__main__":
	main()