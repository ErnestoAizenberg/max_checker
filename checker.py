import asyncio
import sigmax

async def main():
    # Создаем клиент внутри асинхронной функции
    client = sigmax.Client()
    
    # Логинимся перед выполнением запросов
    await client.login_with_token("ТОКЕН")
    
    try:
        # Выполняем запрос
        user = await client.get_user_by_phone('+78005553535')
        print(user.name)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрываем клиент при завершении
        await client.close()

# Запускаем основную функцию
asyncio.run(main())