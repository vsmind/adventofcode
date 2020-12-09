import com.sun.org.apache.xpath.internal.operations.Bool
import java.io.File
import java.text.FieldPosition

fun main() {
    //val input = readInput("09-day-nine/src/inputTest")
    val input = readInput("09-day-nine/src/input")

    val preparedInput = input.map { it.toLong() }
    val preamble = 25

    println(preparedInput)

    findNotASumNumber(preamble, preparedInput)
}

fun findNotASumNumber(preamble: Int, input: List<Long>) {
    for (i in preamble until input.size) {
        val preambleList = findPreamble(preamble, i, input)

        val numberFollowsRule = isNumberFollowsRule(input[i], preambleList)
        if (!numberFollowsRule) {
            println("number not follows rule: " + input[i])
        }
    }
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