import java.io.File

fun main() {
    //val input = readInput("13-day-thirteen/src/inputTest")
    val input = readInput("13-day-thirteen/src/input")
    val earliestTimestamp = input[0].toInt()
    val busDeparture = input[1].replace("x","")
            .replace(",", " ")
            .split(" ")
            .filter { it != "" }
            .toTypedArray()
            .map { it.toInt() }

    findBus(busDeparture, earliestTimestamp)
}

fun findBus(busDeparture: List<Int>, earliestTimestamp: Int) {
    val timeList = mutableListOf<Bus>()
    for (bus in busDeparture) {
        var time = bus
        while (time < earliestTimestamp) {
            time+=bus
        }

        timeList.add(Bus(bus, time % earliestTimestamp))
    }

    timeList.sortBy { it.timeList }
    val bus = timeList.first()
    println("ID of the earliest bus you can take to the airport multiplied by the number of minutes: " + bus.busNumber * bus.timeList)
}

fun readInput(filename: String): List<String> = File(filename).useLines { it.toList() }

data class Bus(val busNumber: Int, val timeList: Int)