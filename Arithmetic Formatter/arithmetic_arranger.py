def arithmetic_arranger(problems):
  arranged_problems = ""
  line1 = line2 = line3 = line4 = ""

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    num_1, op, num_2 = problem.split()

    try:
      num_1 = int(num_1)
      num_2 = int(num_2)

      if num_1 <= 9999 and num_2 <= 9999:

        if op == "+":
          solution = str(int(num_1) + int(num_2))
        elif op == "-":
          solution = str(int(num_1) - int(num_2))
        else:
          print("Operator must be '+' or '-'.")

      else:
        print("Error: Numbers cannot be more than four digits.")

    except ValueError:
      print("Error: Numbers must only contain digits.")

    width = max(len(str(num_1)), len(str(num_2))) + 2

    line1 += str(num_1).rjust(width) + "    "
    line2 += op + " " + str(num_2).rjust(width - 2) + "    "
    line3 += "-" * width + "    "

    line4 += str(solution).rjust(width) + "    "

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip(
    ) + "\n" + line3.rstrip()
    if line4:
      arranged_problems += "\n" + line4.rstrip()

  return arranged_problems
