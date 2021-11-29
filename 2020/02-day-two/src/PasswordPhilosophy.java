import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class PasswordPhilosophy {

    public static void main(String[] args) {
        //String testFile = "02-day-two/src/testInput";
        String passwordFile = "02-day-two/src/passwordDatabase";

        int validPasswords = 0;
        int validPasswordsPartTwo = 0;

        try (Stream<String> stream = Files.lines(Paths.get(passwordFile))){
            List<String> passwordsList = stream.collect(Collectors.toList());

            for (String password: passwordsList) {
                String[] stringToProcess = password.split(":");
                String[] work = stringToProcess[0].split(" ");
                String[] minmax = work[0].split("-");

                int min = Integer.parseInt(minmax[0]);
                int max = Integer.parseInt(minmax[1]);
                String token = work[1];

                PasswordDatabaseEntity entity = new PasswordDatabaseEntity(min, max, token.toCharArray()[0], stringToProcess[1].trim());

                if (checkPassword(entity)){
                    validPasswords++;
                }

                if (checkNewInterpretation(entity)) {
                    validPasswordsPartTwo++;
                }
            }

            System.out.println("Valid passwords:                " + validPasswords);
            System.out.println("Valid passwords with new rule:  " + validPasswordsPartTwo);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static boolean checkPassword(PasswordDatabaseEntity entity) {
        long numberOfChars = entity.getPassword().chars().filter(ch -> ch == entity.getLetter()).count();
        return numberOfChars >= entity.getMinRule() && numberOfChars <= entity.getMaxRule();
    }

    private static boolean checkNewInterpretation(PasswordDatabaseEntity entity) {
        int occurrences = 0;
        if (entity.getPassword().toCharArray()[entity.getMinRule() - 1] == entity.getLetter()) {
            occurrences++;
        }
        if (entity.getPassword().toCharArray()[entity.getMaxRule() - 1] == entity.getLetter()) {
            occurrences++;
        }
        return occurrences == 1;
    }

}
