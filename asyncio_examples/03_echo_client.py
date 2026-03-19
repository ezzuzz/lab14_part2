"""
Асинхронный эхо-клиент для сервера из 02_echo_server.py.

Задания:
  TODO 7 — дописать отправку сообщения и получение ответа
  TODO 8 — запустить несколько клиентов одновременно через gather()

Запуск (предварительно запустите сервер):
    python3 02_echo_server.py
    python3 03_echo_client.py
"""

import asyncio


async def tcp_echo_client(message, client_name="Client"):
    """Подключается к серверу, отправляет сообщение и получает ответ."""
    # Подключаемся к серверу
    reader, writer = await asyncio.open_connection('127.0.0.1', 9095)
    
    print(f"{client_name}: Отправляю '{message}'")
    
    # TODO 7: Отправляем сообщение и получаем ответ
    # Подсказка:
    #   writer.write(message.encode())
    #   await writer.drain()
    #   data = await reader.read(1024)
    #   print(f"{client_name}: Получено '{data.decode()}'")
    
    # --- Ваш код для TODO 7 ---
    
    # Отправляем сообщение
    writer.write(message.encode())
    await writer.drain()
    
    # Получаем ответ
    data = await reader.read(1024)
    print(f"{client_name}: Получено '{data.decode()}'")
    
    # --- Конец вашего кода ---
    
    print(f"{client_name}: Закрываю соединение")
    writer.close()
    await writer.wait_closed()


async def main_single():
    """Запуск одного клиента."""
    await tcp_echo_client("Hello, asyncio!", "Клиент-1")


async def main_multiple():
    """Запуск нескольких клиентов одновременно."""
    print("\n--- Запускаем несколько клиентов одновременно ---")
    
    # TODO 8: Запустить несколько клиентов одновременно через asyncio.gather()
    # Подсказка:
    #   await asyncio.gather(
    #       tcp_echo_client("Сообщение 1", "Клиент-1"),
    #       tcp_echo_client("Сообщение 2", "Клиент-2"),
    #       tcp_echo_client("Сообщение 3", "Клиент-3")
    #   )
    
    # --- Ваш код для TODO 8 ---
    
    await asyncio.gather(
        tcp_echo_client("Сообщение 1", "Клиент-1"),
        tcp_echo_client("Сообщение 2", "Клиент-2"),
        tcp_echo_client("Сообщение 3", "Клиент-3")
    )
    
    # --- Конец вашего кода ---


if __name__ == '__main__':
    print("--- Один клиент ---")
    asyncio.run(main_single())
    
    print("\n--- Несколько клиентов одновременно ---")
    asyncio.run(main_multiple())
    
    print("\nВсе клиенты завершили работу")