public class ExclusiveProduct {
  // Approach with division, O(N), fails if any number is 0
  public static int[] calculate(int[] numbers) {
    int product = 1;
    // Calculate total product
    for (int i = 0; i < numbers.length; i++) {
      product *= numbers[i];
    }
    // Build array
    for (int i = 0; i < numbers.length; i++) {
      // division by zero may happen
      numbers[i] = product / numbers[i]; 
    }
    return numbers;
  }
	
  // No division, O(N^2), doesn't fail on zero 
 public static int[] calculateNoDivision(int[] numbers) {
    int[] result = new int[numbers.length];
    int product;
    for (int i = 0; i < numbers.length; i++) {
      roduct = 1;
      for (int j = 0; j < numbers.length; j++) {
        if (j != i) {
          product *= numbers[j];
        }
      }
      result[i] = product;
    }
    return result;
  }
}
