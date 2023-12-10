import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        //int sumId = findSumOfIds(InputData.input); //2879
        //System.out.println("Sum of the games ids: " + sumId);

        int powerOfCubes = powerOfCubes(InputData.input);
        System.out.println("Power of cubes: " + powerOfCubes);
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

    public static int powerOfCubes(String puzzleInput){
        int powerOfCubes = 0;
        for (String line : puzzleInput.split("\n")) {
            String[] setOfCubes = line.split(":")[1].split(";");
            int red = 0;
            int green = 0;
            int blue = 0;
            for (String cubes : setOfCubes) {
                String[] sets = cubes.split(",");
                for (String set : sets) {
                    String[] cube = set.trim().split(" ");
                    switch (cube[1]) {
                        case "red":
                            if (Integer.parseInt(cube[0]) > red) {
                                red = Integer.parseInt(cube[0]);
                            }
                            break;
                        case "green":
                            if (Integer.parseInt(cube[0]) > green) {
                                green = Integer.parseInt(cube[0]);
                            }
                            break;
                        case "blue":
                            if (Integer.parseInt(cube[0]) > blue) {
                                blue = Integer.parseInt(cube[0]);
                            }
                            break;
                    }
                }
            }
            System.out.println("Red: " + red + " Green: " + green + " Blue: " + blue);
            System.out.println("Power of cubes: " + (red * green * blue));
            powerOfCubes += red * green * blue;
        }
        return powerOfCubes;
    }

    public static boolean checkLimits(int numberOfDice, int diceLimit) {
        return numberOfDice > diceLimit;
    }
}