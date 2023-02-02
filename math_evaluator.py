import math

__version__ = "1.0"

allowed_names = {k: v for k, v in math.__dict__.items() 
                if not k.startswith("__")}

mark = ">>>"

welcome = f"""

EVAluator {__version__}, вычислитель простейших математических выражений!

Введите корректное математическое выражение после знака "{mark}".
Наберите "help" для получения информации.
Наберите "quit" или "exit" для выхода из программы.
"""

usage = f"""

Применение:
Вычисляйте математические выражения используя
числовые значения и встроенные математические функции.

Вы можете использовать нижепоименованные функции и константы:
{', '.join(allowed_names.keys())}
"""



def evaluate(expression):

    """Вычисляет математическое выражение."""
    
    # Собираем выражение
    code = compile(expression, "<string>", "eval")
    # Проверяем допустимость вводимых имен
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Использование '{name}' недопустимо")
    return eval(code, {"__builtins__": {}}, allowed_names)

def main():

    """Считывает и вычисляет пользовательский ввод"""

    print(welcome)

    while True:
        # Считываем пользовательский ввод
        try:
            expression = input(f"{mark} ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Перехватываем команды помощи и выхода
        if expression.lower() == "help":
            print(usage)
            continue

        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()

        # Вычисляем выражение и перехватываем ошибки
        try:
            result = evaluate(expression)

        except SyntaxError:
            # Если пользователь вводит недопустимое выражение
            print("Неверный синтаксис выражения")
            continue

        except (NameError, ValueError) as err:
            # Если пользователь пытается использовать недопустимое имя
            # или передано недопустимое значение в выражение
            print(err)
            continue

        # Выводим результат, если не вызвано ошибок
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
