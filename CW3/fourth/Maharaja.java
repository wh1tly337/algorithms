package Maharaja;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.BitSet;


public class Maharaja {
    public static void main(String[] args) throws Exception {
        String src = "/Users/user/IdeaProjects/algorithms/input.txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(src))) {
            int n = Integer.parseInt(reader.readLine());
            BitSet board = new BitSet(n * n);

            maharaja(board, 0, n);

            System.out.println(result.getResult());
            System.out.println(matrix.getResult());

//            System.out.println(System.currentTimeMillis());
        }
    }

    private static void maharaja(BitSet board, int row, int n) {
        if (row == n) {
            solution(board, n);
            return;
        }

        boolean flag = false;
        for (int i = 0; i < n; i++) {
            if (warning(board, row, i, n)) {
                flag = true;
                board.set(row * n + i);
                maharaja(board, row + 1, n);
                board.clear(row * n + i);
            } else if (i == n - 1 && !flag) {
                maharaja(board, row + 1, n);
            }
        }
    }

    private static boolean warning(BitSet board, int row, int column, int n) {
        int[] x = {+2, +1, -1, -2, -2, -1, +1, +2};
        int[] y = {+1, +2, +2, +1, -1, -2, -2, -1};

        for (int i = 0; i < 8; i++) {
            if (
                    row + x[i] >= 0 && row + x[i] < n &&
                            column + y[i] >= 0 && column + y[i] < n
            ) {
                if (board.get((row + x[i]) * n + column + y[i])) {
                    return false;
                }
            }
        }

        for (int i = 0; i < row; i++) {
            if (board.get(i * n + column)) {
                return false;
            }
        }

        for (
                int i = row, j = column;
                i >= 0 && j >= 0 && i < n && j < n;
                i--, j--
        ) {
            if (board.get(i * n + j)) {
                return false;
            }
        }

        for (
                int i = row, j = column;
                i >= 0 && j < n && i < n;
                i--, j++
        ) {
            if (board.get(i * n + j)) {
                return false;
            }
        }

        return true;
    }

    private static final Matrix matrix = new Matrix();
    private static final Result result = new Result(0);

    private static void solution(BitSet board, int n) {
        int counter = board.cardinality();
        if (counter > result.getResult()) {
            result.setResult(counter);
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < n * n; i++) {
                result.append(board.get(i) ? " M " : " - ");
                if (i % n == n - 1) {
                    result.append("\n");
                }
            }
            matrix.setResult(result);
        }
        if (counter == n) {
            System.out.println(result.getResult());
            System.out.println(matrix.getResult());
            System.exit(0);
        }
    }
}

class Matrix {

    private StringBuilder result;

    public Matrix() {
    }

    public void setResult(StringBuilder result) {
        this.result = result;
    }

    public StringBuilder getResult() {
        return result;
    }
}

class Result {

    private Integer value;

    public Result(int value) {
        this.value = value;
    }

    public void setResult(Integer value) {
        this.value = value;
    }

    public Integer getResult() {
        return value;
    }
}

