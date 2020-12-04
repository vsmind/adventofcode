import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ExpenseReport {

    public static void main(String[] args) {
        String expenseReportFilePath = "day-one/src/input";
        //String expenseReportFilePath = "src/testInput";

        try (Stream<String> stream = Files.lines(Paths.get(expenseReportFilePath))){
            List<Integer> expenses = stream.map(Integer::parseInt)
                    .collect(Collectors.toList());
            List<Integer> expensesCopy = expenses;
            List<Integer> expensesCopyTwo = expenses;

            for (Integer expense: expenses ) {
                for (Integer expenseCopy: expensesCopy) {
                    for (Integer expenseCopyTwo: expensesCopyTwo) {
                        if (expense + expenseCopy + expenseCopyTwo == 2020) {
                            System.out.println(expense);
                            System.out.println(expenseCopy);
                            System.out.println(expenseCopyTwo);
                            System.out.println(expense * expenseCopy * expenseCopyTwo);
                        }
                    }
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
