class NotNaturalNumberError(Exception):
	pass


def fatorial(num):
	if not isinstance(num, int) or num < 0:
		raise NotNaturalNumberError('Only natural numbers')
	if num < 2:
		return 1
	return num * fatorial(num - 1)