from my_app.models import *

employees = Employee.objects.all()
employees

employees = Employee.objects.all().values_list('fullname', 'salary').order_by('-salary')
employees

new_emp = Employee.objects.create(
    fullname='Навуходоно́сор',
    birth_date='1980-01-01',
    salary=35000,
    receipt_date='2010-01-01',
    department_id=2,
    position_id=4)

new_emp.save()
new_emp.department.name

employees = Employee.objects.all().order_by('-birth_date', 'receipt_date')
employees

from django.db.models import Q

employees = Employee.objects.filter(Q(salary__lt=50000) | Q(salary__gt=20000))
employees

accounting_department = Department.objects.get(name='accounting_department')
accounting_department

accounting_employees = Employee.objects.filter(department=accounting_department).order_by('fullname')
accounting_employees

from django.db.models import Count

departments = Department.objects.annotate(employee_count=Count('employee')).order_by('employee_count')
departments

employees = Employee.objects.values('department_id').annotate(department_count=Count('department'))
employees

from django.db.models import Avg

average_salary = Department.objects.annotate(avg_salary=Avg('employee__salary'))
average_salary

employees_salary = Employee.objects.all().annotate(salary_count=Avg('salary'))
employees_salary



from datetime import date

# Получаем текущую дату
current_date = date.today()

# Получаем список всех сотрудников
employees = Employee.objects.all()

# Рассчитываем премию для каждого сотрудника
for employee in employees:
    years_worked = (current_date - employee.receipt_date).days / 365  # Считаем годы работы
    if years_worked < 5:
        bonus_percentage = 0.05  # 5% премии для менее 5 лет стажа
    elif years_worked >= 5 and employee.department.name == 'IT_department':
        bonus_percentage = 0.10  # 10% премии для более 5 лет стажа и IT отдела
    else:
        bonus_percentage = 0.08  # 8% премии для более 5 лет стажа (не IT отдел)

    bonus = employee.salary * bonus_percentage  # Рассчитываем премию
    employee.bonus = bonus  # Присваиваем премию сотруднику
    employee.save()  # Сохраняем изменения в базе данных


from datetime import date

# Дата начала работы "Навуходоно́сора"
start_date = date(2010, 1, 1)

# Получаем текущую дату
current_date = date.today()

# Рассчитываем количество дней между началом работы и текущей датой
days_worked = (current_date - start_date).days

# Проверяем, если "Навуходоно́сор" уже проработал 5 лет
if days_worked >= (5 * 365):  # Предполагаем, что в году 365 дней
    days_till_vacation = days_worked % (5 * 365)  # Остаток дней после 5 лет
else:
    days_till_vacation = 0  # "Навуходоно́сор" еще не проработал 5 лет

print(f"Сотрудник Навуходоно́сор уйдет на отпуск через {days_till_vacation} дней")
