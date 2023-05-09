import java.io.BufferedReader;
import java.io.FileReader;
import java.util.BitSet;


public class Maharaja {
    public static long start;

    public static void main(String[] args) throws Exception {
        start = System.currentTimeMillis();
        final String src = "C:/Users/wh1tly337/IdeaProjects/algotitms/src/input.txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(src))) {
            final int n = Integer.parseInt(reader.readLine());
            final BitSet board = new BitSet(n * n);

            maharaja(board, 0, n);

            System.out.println(result.getResult());
            System.out.println(matrix.getResult());

            final double elapsed = (System.currentTimeMillis() - start) * 0.001;
            System.out.println("Прошло времени: " + elapsed);
        }
    }

    //Временная сложность метода `maharaja` равна `O(n ^n)`, где `n` - размер
    // шахматной доски. Это связано с тем, что для каждой строки метод
    // выполняет `n` рекурсивных вызовов, каждый из которых имеет `n-1`,
    // `n-2`, ..., `1` возможных вариантов для позиции Магараджи.
    // Это приводит к коэффициенту ветвления `n` на каждом уровне, а глубина
    // рекурсии равна `n`, поскольку на шахматной доске имеется `n` строк.
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

    public static final int[] x = {-1, -2, -2, -1};
    public static final int[] y = {2, 1, -1, -2};

    //Временная сложность метода "warning" равна "O(n)", поскольку он проверяет
    // каждую ячейку в одной строке, а также не более 8 ячеек по диагоналям,
    // и конь перемещается. Метод `checkDiagonal` также является методом
    // `O(n)`, поскольку он рекурсивно проверяет каждую ячейку на диагонали
    private static boolean warning(BitSet board, int row, int column, int n) {
        for (int i = 0; i < row; i++) {
            if (board.get(i * n + column)) return false;
        }

        if (!checkDiagonal(row - 1, column - 1, -1, -1, n, board)) {
            return false;
        }
        if (!checkDiagonal(row - 1, column + 1, -1, 1, n, board)) {
            return false;
        }

        if (row + x[0] < n && row + x[0] >= 0 && column + y[0] < n && column + y[0] >= 0) {
            if (board.get((row + x[0]) * n + column + y[0])) return false;
        }
        if (row + x[1] < n && row + x[1] >= 0 && column + y[1] < n && column + y[1] >= 0) {
            if (board.get((row + x[1]) * n + column + y[1])) return false;
        }
        if (row + x[2] < n && row + x[2] >= 0 && column + y[2] < n && column + y[2] >= 0) {
            if (board.get((row + x[2]) * n + column + y[2])) return false;
        }
        if (row + x[3] < n && row + x[3] >= 0 && column + y[3] < n && column + y[3] >= 0) {
            return !board.get((row + x[3]) * n + column + y[3]);
        }

        return true;
    }

    private static boolean checkDiagonal(int row, int column, int dirRow, int dirCol, int n, BitSet chessBoard) {
        if (row < 0 || row >= n || column < 0 || column >= n) return true;

        if (chessBoard.get(row * n + column)) return false;

        return checkDiagonal(row + dirRow, column + dirCol, dirRow, dirCol, n, chessBoard);
    }

    private static final Matrix matrix = new Matrix();
    private static final Result result = new Result(0);
    private static final StringBuilder score = new StringBuilder();

    // Временная сложность метода "solution" равна "O (n ^ 2)", поскольку он
    // выполняет итерацию по всем ячейкам шахматной доски,
    // чтобы создать строку результатов.
    private static void solution(BitSet board, int n) {
        int counter = board.cardinality();
        if (counter > result.getResult()) {
            result.setResult(counter);
            score.setLength(0);
            for (int i = 0; i < n * n; i++) {
                score.append(board.get(i) ? " M " : " - ");
                if (i % n == n - 1) {
                    score.append("\n");
                }
            }
            matrix.setResult(score);
        }
        if (counter == n) {
            System.out.println(result.getResult());
            System.out.println(matrix.getResult());

            double elapsed = (System.currentTimeMillis() - start) * 0.001;
            System.out.println("Прошло времени: " + elapsed);

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

    private int value;

    public Result(int value) {
        this.value = value;
    }

    public void setResult(int value) {
        this.value = value;
    }

    public int getResult() {
        return value;
    }
}

//Итог: сложность данного алгоритма  "O(n ^ n)", поскольку "maharaja"
// доминирует во времени выполнения.