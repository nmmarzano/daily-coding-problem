public class ListSum {

  public static boolean addsUp(int[] nums, int tgt){
    for(int i = 0; i < nums.length; i++){
      for(int j = i+1; j < nums.length; j++){
        if(nums[i] + nums[j] == tgt){
          return true;
        }
      }
    }
    return false;
  }
	
}
