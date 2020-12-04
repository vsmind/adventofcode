public class PasswordDatabaseEntity {

    private int minRule;
    private int maxRule;
    private char letter;
    private String password;

    public PasswordDatabaseEntity(int minRule, int maxRule, char letter, String password) {
        this.minRule = minRule;
        this.maxRule = maxRule;
        this.letter = letter;
        this.password = password;
    }

    public int getMinRule() {
        return minRule;
    }

    public void setMinRule(int minRule) {
        this.minRule = minRule;
    }

    public int getMaxRule() {
        return maxRule;
    }

    public void setMaxRule(int maxRule) {
        this.maxRule = maxRule;
    }

    public char getLetter() {
        return letter;
    }

    public void setLetter(char letter) {
        this.letter = letter;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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
