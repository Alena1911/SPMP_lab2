from queue import Queue


# Чтение в очередь из файла посимвольно
def file_to_queue(file):
    q = Queue()
    for line in file:
        for ch in line:
            q.put(ch)
    return q


# Преобразование очереди символов в очередь строк
def queue_chars_to_queue_lines(char_q):
    ch = ""
    line = ""
    line_q = Queue()
    while not char_q.empty():
        while ch != "\n" and not char_q.empty():
            ch = char_q.get()
            line += ch
        line_q.put(line)
        line = ""
        ch = ""
    return line_q


f = open('test.txt', 'r', encoding="utf-8")
queue = file_to_queue(f)
f.close()

l_q = queue_chars_to_queue_lines(queue)
print(l_q.get())
print(l_q.get())
