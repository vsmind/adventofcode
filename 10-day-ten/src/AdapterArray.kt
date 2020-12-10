import java.io.File

fun main() {
    val adaptersList = readInput("10-day-ten/src/inputTestSmall")
    //val adaptersList = readInput("10-day-ten/src/inputTest")
    //val adaptersList = readInput("10-day-ten/src/input")
    println(adaptersList)
}

fun readInput(filename: String): List<Int> = File(filename).useLines { it.toList() }.map { it.toInt() }
