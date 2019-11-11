public class Staircase {
	
	public static int waysToClimb(int steps, int[] alts){
		if (alts.length == 0 || (alts.length == 1 && alts[0] == 0)) {
			return 0;
		}
		return recursiveWaysToClimb(steps, 0, alts, "");
	}
	
	private static int recursiveWaysToClimb(int steps, int climbed, int[] alts, String path){
		if (steps - climbed == 0) {
			System.out.println("Found path:"+path);
			return 1;
		} else if (steps - climbed < 0) {
			return 0;
		} else {
			int count = 0;
			for (int i = 0; i < alts.length; i++){
				count += recursiveWaysToClimb(steps - climbed, alts[i], alts, path+" "+alts[i]);
			}
			return count;
		}
		
	}
	
}
