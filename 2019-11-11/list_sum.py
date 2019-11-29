def addsUp(numbers, target):
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == target:
        return True
  return False
