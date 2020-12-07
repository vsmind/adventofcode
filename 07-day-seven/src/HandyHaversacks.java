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

            //int count = 0;
            HashSet<String> search = new HashSet<>();
            HashSet<String> allSearched = new HashSet<>();
            search.add("shiny gold");
            //System.out.println("************************************");
            //System.out.println("Count: " + bottomUp(count, allBags.values(), search, allSearched));
            //findShinyGoldBag(allBags);

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

    public static int bottomUp(int count, Collection<Bags> allBags, HashSet<String> search, HashSet<String> allSearched) {
        HashSet<String> theNewSearch = new HashSet<>();
        for (String srch: search){
            if (!allSearched.contains(srch)) {
            for (Bags bags: allBags) {
                if (bags.bagContent.containsKey(srch)){
                    System.out.println(bags.bagColorCode);
                    theNewSearch.add(bags.bagColorCode);
                    count++;
                }
            }
            }
        }
        System.out.println("//////////////////////////////////");
        System.out.println("new search " + theNewSearch);
        System.out.println("allSearched " + allSearched);
        System.out.println("allSearched " + allSearched.size());
        allSearched.addAll(search);
        if (theNewSearch.isEmpty()) {
            System.out.println("return count is:" + count);
            return count;
        } else {
            bottomUp(count, allBags, theNewSearch, allSearched);
        }
        return count;
    }

    public static void parseRules(List<String> bagRules, HashMap<String, Bags> allBags) {
        for (String rule: bagRules) {
            String[] ruleDeclaration = rule.split("contain");
            String bagColorCode = ruleDeclaration[0].replace("bags", "").trim();
            HashMap<String, Integer> bagsMap = new HashMap<>();
            Bags bag = new Bags(bagColorCode, bagsMap);
            bag.getBagsContain(ruleDeclaration[1]);
            System.out.println("@@@@@@@@@@@@@@@@@@@@@@@@@@");
            System.out.println(bag.bagColorCode);
            System.out.println(bag.bagContent);
            System.out.println("@@@@@@@@@@@@@@@@@@@@@@@@@@");
            allBags.put(bag.bagColorCode, bag);
        }
    }

//    public static void findShinyGoldBag(HashMap<String, Bags> allBags) {
//        int numberOfBagColorsThatCanEventuallyContainAtLeastOneShinyGoldBag = 0;
//        for (Bags bag: allBags.values()) {
//            numberOfBagColorsThatCanEventuallyContainAtLeastOneShinyGoldBag = numberOfBagColorsThatCanEventuallyContainAtLeastOneShinyGoldBag
//                    + checkBags(bag, allBags);
//        }
//
//        System.out.println("Number of bag colors that can eventually contain at least one shiny gold bag is: "
//                + numberOfBagColorsThatCanEventuallyContainAtLeastOneShinyGoldBag);
//    }

//    public static int checkBags(Bags bag, HashMap<String, Bags> allBags) {
//            for (String bagColor: bag.bagContent.keySet()) {
//                Bags bagToCheck = allBags.get(bagColor);
//                if (bagToCheck.bagContent.containsKey("shiny gold")) {
//                    return 1;
//                } else {
//                    checkBags(bagToCheck, allBags);
//                }
//            }
//        return 0;
//    }

}
