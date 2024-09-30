//
// UndoRedo.java
// Author: Brian M.
//

import java.util.*;
import java.io.*;

public class UndoRedo implements Stack, Serializable {

    private List list1;
    private List list2;
    private int done;

    public UndoRedo() {
        list1 = new ArrayList();
        list2 = new ArrayList();
        done = 0;
    }

    public int size() {
        return list1.size();
    }

    private int size(List listX) {
        return listX.size();
    }

    public void pushBack(Object word) {
        boolean push1 = list1.add(word);
        if (push1) {
            System.out.println("List1 size: "+size()+", pushBack word: "+word);
        }
    }

    private void doIt(Object word) {
        boolean push2 = list2.add(word);
        if (push2) {
            System.out.println("List2 size: "+size(list2)+", do word: "+word);
            done += 1;
        }
    }

    public Object pop() {
        int length1 = list1.size();
        if (length1 < 1) {
            throw new RuntimeException("Stack1 is empty.");
        }
        int index1 = length1 - 1;
        Object word = list1.remove(index1);
        doIt(word);
        return word;
    }

    public void undo() {
        int length2 = size(list2);
        if (length2 < 1) {
            throw new RuntimeException("Stack2 is empty.");
        }
        int index2 = length2 - 1;
        Object word = list2.remove(index2);
        pushBack(word);
        done -= 1;
    }

    public boolean redo() {
        if (done < 1) {
            System.out.println("done: "+done);
            return false;
        } else {
            Object word = pop();
            System.out.println("redo: "+word);
        }
        return true;

    }

}
