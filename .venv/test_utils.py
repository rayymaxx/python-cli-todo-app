import unittest
from utils import generate_task_id
from task import Task

class TestUtils(unittest.TestCase):
    def test_generate_task_id_empty(self):
        self.assertEqual(generate_task_id([]), 1)

    def test_generate_task_id_non_empty(self):
        tasks = [Task(1, "Test", "Desc"), Task(3, "Another", "Desc")]
        self.assertEqual(generate_task_id(tasks), 4)


if __name__ == "__main__":
    unittest.main()