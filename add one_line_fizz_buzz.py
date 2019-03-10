## Mihir Patel
## 3/9/19
## File : one_line_fizz_buzz.py


# implement fizz_buzz in one line

print ([["", "fizz"][num % 3 == 0] + ["", "buzz"][num % 5 == 0] for num in range(1, 100)])
