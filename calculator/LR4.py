import SimpleArithmetic
import DivWithRem
import TrigF
n1 = float(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
TrigF.trigfunctions(n1, n2)
print("Сумма: ", SimpleArithmetic.sum(n1, n2))
print("Деление с остатком: ", DivWithRem.div_with_rem(n1, n2))