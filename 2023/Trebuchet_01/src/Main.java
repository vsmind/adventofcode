import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        // Puzzle one
        //List<Integer> correctionValues = calibrationValues(PuzzleInput.inputTest);
        //Integer sum = correctionValues.stream().reduce(0, Integer::sum);

        //System.out.println(calibrationValues(PuzzleInput.inputTest));
        //System.out.println(sum);
        // Puzzle two
        List<Integer> values = spelledOutLetters(PuzzleInput.input);
        Integer sum = values.stream().reduce(0, Integer::sum);
        System.out.println("Sum of all of the calibration values is: " + sum);
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

    private static List<Integer> spelledOutLetters(String input) {
        return Arrays.stream(input.split("\n"))
                .map(line -> {
                    int firstDigitPosition = -1;
                    int lastDigitPosition = -1;

                    String firstNumber = "";
                    String lastNumber = "";
                    String[] numbers = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

                    for (int i = 0; i < line.length(); i++) {
                        if (Character.isDigit(line.charAt(i))) {
                            if (firstDigitPosition == -1) {
                                firstDigitPosition = i;
                                firstNumber = String.valueOf(line.charAt(i));
                            }
                            lastDigitPosition = i;
                            lastNumber = String.valueOf(line.charAt(i));
                        }
                    }

//                    System.out.println("Line: " + line);
//                    System.out.println("First digit position: " + firstDigitPosition);
//                    System.out.println("Last digit position: " + lastDigitPosition);

                    int position = firstDigitPosition;
                    for (int i = 0; i < numbers.length; i++) {
                        if (position == -1 && line.contains(numbers[i])) {
                            position = line.indexOf(numbers[i]);
                            firstNumber = String.valueOf(i + 1);
                        }
                        if (line.contains(numbers[i]) && line.indexOf(numbers[i]) < position) {
                            position = line.indexOf(numbers[i]);
                            firstNumber = String.valueOf(i + 1);
                        }
                    }

                    position = lastDigitPosition;
                    for (int i = 0; i < numbers.length; i++) {
                        if (position == -1 && line.contains(numbers[i])) {
                            position = line.lastIndexOf(numbers[i]);
                            lastNumber = String.valueOf(i + 1);
                        }
                        if (line.contains(numbers[i]) && line.lastIndexOf(numbers[i]) > position) {
                            position = line.lastIndexOf(numbers[i]);
                            lastNumber = String.valueOf(i + 1);
                        }
                    }
//                    System.out.println(firstNumber + " " + lastNumber);
                    return Integer.valueOf(new StringBuilder("").append(firstNumber).append(lastNumber).toString());
                })
                .collect(Collectors.toList());
    }
}