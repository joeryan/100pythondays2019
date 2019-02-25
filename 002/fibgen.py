import argparse

def fibonacci_generator(limit):
  count = 1
  current, next = 0, 1
  while count <= limit:
    current, next = next, next + current
    count += 1
    yield current 

def main():
  parser = argparse.ArgumentParser(description="generate a fibonacci sequence")
  parser.add_argument("limit", type=int, help="Ending number to generate fibonacci sequence")
  args = parser.parse_args()
  nums = fibonacci_generator(args.limit)
  for num in nums:
    print(num, end=', ')


if __name__ == '__main__':
  main()

