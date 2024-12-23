
import unittest
import psycopg2

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        try:
            conn = psycopg2.connect(
                dbname="insurancedb",
                user="liocko",
                password="password",
                host="postgres",
                port=5432
            )
            self.assertIsNotNone(conn)
        except Exception as e:
            self.fail(f"Database connection failed: {e}")

if __name__ == "__main__":
    unittest.main()
