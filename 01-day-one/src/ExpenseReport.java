import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ExpenseReport {

    public static void main(String[] args) {
        String expenseReportFilePath = "01-day-one/src/input";
        //String expenseReportFilePath = "01-day-one/src/testInput";

        try (Stream<String> stream = Files.lines(Paths.get(expenseReportFilePath))){
            List<Integer> expenses = stream.map(Integer::parseInt)
                    .collect(Collectors.toList());
            System.out.println("The product of the three entries that sum to 2020: " + findEntries(expenses));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static int findEntries(List<Integer> expenses) {
        for (Integer expense: expenses ) {
            for (Integer expenseCopy: expenses) {
                for (Integer expenseCopyTwo: expenses) {
                    if (expense + expenseCopy + expenseCopyTwo == 2020) {
                        return expense * expenseCopy * expenseCopyTwo;
                    }
                }
            }
        }
        return 0;
    }
}
