import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class PassportProcessing {

    public static void main(String[] args) {
        String inputFile = "day-four/src/input";
        //String inputFile = "day-four/src/inputTest";
        List<Map<String, String>> allPassports = new LinkedList<>();

        try (Stream<String> stream = Files.lines(Paths.get(inputFile))){
            List<String> passportData = stream.collect(Collectors.toList());
            readPassportData(passportData, allPassports);
            //System.out.println(passportData.get(passportData.size() - 1));
            System.out.println("Valid passports: " + findValidPassports(allPassports));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void readPassportData(List<String> passportData, List<Map<String, String>> allPassports){
        int allData = 0;
        Map<String, String> passData = new HashMap<String, String>();;
        for (String passportLine: passportData) {
            System.out.println(passportLine);
            if (passportLine.equals("")) {
                allPassports.add(passData);
                passData = new HashMap<String, String>();
                allData++;
            }
            if (!passportLine.equals("")) {
                String[] passportFields = passportLine.split(" ");
                for (String field: passportFields) {
                    String[] passFields = field.split(":");
                    passData.put(passFields[0], passFields[1]);
                }
            }
        }
        allPassports.add(passData);

        System.out.println("Total data read: " + (allData + 1));
    }

    private static int findValidPassports(List<Map<String, String>> allPassports) {
        int numberOfPass = 0;
        int numberOfNPC = 0;
        int numberOfBad = 0;
        for (Map<String, String> pass: allPassports) {
            if ((pass.containsKey("byr") && (Integer.parseInt(pass.get("byr")) >= 1920) && (Integer.parseInt(pass.get("byr")) <= 2002))
                    && (pass.containsKey("iyr") && (Integer.parseInt(pass.get("iyr")) >= 2010) && (Integer.parseInt(pass.get("iyr")) <= 2020))
                    && (pass.containsKey("eyr") && (Integer.parseInt(pass.get("eyr")) >= 2020) && (Integer.parseInt(pass.get("eyr")) <= 2030))
                    && (pass.containsKey("hgt") &&
                    (
                            (
                                    pass.get("hgt").matches("[0-9]{3}cm")
                                            && (Integer.parseInt(pass.get("hgt").substring(0, 3)) >= 150)
                                            && (Integer.parseInt(pass.get("hgt").substring(0, 3)) <= 193)

                            )
                                    ||
                                    (
                                            pass.get("hgt").matches("[0-9]{2}in")
                                                    && (Integer.parseInt(pass.get("hgt").substring(0, 2)) >= 59)
                                                    && (Integer.parseInt(pass.get("hgt").substring(0, 2)) <= 76)
                                    )
                    )
            )
                    && (
                    pass.containsKey("hcl")
                            && pass.get("hcl").matches("#[0-9a-f]{6}")
            )
                    && (
                    pass.containsKey("ecl")
                            && pass.get("ecl").matches("\\b(amb|blu|brn|gry|grn|hzl|oth)\\b")
            )
                    && (pass.containsKey("pid")
                        && pass.get("pid").matches("\\d{9}")

            )
            ) {
                if ( pass.containsKey("cid")) {
                    numberOfPass++;
                    //System.out.println(pass.keySet());
                } else {
                    //System.out.println("North Pole Credentials");
                    //System.out.println(pass.keySet());
                    numberOfPass++;
                    numberOfNPC++;
                }
            } else {
                //System.out.println("Not a vailid pass");
                //System.out.println(pass.keySet());
                numberOfBad++;
            }
        }
        System.out.println("North Pole Credentials: " + numberOfNPC);
        System.out.println("Bad pass: " + numberOfBad);
        return numberOfPass;
    }

}
