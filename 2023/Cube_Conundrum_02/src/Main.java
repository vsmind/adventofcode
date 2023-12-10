public class Main {
    public static void main(String[] args) {
        int sumId = findSumOfIds(InputData.input); //2879

        System.out.println("Sum of the games ids: " + sumId);
    }

    public static int findSumOfIds(String puzzleInput){
        int sumId = 0;

        for (String line : puzzleInput.split("\n")) {
            String[] gameInput = line.split(":");
            String id = gameInput[0].split(" ")[1];
            String[] setOfCubes = gameInput[1].split(";");
            boolean addId = true;
            for (String cubes : setOfCubes) {
                String[] sets = cubes.split(",");
                //System.out.println(Arrays.stream(sets).toList());
                for (String set : sets) {
                    String[] cube = set.trim().split(" ");
                    System.out.println(cube[0] + " " + cube[1]);
                    switch (cube[1]) {
                        case "red":
                            if (checkLimits(Integer.parseInt(cube[0]), 12)) {
                                addId = false;
                            }
                            break;
                        case "green":
                            if (checkLimits(Integer.parseInt(cube[0]), 13)) {
                                addId = false;
                            }
                            break;
                        case "blue":
                            if (checkLimits(Integer.parseInt(cube[0]), 14)) {
                                addId = false;
                            }
                            break;
                    }
                }
            }
            if (addId) {
                sumId += Integer.parseInt(id);
            }
        }
        return sumId;
    }

    public static boolean checkLimits(int numberOfDice, int diceLimit) {
        return numberOfDice > diceLimit;
    }
}