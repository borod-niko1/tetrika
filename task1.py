#Подогнал под ответ вычев единицу, но не понял почему так, индекс первого нуля 25
#Сложность алгоритма O(n)

def task(array):
  return array.index("0") - 1

print(task("111111111111111111111111100000000"))

