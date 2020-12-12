import java.io.File
import kotlin.math.absoluteValue

fun main() {
    //val input = readInput("12-day-twelve/src/inputTest")
    val input = readInput("12-day-twelve/src/input")
    val navigationInstructions = parseNavigationInstructions(input)

    val manhattanDistance = findManhattanDistance(navigationInstructions)
    println("Ship manhattan distance: $manhattanDistance")
}

data class ShipDirections(val directions: Directions, val navigationUnit: Int)

fun findManhattanDistance(shipDirections: List<ShipDirections>) : Int {
    var direction = 90
    var eastWestPosition = 0
    var northSouthPosition = 0

    for (instruction in shipDirections) {
        when(instruction.directions) {
            Directions.NORTH -> northSouthPosition += instruction.navigationUnit
            Directions.SOUTH -> northSouthPosition -= instruction.navigationUnit
            Directions.EAST -> eastWestPosition += instruction.navigationUnit
            Directions.WEST -> eastWestPosition -= instruction.navigationUnit
            Directions.FORWARD -> {
                when(direction) {
                    0 -> northSouthPosition += instruction.navigationUnit
                    180 -> northSouthPosition -= instruction.navigationUnit
                    90 -> eastWestPosition += instruction.navigationUnit
                    270 -> eastWestPosition -= instruction.navigationUnit
                }
            }
            Directions.LEFT -> {
                direction = (360 + direction - instruction.navigationUnit) % 360
                println(direction)
            }
            Directions.RIGHT -> {
                direction = (360 + direction + instruction.navigationUnit) % 360
                println(direction)
            }
            else -> println("Error")
        }
    }

    println("northSouthPosition: " + northSouthPosition.absoluteValue)
    println("eastWestPosition: " + eastWestPosition.absoluteValue)

    return eastWestPosition.absoluteValue + northSouthPosition.absoluteValue
}

fun parseNavigationInstructions(input: List<String>) : List<ShipDirections> {
    val navigationInstructions : MutableList<ShipDirections> = mutableListOf()

    for (inputLine in input) {
        val direction = when(inputLine.subSequence(0, 1)) {
            "N" -> Directions.NORTH
            "S" -> Directions.SOUTH
            "E" -> Directions.EAST
            "W" -> Directions.WEST
            "L" -> Directions.LEFT
            "R" -> Directions.RIGHT
            "F" -> Directions.FORWARD
            else -> Directions.ERROR
        }
        val units = inputLine.substring(1).toInt()
        navigationInstructions.add(ShipDirections(direction, units))
    }
    return navigationInstructions
}

fun readInput(filename: String): List<String> = File(filename).useLines { it.toList() }
