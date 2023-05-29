class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """ Добавление элемента в конец очереди. """

        self.queue.append(item)

    # def enqueue(self, item):
    #     """ Добавление элемента в конец очереди. """
    #
    #     self.queue.insert(0, item)

    def dequeue(self):
        """ Удаление элемента из начала очереди. """

        if not self.is_empty():
            last_element = self.queue[0]  # Получение последнего элемента
            self.queue = self.queue[1:]  # Удаление последнего элемента
            return last_element
        else:
            print('Очередь пуста.')

        # if not self.is_empty():
        #     return self.queue.pop()
        # else:
        #     print('Очередь пуста.')

    def is_empty(self):
        """ Проверка является ли очередь пустой или нет. """

        return len(self.queue) == 0

    def peek(self):
        """ Вывод в консоль первого элемента, без его удаления. """

        if not self.is_empty():
            return self.queue[0]
        else:
            print('Очередь пуста.')

    def rear(self):
        """ Вывод в консоль последнего элемента, без его удаления. """

        if not self.is_empty():
            return self.queue[-1]
        else:
            print('Очередь пуста.')

    def size(self):
        """ Получение размера очереди. """

        return len(self.queue)


my_queue = Queue()  # Создание экземпляра
print('Проверка очередь пустая или нет: ', my_queue.is_empty())

# Добавление элементов в очередь
my_queue.enqueue("Apple")
my_queue.enqueue("Banana")
my_queue.enqueue("Orange")
my_queue.enqueue("Cherry")

print('\nВся очередь: ', my_queue.queue)
print('Размер очереди: ', my_queue.size())
print('Первый элемент очереди: ', my_queue.peek())
print('Последний элемент очереди: ', my_queue.rear(), '\n')

# Удаление и вывод этих элементов
print('Удаление элементов:')
print(my_queue.dequeue())
print(my_queue.dequeue())

print('\nПроверка очередь пустая или нет: ', my_queue.is_empty())
print('Вся очередь: ', my_queue.queue)
print('Размер очереди: ', my_queue.size())
print('Первый элемент очереди: ', my_queue.peek())
print('Последний элемент очереди: ', my_queue.rear(), '\n')

# Удаление и вывод этих элементов
print('Удаление элементов:')
print(my_queue.dequeue())
print(my_queue.dequeue())

# Попытка удаления элемента из пустой очереди
print()
my_queue.dequeue()
