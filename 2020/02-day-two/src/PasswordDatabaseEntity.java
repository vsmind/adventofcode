public class PasswordDatabaseEntity {

    private final int minRule;
    private final int maxRule;
    private final char letter;
    private final String password;

    public PasswordDatabaseEntity(int minRule, int maxRule, char letter, String password) {
        this.minRule = minRule;
        this.maxRule = maxRule;
        this.letter = letter;
        this.password = password;
    }

    public int getMinRule() {
        return minRule;
    }

    public int getMaxRule() {
        return maxRule;
    }

    public char getLetter() {
        return letter;
    }

    public String getPassword() {
        return password;
    }

    @Override
    public String toString() {
        return "PasswordDatabaseEntity{" +
                "minRule=" + minRule +
                ", maxRule=" + maxRule +
                ", letter='" + letter + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
