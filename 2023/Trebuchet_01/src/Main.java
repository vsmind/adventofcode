import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        System.out.println(PuzzleInput.inputTest);

        List<Integer> correctionValues = calibrationValues(PuzzleInput.inputTest);
        Integer sum = correctionValues.stream().reduce(0, Integer::sum);

        System.out.println(calibrationValues(PuzzleInput.inputTest));
        System.out.println(sum);
    }

    private static List<Integer> calibrationValues(String input) {
        return Arrays.stream(input.split("\n"))
                .map(line -> {
                    StringBuilder reversed = new StringBuilder(line).reverse();
                    char firstDigit = line.chars().filter(Character::isDigit).mapToObj(c -> (char) c).findFirst().orElseThrow();
                    char lastDigit = reversed.chars().filter(Character::isDigit).mapToObj(c -> (char) c).findFirst().orElseThrow();
                    return Integer.valueOf(new StringBuilder("").append(firstDigit).append(lastDigit).toString());
                })
                .collect(Collectors.toList());
    }
}