from typing import Optional
def salary(**departments: dict[dict[str, int|float]]):
    sum_salaries = 0
    for department in departments.values():
        for salary in department.values():
            sum_salaries += salary
        average_salary = sum_salaries / len(department)
        all_salaries = list(department.values())
        max_salary = max(all_salaries)
        index_middle_salary = len(all_salaries)//2
        median_salary = all_salaries[index_middle_salary]
    return round(average_salary, 2), max_salary, median_salary
print(salary(department1 = {'Ульяна':80000, 'Игорь':85000, 'Виктория': 70000}, department2 = {'Алина': 100000, 'Катя': 150000, 'Виктор': 150000}))
#max: Optional[int|float] = None,
#список зарплат
    
        