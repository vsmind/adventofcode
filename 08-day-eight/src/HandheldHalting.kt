import java.io.File

fun main(args: Array<String>) {
    //Test input
    //val input = readInput("08-day-eight/src/inputTest")
    val input = readInput("08-day-eight/src/input")
    //println(input)

    val instructionList: MutableList<Instruction> = mutableListOf()

    for (inst in input) {
        val readInstruction = inst.split(" ")
        val instructionFromInput = Instruction(readInstruction[0],
                readInstruction[1].substring(0, 1),
                readInstruction[1].substring(1).toInt(),
                0);
        instructionList.add(instructionFromInput)
    }

    runInstructionsBeforeFirstInfiniteLoop(instructionList)
    //instructionList.forEach(::print);
}

fun runInstructionsBeforeFirstInfiniteLoop(instructions: MutableList<Instruction>) {
    var accumulator = 0
    var startingInstruction = 0
    var runProgram = true
    while (runProgram) {
        val currentInstruction = instructions[startingInstruction]
        if (currentInstruction.runs < 1) {
            when (currentInstruction.operation) {
                "nop" -> startingInstruction++;
                "acc" -> {
                    startingInstruction++
                    if (currentInstruction.direction == "+")
                        accumulator += currentInstruction.argument
                    else
                        accumulator -= currentInstruction.argument
                }
                "jmp" -> if (currentInstruction.direction == "+")
                    startingInstruction += currentInstruction.argument
                else
                    startingInstruction -= currentInstruction.argument
            }

            currentInstruction.runs++


            println("Operation:   " + currentInstruction.operation)
            println("position:    " + startingInstruction)
            println("accumulator: " + accumulator)
            println("runs:        " + currentInstruction.runs)
            println("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        } else {
            runProgram = false
        }
    }
    println("Accumulator: $accumulator")
}

fun readInput(filename: String) : List<String>
    = File(filename).useLines { it.toList() }