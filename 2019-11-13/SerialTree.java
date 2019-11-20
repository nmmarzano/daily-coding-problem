import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SerialTree {
  
  public static class Node {
    public String value;
    public Node left;
    public Node right;
    
    public Node() {
      this(null, null, null);
    }
    public Node(String value) {
      this(value, null, null);
    }
    public Node(String value, Node left, Node right) {
      this.value = value;
      this.left = left;
      this.right = right;
    }
  }
  
  public static String serialize(Node tree) {
    StringBuilder result = new StringBuilder();
    result.append("\"" + Arrays.toString(tree.value.getBytes()) + "\"");
    if(tree.left != null || tree.right != null){
      result.append("(");
      if(tree.left != null){
        result.append("L" + serialize(tree.left));
      }
      if(tree.right != null){
        result.append("R" + serialize(tree.right));
      }
      result.append(")");
    }
    return result.toString();
  }
  
  public static Node deserialize(String s) throws Exception {
    Node node = new Node();
    if(s == null || s.isEmpty()){
      return null;
    }
    if(s.charAt(s.length()-1) == '"'){ // If it's a node with no children
      node.value = SerialTree.deserializeBytes(s.substring(1, s.length()-1));
      System.out.println("Node value: " + node.value);
    }else{
      Pattern separateRootFromChildren = Pattern.compile("\"([^\"]+)\"\\((.+)?\\)");
      Matcher matcher = separateRootFromChildren.matcher(s);
      if(matcher.find()){
        node.value = SerialTree.deserializeBytes(matcher.group(1));
        String children = matcher.group(2);
        int childStart = 0;
        int childEnd = 0;
        int i = 0;
        int count = 0;
        char childType;
        if(children!=null){
          childType = children.charAt(0);
          // Position myself at the start of the first child
          // look for start of children, start of R node, or end of string
          while(i < children.length() && children.charAt(i) != '(' 
              && !(childType == 'L' && children.charAt(i) == 'R')){
            i++;
          }
          i++;
          childStart = 1;
          count++;
          if (i >= children.length()) { // only has one leaf
            initializeChild(node, childType, deserialize(children.substring(1)));
          }else if(children.charAt(i-1) == 'R'){ // has two leaves
            if(childType == 'L'){
              initializeChild(node, childType, deserialize(children.substring(1, i-1)));
            }else {
              return null;
            }
            initializeChild(node, 'R', deserialize(children.substring(i)));
          }else if(children.charAt(i-1) == '('){ // has a branch, find the end, the rest is a second branch
            // look for the end of the child
            while(i < children.length() && count > 0){
              if(children.charAt(i) == '('){
                count++;
              }else if(children.charAt(i) == ')'){
                count--;
              }
              i++;
            }
            childEnd = i;
            i++;
            count++;
            initializeChild(node, childType, deserialize(children.substring(childStart, childEnd)));
            if (i <= children.length()) {
              childType = children.charAt(childEnd);
              initializeChild(node, childType, deserialize(children.substring(childEnd+1)));
            }
          }
        }
      }
    }
    return node;
  }
  
  private static void initializeChild(Node node, char childType, Node child) throws Exception{
    if(childType == 'L'){
      node.left = child;
    }else if(childType == 'R'){
      node.right = child;
    }else{
      throw new Exception("Bad string!");
    }
  }
  
  private static String deserializeBytes(String bytes){
    StringBuilder result = new StringBuilder();
    String[] byteArray = bytes.substring(1, bytes.length()-1).split(", ");
    for (int i = 0; i < byteArray.length; i++) {
      result.append((char)Integer.parseInt(byteArray[i]));
    }
    return result.toString();
  }
}
