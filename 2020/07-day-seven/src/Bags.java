import java.util.HashMap;

public class Bags {

    final String bagColorCode;
    HashMap<String, Integer> bagContent;

    public Bags(String bagColorCode, HashMap<String, Integer> bagsContent) {
        this.bagColorCode = bagColorCode;
        this.bagContent = bagsContent;
    }

    public void getBagsContain(String bagsInBag) {
        if (bagsInBag.equals(" no other bags.")) {
            System.out.println("this bag has no other bags");
        } else {
            String[] bags = bagsInBag.split(",");
            for (String bag: bags) {
                int numberOfBags = Integer.parseInt(bag.substring(1,2));
                String typeOfBags;
                if (numberOfBags == 1) {
                    typeOfBags = bag.substring(2).replace(".","").replace("bag", "").trim();
                } else {
                    typeOfBags = bag.substring(2).replace(".","").replace("bags", "").trim();
                }
                bagContent.put(typeOfBags, numberOfBags);
            }
        }
    }
}
