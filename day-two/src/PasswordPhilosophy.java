import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class PasswordPhilosophy {

    public static void main(String[] args) {
        List<PasswordDatabaseEntity> passwords = new LinkedList<>();

        String testFile = "day-two/src/testInput";
        String passwordFile = "day-two/src/passwordDatabase";

        int validPasswords = 0;
        int validPasswordsNewRule = 0;

        try (Stream<String> stream = Files.lines(Paths.get(passwordFile))){
            List<String> passwordsList = stream.collect(Collectors.toList());

            for (String password: passwordsList) {
                //System.out.println(password);
                String[] stringToProcess = password.split(":");
                //System.out.println("Part1 | " + stringToProcess[0]);
                //System.out.println("Part2 | " + stringToProcess[1]);

                String[] work = stringToProcess[0].split(" ");
                //System.out.println("Part3 | " + work[0]);
                //System.out.println("Part4 | " + work[1]);

                String[] minmax = work[0].split("-");

                int min = Integer.parseInt(minmax[0]);
                int max = Integer.parseInt(minmax[1]);
                String token = work[1];

                PasswordDatabaseEntity entity = new PasswordDatabaseEntity(min, max, token.toCharArray()[0], stringToProcess[1].trim());

                System.out.println(entity.toString());

                if (checkPassword(entity)){
                    validPasswords++;
                }

                if (checkNewInterpretation(entity)) {
                    validPasswordsNewRule++;
                }
            }

            System.out.println("Valid passwords: " + validPasswords);
            System.out.println("Valid passwords new rule: " + validPasswordsNewRule);


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
