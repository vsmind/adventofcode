import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TobogganTrajectory {

    public static void main(String[] args) {

        int tree11, tree31, tree51, tree71, tree12;
        char[][] map11, map31, map51, map71 ,map12;

        String mapFile = "03-day-three/src/input";
        char[][] map;

        try (Stream<String> stream = Files.lines(Paths.get(mapFile))){
            List<String> mapFromFile = stream.collect(Collectors.toList());

            int mapX = mapFromFile.get(0).length();
            int mapY = mapFromFile.size();

            map = new char[mapX][mapY];
            int currentLine = 0;
            for (String mapElement: mapFromFile) {
                int currentTile = 0;
                for (char maptile: mapElement.toCharArray()) {
                    map[currentTile][currentLine] = maptile;
                    currentTile++;
                }
                currentLine++;
            }

            map11 = map.clone();
            map31 = map.clone();
            map51 = map.clone();
            map71 = map.clone();
            map12 = map.clone();

            tree11 = move(0,0, map11, mapX, mapY, 1, 1);
            tree31 = move(0,0, map31, mapX, mapY, 3, 1);
            tree51 = move(0,0, map51, mapX, mapY, 5, 1);
            tree71 = move(0,0, map71, mapX, mapY, 7, 1);
            tree12 = move(0,0, map12, mapX, mapY, 1, 2);

            BigInteger totalTrees = BigInteger.valueOf(tree11)
                    .multiply(BigInteger.valueOf(tree31))
                    .multiply(BigInteger.valueOf(tree51))
                    .multiply(BigInteger.valueOf(tree71))
                    .multiply(BigInteger.valueOf(tree12));

            System.out.println("All of the Tree: " + totalTrees);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Used in development
    private static void printMap(int maxX, int maxY, char[][] map){
        for (int i = 0; i < maxY; i++){
            for (int j = 0; j < maxX; j++) {
                System.out.print(map[j][i]);
            }
            System.out.println();
        }
    }

    private static int move(int xPos, int yPos, char[][] map, int maxX, int maxY, int stepX, int stepY) {
        int trees = 0;
        for (int y = 0; y < maxY; y++) {
            if (xPos >= maxX)
                xPos = xPos - maxX;
            if (yPos >= maxY)
                return trees;
            trees = trees + changePosition(xPos, yPos, map);
            xPos = xPos + stepX;
            yPos = yPos + stepY;
        }
        return trees;
    }

    private static int changePosition(int xPos, int yPos, char[][] map) {
        if (map[xPos][yPos] == '#' || map[xPos][yPos] == 'X'){
            map[xPos][yPos] = 'X';
            return 1;
        }
        else {
            map[xPos][yPos] = 'O';
            return 0;
        }
    }
}
