import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class CustomCustoms {


    public static void main(String[] args) {
        String inputFile = "06-day-six/src/input";
        //String inputFile = "06-day-six/src/inputTest";

        try (Stream<String> stream = Files.lines(Paths.get(inputFile))){
            List<String> declarations = stream.collect(Collectors.toList());
            declarations.add("");
            checkDeclarations(declarations);
        } catch (IOException e) {
            e.printStackTrace();
        }

        getCustomDeclarationForm();
    }

    private static void checkDeclarations(List<String> declarations) {
        Map<Character, Integer> groupDeclaration = getCustomDeclarationForm();
        int numberOfYesForAll = 0;
        int numberOfPeople = 0;
        for (String declaration: declarations) {
            if (!declaration.equals("")) {
                for (char question: declaration.toCharArray()) {
                    groupDeclaration.put(question, groupDeclaration.get(question) + 1);
                }
                numberOfPeople++;
            } else {
                //int numberOfYesForGroup = getNumberOfYesAnswers(groupDeclaration);
                int numberOfYesForGroup = getNumberOfYesAnswersForEveryone(groupDeclaration, numberOfPeople);
                //System.out.println("GROUP Yes: " +  numberOfYesForGroup);
                numberOfYesForAll = numberOfYesForAll + numberOfYesForGroup;
                numberOfPeople = 0;
                groupDeclaration = getCustomDeclarationForm();
            }
        }
        System.out.println("SUM OF YES FOR ALL:    " + numberOfYesForAll);
    }

    // Part one
    private static int getNumberOfYesAnswers(Map<Character, Integer> groupDeclaration) {
        return groupDeclaration.values().stream().mapToInt(Integer::intValue).sum();
    }

    private static int getNumberOfYesAnswersForEveryone(Map<Character, Integer> groupDeclaration, int numberOfPeople) {
        return groupDeclaration.values().stream()
                .filter(i -> i == numberOfPeople)
                .map(i -> i / numberOfPeople)
                .mapToInt(Integer::intValue)
                .sum();
    }

    private static Map<Character, Integer> getCustomDeclarationForm(){
        Map<Character, Integer> customDeclarationForm = new HashMap<>();

        for (int i = 97; i < 123; i++) {
            customDeclarationForm.put((char)i, 0);
        }

        return customDeclarationForm;
    }
}
