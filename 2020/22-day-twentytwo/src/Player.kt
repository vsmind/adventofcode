class Player (val name: String) {

    private val cards = mutableListOf<Int>()

    fun addCard(card: Int) {
        cards.add(card)
    }

    fun getNumberOfCards() : Int {
        return cards.size
    }

    fun getFirstCard() : Int {
        return cards.removeFirst()
    }

    fun printCards(): String {
        return cards.toString()
    }

    fun calculateScore() : Int{
        var score = 0
        var multiplier = 1

        while (cards.size != 0) {
            score += cards.removeLast() * multiplier
            multiplier++
        }
        return score
    }
}