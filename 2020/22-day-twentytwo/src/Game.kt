class Game(val player1: Player, val player2: Player) {

    fun start() {
        var roundOutput = 1
        while (player1.getNumberOfCards() != 0 && player2.getNumberOfCards() != 0) {
            println("-- Round $roundOutput --")

            println("Player 1's deck: " + player1.printCards())
            println("Player 2's deck: " + player2.printCards())

            val playerOneCard = player1.getFirstCard()
            val playerTwoCard = player2.getFirstCard()

            println("Player 1 plays: $playerOneCard")
            println("Player 2 plays: $playerTwoCard")

            if (playerOneCard > playerTwoCard) {
                player1.addCard(playerOneCard)
                player1.addCard(playerTwoCard)
                println("Player 1 wins the round!")
            } else {
                player2.addCard(playerTwoCard)
                player2.addCard(playerOneCard)
                println("Player 2 wins the round!")
            }
            roundOutput++
        }

        println("== Post-game results ==")

        val deck1 = player1.printCards()
        val deck2 = player2.printCards()

        println("Player 1's deck: $deck1")
        println("Player 2's deck: $deck2")

        if (player1.getNumberOfCards() != 0 ) {
            println("winning player's score is " +  player1.calculateScore())
        } else {
            println("winning player's score is " +  player2.calculateScore())
        }
    }

}