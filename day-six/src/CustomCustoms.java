import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class CustomCustoms {


    public static void main(String[] args) {
        String inputFile = "day-six/src/input";
        //String inputFile = "day-six/src/inputTest";

        try (Stream<String> stream = Files.lines(Paths.get(inputFile))){
            List<String> declarations = stream.collect(Collectors.toList());
            declarations.add("");
            checkDeclarations(declarations);

        } catch (IOException e) {
            e.printStackTrace();
        }

        getCustomDeclarationForm();

    }

    public static void checkDeclarations(List<String> declarations) {
        Map<Character, Integer> groupDeclaration = getCustomDeclarationForm();
        int numberOfYesForAll = 0;
        System.out.println(declarations);
        for (String declaration: declarations) {
            System.out.println(declaration);
            if (!declaration.equals("")) {
                for (char question: declaration.toCharArray()) {
                    groupDeclaration.put(question, 1);
                }
            } else {
                int numberOfYesForGroup = getNumberOfYesAnswers(groupDeclaration);
                System.out.println("GROUP Yes: " +  numberOfYesForGroup);
                numberOfYesForAll = numberOfYesForAll + numberOfYesForGroup;
                groupDeclaration = getCustomDeclarationForm();
            }
        }

        System.out.println("SUM OF YES FOR ALL :" + numberOfYesForAll);
    }

    public static int getNumberOfYesAnswers(Map<Character, Integer> groupDeclaration) {
        return groupDeclaration.values().stream().mapToInt(Integer::intValue).sum();
    }

    public static Map<Character, Integer> getCustomDeclarationForm(){
        Map<Character, Integer> customDeclarationForm = new HashMap<>();

        for (int i = 97; i < 123; i++) {
            customDeclarationForm.put( (char)i, 0);
        }

        return customDeclarationForm;
    }
}
