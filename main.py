from sympy import *
from sympy.plotting import plot

x = Symbol("x")
f = 5 * x ** 2 + 10 * x - 30
f

plot(f, (x, -5, 2.5))

solve(f)

solveset(f)  # 1. Определить корни
#    Нули функции

solveset(f > 0)  # 2. Найти интервалы, на которых функция возрастает

solveset(f < 0)  # 3. Найти интервалы, на которых функция убывает  и возрастает

result = [-oo, oo]  # [-oo,oo] - минус бесконечность и бесконечность
result[1:1] = solve(diff(f), x)
result

res_increase = []
res_dicrease = []
for i in range(1, len(result)):
    if is_increasing(f, Interval.open(result[i - 1], result[i])):
        res_increase.append(f'{result[i - 1]}, {result[i]}')
    else:
        res_dicrease.append(f'{result[i - 1]}, {result[i]}')
print(f'Убывает {res_dicrease}')
print(f'Возрастает {res_increase}')

# 5. Вычислить вершину
#    Экстремумы функции

result_func = solve(diff(f), x)
for i in result_func:
    check = f.subs(x, i)
    if check > 0:
        print(f'Точка минимума {i},{check}')
    elif check < 0:
        print(f'Точка максимума {i},{check}')
    else:
        print(f'{check} находится на оси')

# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
#    Знакопостоянства функции

result = [-oo, oo]
result[1:1] = solve(f, x)

res_increase = []
res_dicrease = []
for i in range(1, len(result)):
    if is_increasing(f, Interval.open(result[i - 1], result[i])):
        res_increase.append(f'{result[i - 1]}, {result[i]}')
    else:
        res_dicrease.append(f'{result[i - 1]}, {result[i]}')
print(f'f>0 {res_dicrease}')
print(f'f<0 {res_increase}')

plot(f, (x, -5, 2.5))