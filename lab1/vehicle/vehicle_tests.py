import unittest
import vehicle

class VehicleTests(unittest.TestCase):
   def test_vehicle(self):
      # Add code here
      car1 = vehicle.vehicle(5, 1, 3.9, False)

      self.assertEqual(car1.wheels, 5)
      self.assertEqual(car1.doors, 1)
      self.assertEqual(car1.fuel, 3.9)
      self.assertEqual(car1.roof, False)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

