import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class HandyHaversacks {
    public static void main(String[] args) {
        String inputFile = "07-day-seven/src/input";
        //String inputFile = "07-day-seven/src/inputPart2";
        //String inputFile = "07-day-seven/src/inputTest";

        try (Stream<String> stream = Files.lines(Paths.get(inputFile))){
            List<String> bagRules = stream.collect(Collectors.toList());
            HashMap<String, Bags> allBags = new HashMap<>();
            parseRules(bagRules, allBags);

            HashSet<String> search = new HashSet<>();
            HashSet<String> allSearched = new HashSet<>();
            search.add("shiny gold");

            /*Part one
            int count = 0;
            System.out.println("************************************");
            System.out.println("Count: " + bottomUp(count, allBags.values(), search, allSearched));
            findShinyGoldBag(allBags);*/

            LinkedList<Bags> searchNumber = new LinkedList<>();
            searchNumber.add(allBags.get("shiny gold"));
            LinkedList<Bags> totalBags = new LinkedList<>();
            numberOfBags(allBags, searchNumber, totalBags);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void numberOfBags(HashMap<String, Bags> allBag, LinkedList<Bags> search, LinkedList<Bags> totalBags) {
        LinkedList<Bags> nextIteration = new LinkedList<>();
        for (Bags bag: search) {
            for (Map.Entry<String, Integer> entry: bag.bagContent.entrySet())     {
                for (int i = 0; i < entry.getValue(); i++) {
                    Bags bagForNextSearch = allBag.get(entry.getKey());
                    totalBags.add(bagForNextSearch);
                    nextIteration.add(bagForNextSearch);
                }
            }
        }
        if (!nextIteration.isEmpty()) {
            numberOfBags(allBag, nextIteration, totalBags);
        } else {
            System.out.println(totalBags.size());
        }
    }

    //part one
    private static int bottomUp(int count, Collection<Bags> allBags, HashSet<String> search, HashSet<String> allSearched) {
        HashSet<String> theNewSearch = new HashSet<>();
        for (String srch: search){
            if (!allSearched.contains(srch)) {
            for (Bags bags: allBags) {
                if (bags.bagContent.containsKey(srch)){
                    theNewSearch.add(bags.bagColorCode);
                    count++;
                }
            }
            }
        }
        allSearched.addAll(search);
        if (theNewSearch.isEmpty()) {
            return count;
        } else {
            bottomUp(count, allBags, theNewSearch, allSearched);
        }
        return count;
    }

    private static void parseRules(List<String> bagRules, HashMap<String, Bags> allBags) {
        for (String rule: bagRules) {
            String[] ruleDeclaration = rule.split("contain");
            String bagColorCode = ruleDeclaration[0].replace("bags", "").trim();
            HashMap<String, Integer> bagsMap = new HashMap<>();
            Bags bag = new Bags(bagColorCode, bagsMap);
            bag.getBagsContain(ruleDeclaration[1]);
            allBags.put(bag.bagColorCode, bag);
        }
    }
}
