def myping(host):
    # Выберите параметр в зависимости от операционной системы
    parameter = "-n" if platform.system().lower() == "windows" else "-c"
    number = input('Введите кол-во пингов:')
    # Построение команды ping
    command = ["ping", parameter, number, host]
    response = subprocess.call(command)

    # Интерпретация ответа
    return response == 0
