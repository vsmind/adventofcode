import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class BinaryBoarding {

    public static void main(String[] args) {
        String inputFile = "day-five/src/input";
        //String inputFile = "day-five/src/inputTest";
        //String inputFile = "day-five/src/inputExample";
        ArrayList<Integer> seatIds = new ArrayList<>();

        try (Stream<String> stream = Files.lines(Paths.get(inputFile))){
            List<String> partitions = stream.collect(Collectors.toList());
            for (String partition: partitions) {
                changeRange(partition, seatIds);
            }
            System.out.println(Collections.max(seatIds));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void changeRange(String partition, ArrayList<Integer> seats) {
        int minRange = 0;
        int maxRange = 127;
        int half = 64;
        int minSeat = 0;
        int maxSeat = 7;
        int halfSeat = 4;
        for (char place: partition.toCharArray()) {
            if (place == 'F') {
                maxRange = maxRange - half;
                half = half / 2;
            }
            if (place == 'B') {
                minRange = minRange + half;
                half = half / 2;
            }
            if (place == 'L') {
                // lower half
                maxSeat = maxSeat - halfSeat;
                halfSeat = halfSeat / 2;
            }
            if (place == 'R') {
                // upper half
                minSeat = minSeat + halfSeat;
                halfSeat = halfSeat / 2;
            }

            if (minRange == maxRange && minSeat == maxSeat) {
                seats.add(seatID(minRange, minSeat));
            }
        }
    }

    public static int seatID(int row, int column) {
        return row * 8 + column;
    }
}
