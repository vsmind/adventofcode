import java.io.File
import java.io.FileOutputStream

fun main() {
    //Test input
    //val input = readInput("08-day-eight/src/inputTest")
    val input = readInput("08-day-eight/src/input")

    val originalInstructionList: MutableList<Instruction> = prepareOriginalInstructionsList(input)
    val possiblyBrokenInstructionsList: List<Instruction> = originalInstructionList.map { it.copy() }

    val instructionsCopy: List<Instruction> = originalInstructionList.map { it.copy() }
    //Part-one
    calculateAccumulatorValue(instructionsCopy)

    findAccumulatorValueAfterFix(originalInstructionList, possiblyBrokenInstructionsList)
}

// Part-two
fun findAccumulatorValueAfterFix(originalInstructionList: List<Instruction>,
                                 possiblyBrokenInstructionsList: List<Instruction>) {
    for ((index, value) in possiblyBrokenInstructionsList.withIndex()) {
        val instructionsCopy: List<Instruction> = originalInstructionList.map { it.copy() }

        if (value.operation != "acc") {
            reverseInstruction(instructionsCopy, index)
            calculateAccumulatorValue(instructionsCopy)
        }
    }
}

// Part-one
fun calculateAccumulatorValue(instructions: List<Instruction>) {
    var accumulator = 0
    var position = 0
    var runProgram = true

    while (runProgram) {
        val currentInstruction = instructions[position]

        if (currentInstruction.runs < 1) {
            when (currentInstruction.operation) {
                "nop" -> {
                    position = nopInstruction(currentInstruction, position)
                }
                "acc" -> {
                    position += 1
                    accumulator = accInstruction(currentInstruction, accumulator)
                }
                "jmp" -> {
                    position = jumpInstruction(currentInstruction, position)
                }
            }
        } else {
            runProgram = false
            println("Accumulator: $accumulator - position: $position")

//            FileOutputStream("08-day-eight/src/output", true).bufferedWriter().use { writer ->
//                writer.append("Accumulator: $accumulator - position: $position")
//                        .appendLine()
//            }
        }

        if (position == instructions.size) {
            runProgram = false
            println("***********************************************************")
            println("Value of the accumulator after the program terminates: $accumulator")
            println("***********************************************************")

            FileOutputStream("08-day-eight/src/output", true).bufferedWriter().use { writer ->
                writer.append("Value of the accumulator after the program terminates: $accumulator")
                        .append(" position: $position")
                        .appendLine()
            }
        }
    }
}

fun nopInstruction(currentInstruction: Instruction, position: Int): Int {
    currentInstruction.runs++
    return position + 1
}

fun accInstruction(currentInstruction: Instruction, accumulator: Int): Int {
    currentInstruction.runs++
    return if (currentInstruction.direction == "+")
        accumulator + currentInstruction.argument
    else
        accumulator - currentInstruction.argument
}

fun jumpInstruction(currentInstruction: Instruction,
                    position: Int): Int {
    return if (currentInstruction.direction == "+")
        position + currentInstruction.argument
    else
        position - currentInstruction.argument
}

fun reverseInstruction(instructions: List<Instruction>, positionToReverse: Int) {
    if (instructions[positionToReverse].operation == "jmp")
        instructions[positionToReverse].operation = "nop"
    else
        instructions[positionToReverse].operation = "jmp"
}

fun readInput(filename: String): List<String> = File(filename).useLines { it.toList() }

fun prepareOriginalInstructionsList(input: List<String>): MutableList<Instruction> {
    val instructionList: MutableList<Instruction> = mutableListOf()
    for (instruction in input) {
        val readInstruction = instruction.split(" ")
        val instructionFromInput = Instruction(readInstruction[0],
                readInstruction[1].substring(0, 1),
                readInstruction[1].substring(1).toInt(),
                0)
        instructionList.add(instructionFromInput)
    }
    return instructionList
}