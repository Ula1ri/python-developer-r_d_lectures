# 2. Створити програму, яка буде друкувати в консоль “I love Python” кожні 4.2 секунди, 
# поки її виконання не буде перервано вручну.
import time
x = 1
while x > 0:
    time.sleep(4.2)
    print("I love Python")