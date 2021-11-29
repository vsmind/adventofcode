import java.io.File

fun main() {
    //val input = readInput("22-day-twentytwo/src/inputTest")
    val input = readInput("22-day-twentytwo/src/input")
    val players = mutableListOf<Player>()

    parseInput(input, players)

    val game = Game(players[0], players[1])
    game.start()
}

fun parseInput(inputString: List<String>, players: MutableList<Player>) {
    var playerIndex = 0
    for (line in inputString) {
        if (line.startsWith("Player")) {
            players.add(Player(line))
        }
        else if (line != "") {
            players[playerIndex].addCard(line.toInt())
        }
        if (line == "") {
            playerIndex++
        }
    }
}

fun readInput(filename: String): List<String> = File(filename).useLines { it.toList() }