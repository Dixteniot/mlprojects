
//
// TestUndoRedo.java
//

public class TestUndoRedo {
      public static void main(String [] args) {
          UndoRedo test1 = new UndoRedo();
          test1.pushBack("Hello World.");
          test1.pushBack("123...");
          int sizeX1 = test1.size();
          System.out.println("List1 size: "+sizeX1);
      }
}
