import java.io.File

fun main(){
    //val input = readInput("14-day-fourteen/src/inputTest")
    val input = readInput("14-day-fourteen/src/input")
    val results = readDockingData(input)

    println("Sum of all values left in memory after it completes: " + results.toMap().values.sum())
}

fun readDockingData(input: List<String>) : MutableMap<String, Long> {
    var mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    val memory = mutableMapOf<String, Long>()

    for (inputLine in input) {
        when {
            inputLine.startsWith("mask") -> {
                mask = changeMask(inputLine)
            }
            inputLine.startsWith("mem") -> {
                val memoryLine = readValue(inputLine)
                val memoryPosition = memoryLine[0].replace("[^\\d.]", "")
                val value = memoryLine[1]
                val valueWithMask = applyMaskToTheValue(value, mask)
                val convertedValueWithMask = convertBinaryToInt(valueWithMask)
                memory[memoryPosition] = convertedValueWithMask
            }
            else -> {
                println("Unsupported command")
            }
        }
    }
    return memory
}

fun convertBinaryToInt(value: String) : Long {
    return value.toLong(2)
}

fun applyMaskToTheValue(value: String, mask: String) : String {
    val valueInt = value.toInt().to36bitString()

    for ((index, char) in mask.withIndex()) {
        if (char != 'X') {
            valueInt[index] = char
        }
    }

    return String(valueInt)
}

fun readValue(inputLine: String): List<String> {
    return inputLine.split(" = ")
}

fun changeMask(inputLine: String): String {
    return inputLine.split(" = ")[1]
}

fun Int.to36bitString(): CharArray =
        Integer.toBinaryString(this).padStart(36, '0').toCharArray()

fun readInput(filename: String): List<String> = File(filename).useLines { it.toList() }

