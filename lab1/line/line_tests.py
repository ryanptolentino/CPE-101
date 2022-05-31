import unittest
import line

class LineTests(unittest.TestCase):
   def test_line(self):

      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.
      a = line.line(5, 0, 4, 2)
      self.assertEqual(a.x1, 5)
      self.assertEqual(a.y1, 0)
      self.assertEqual(a.x2, 4)
      self.assertEqual(a.y2, 2)

   def test_line_again(self):

      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.
      b = line.line(6, 9, 6, 9)
      self.assertEqual(b.x1, 6)
      self.assertEqual(b.y1, 9)
      self.assertEqual(b.x2, 6)
      self.assertEqual(b.y2, 9)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

