import java.io.File

fun main() {
    //var adaptersList = readInput("10-day-ten/src/inputTestSmall")
    //val adaptersList = readInput("10-day-ten/src/inputTest")
    val adaptersList = readInput("10-day-ten/src/input")
    println(adaptersList)

    val joltageOne = mutableListOf<Int>()
    val joltageThree = mutableListOf<Int>()

    adaptersList.maxOrNull()?.plus(3)?.let { adaptersList.add(it) }
    getJoltDifference(adaptersList, joltageOne, joltageThree)

    findJoltageValue(joltageOne, joltageThree)
}

fun getJoltDifference(adaptersList: List<Int>,
                      joltageOne: MutableList<Int>,
                      joltageThree: MutableList<Int>) {
    var prevJoltage = 0

    adaptersList.sorted().forEach {
        when (it - prevJoltage) {
            1 -> joltageOne.add(it)
            3 -> joltageThree.add(it)
        }
        prevJoltage = it
    }

    println(joltageOne.size)
    println(joltageThree.size)
}

fun findJoltageValue(joltageOne: MutableList<Int>,
                     joltageThree: MutableList<Int>) {
    println("Number of 1-jolt differences multiplied by the number of 3-jolt differences: " + (joltageOne.size * joltageThree.size))
}

fun readInput(filename: String): MutableList<Int> = File(filename).useLines { it.toList() }.map { it.toInt() }.toMutableList()
