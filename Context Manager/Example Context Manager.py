# Example - 1
import traceback
class ContextManager:
        def __init__(self):
            self.log_counter = 0        # Счётчик успешных логов.

        def __enter__(self):
            self.log = open("log.txt", "a+") # Открываем лог-файл в режиме до-записи.
            return self  # Возвращаем объект менеджера.

        def __exit__(self, exc_type, exc_val, exc_tb): # exc_type, exc_val, exc_tb — если была ошибка.
            if not exc_type:  # ✅ Если ошибки не было.
                self.log_counter += 1
                self.log.write(f"Log counter: {self.log_counter}\n") # Пишем успешный лог.

            else:    # ❌ Если была ошибка.
                self.log.write(f"[Error] - {exc_type.__name__}: {exc_val}\n") # Тип и текст ошибки.
                trace = "".join(traceback.format_tb(exc_tb)) # Получаем traceback.
                self.log.write(f"[TraceBack]\n{trace}\n") # Пишем его в файл.

            self.log.write("File closed.\n") # Записываем что файл закрыт.
            self.log.close() # Закрываем файл.
            return False # Ошибки не подавляются (они поднимутся наружу).

cm = ContextManager()

# with cm as cm_object:
#     cm.log.write("Test - 1\n")
#
# with cm as cm_object:
#     cm.log.write("Test - 2\n")

with cm as cm_object:
    raise ValueError("Test - 3 Error.")

# ---> contextmanager <---
# Example - 1

from contextlib import contextmanager             # Импортируем декоратор для создания контекстного менеджера без класса.

@contextmanager                                   # Указываем, что следующая функция будет использоваться как контекстный менеджер.
def open_file(name, mode):                        # Определяем функцию, которая принимает имя файла и режим ("w", "a", "r" и т.д.).
    f = open(name, mode)                          # Открываем файл с указанным именем и режимом (например, "w" — запись).
    f.write("Before enter.\n")                    # Пишем в файл — до входа в блок `with`.

    try:                                          # __enter__
        f.write("In enter.\n")                    # Пишем в файл — в момент входа в `with` (до передачи управления пользователю).
        yield f                                   # Возвращаем объект `f` (файл) во внешний блок `with`.

    finally:                                      # __exit__
        f.write("In exit.\n")                     # Пишем в файл — при выходе из блока `with`, даже если была ошибка.
        f.close()                                 # Закрываем файл (обязательно).

with open_file("log1.txt", "w") as file:          # Входим в блок с нашим контекстным менеджером.
    file.write("Between [Enter] and [Exit].\n")   # Делаем что-то внутри блока.