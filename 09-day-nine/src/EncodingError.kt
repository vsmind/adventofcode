import java.io.File

fun main() {
    //val input = readInput("09-day-nine/src/inputTest")
    val input = readInput("09-day-nine/src/input")

    val preparedInput = input.map { it.toLong() }
    val preamble = 25

    println(preparedInput)

    val sumToFind = findNotASumNumber(preamble, preparedInput)

    val sequenceForSum = findSequenceForSum(sumToFind, preparedInput)
    val encryptionWeakness = sequenceForSum.minOrNull()?.plus(sequenceForSum.maxOrNull()!!)
    println("Encryption weakness: $encryptionWeakness")
}

fun findSequenceForSum(sumToFind :Long, input: List<Long>) : List<Long> {
    val sumSequence = mutableListOf<Long>()
    for (value in input) {
        when {
            sumSequence.sum().plus(value) < sumToFind -> {
                sumSequence.add(value)
            }
            sumSequence.sum().plus(value) > sumToFind -> {
                removeElementsFromArray(sumToFind, value, sumSequence)
                sumSequence.add(value)
            }
            else -> {
                println("Something went wrong :(")
            }
        }

            if (sumSequence.sum() == sumToFind) {
            println("SEQUENCE")

            return sumSequence
        }
    }
    return emptyList()
}

fun removeElementsFromArray( sumToFind: Long, nextValue: Long,  sumSequence: MutableList<Long>)  {
    while (sumSequence.sum().plus(nextValue) > sumToFind) {
        sumSequence.removeFirst()
    }
}

fun findNotASumNumber(preamble: Int, input: List<Long>) : Long {
    for (i in preamble until input.size) {
        val preambleList = findPreamble(preamble, i, input)

        val numberFollowsRule = isNumberFollowsRule(input[i], preambleList)
        if (!numberFollowsRule) {
            println("number not follows rule: " + input[i])
            return input[i]
        }
    }
    return 0
}

fun isNumberFollowsRule(numberToCheck: Long, preambleList: List<Long>) : Boolean {
    for (number in preambleList)
        for (secondNumber in preambleList)
            if (number +  secondNumber == numberToCheck)
                return true
    return false
}

fun findPreamble(preamble: Int, position: Int, input: List<Long>) : List<Long> {
    return input.subList((position - preamble), position)
}

fun readInput(filename: String): List<String> = File(filename).useLines { it.toList() }