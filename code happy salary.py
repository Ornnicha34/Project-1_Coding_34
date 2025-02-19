salary = int(input("เงินเดือน"))
years_worked = int(input("จำนวนปีที่ทำงาน"))

def calculate_bonus(salary,years_worked):


#salary = int(input("เงินเดือน"))

#years_worked = int(input("จำนวนปีที่ทำงาน"))

  if years_worked <= 5:
    bonus = salary * 0.05

  elif years_worked <= 10:
    bonus = salary * 0.10
  else:
    bonus = salary * 0.15

  return bonus

bonus = calculate_bonus(salary,years_worked)
print(f"จำนวนเงินโบนัส : {bonus: .2f}บาท")