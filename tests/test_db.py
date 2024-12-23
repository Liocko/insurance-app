import unittest
import psycopg2
import os
import time

class TestDBConnection(unittest.TestCase):
    def test_connection(self):
        # Загрузка параметров из переменных окружения
        dbname = os.getenv("POSTGRES_DB", "insurancedb")
        user = os.getenv("POSTGRES_USER", "liocko")
        password = os.getenv("POSTGRES_PASSWORD", "password")
        host = os.getenv("POSTGRES_HOST", "postgres")
        port = int(os.getenv("POSTGRES_PORT", 5432))
        
        retries = 5  # Количество попыток подключения
        delay = 5    # Задержка между попытками (в секундах)
        
        for attempt in range(retries):
            try:
                conn = psycopg2.connect(
                    dbname=dbname,
                    user=user,
                    password=password,
                    host=host,
                    port=port
                )
                self.assertIsNotNone(conn)
                conn.close()  # Закрываем подключение после успешного теста
                return  # Если подключение удалось, тест считается успешным
            except Exception as e:
                if attempt < retries - 1:
                    print(f"Connection attempt {attempt + 1} failed. Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    self.fail(f"Database connection failed after {retries} attempts: {e}")

if __name__ == "__main__":
    unittest.main()
