def score(x, y):
  """
  Calculates points earned in a Darts game based on dart coordinates.

  Args:
      x: X-coordinate of the dart's location.
      y: Y-coordinate of the dart's location.

  Returns:
      The number of points earned (0, 1, 5, or 10).
  """
  squared_distance = (x - 0)**2 + (y - 0)**2  # Center coordinates assumed to be (0, 0)

  if squared_distance <= 1:
    return 10  # Bullseye
  elif squared_distance <= 25:
    return 5  # Middle ring
  elif squared_distance <= 100:
    return 1  # Outer ring
  else:
    return 0  # Outside the target
