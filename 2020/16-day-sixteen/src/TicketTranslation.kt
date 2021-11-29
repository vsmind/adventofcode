import java.io.File

fun main() {
    val input = readInput("16-day-sixteen/src/input")
    val fields = mutableListOf<TicketField>()
    val yourTicket = mutableListOf<Int>()
    val nearbyTickets = mutableListOf<List<Int>>()
    val validNearbyTickets = mutableListOf<List<Int>>()

    parseInput(input, fields, yourTicket, nearbyTickets)

    println(fields)
    println("***************************************")
    println(yourTicket)
    println("***************************************")
    println(nearbyTickets)

    var sum = 0

    val allRules = mutableSetOf<Int>()

    for (rule in fields) {
        for (value in rule.ruleOneLow..rule.ruleOneHigh) {
            allRules.add(value)
        }
        for (value in rule.ruleTwoLow..rule.ruleTwoHigh) {
            allRules.add(value)
        }
    }

    println("***************************************")
    println(allRules)
    println("***************************************")


    for (ticket in nearbyTickets) {
        for (field in ticket) {
//            if (field !in fields[index].ruleOneLow..fields[index].ruleOneHigh && field !in fields[index].ruleTwoLow..fields[index].ruleTwoHigh) {
//                sum+=field
//            }
             if (field !in allRules) {
                 sum+=field
             }
        }
    }

    println("***************************************")
    println("SUM:   $sum")

    for (ticket in nearbyTickets) {
        if (ticket.all { it in allRules }) {
            validNearbyTickets.add(ticket)
        }
    }
    println("***************************************")
    println("Valid tickets:   ${validNearbyTickets.size}")
    println(validNearbyTickets)
}

fun parseInput(input: List<String>, fields: MutableList<TicketField>, yourTicket: MutableList<Int>, nearbyTickets: MutableList<List<Int>>) {
    var parserId = 1

    for ((index, line) in input.withIndex()) {
        if (line == "") {
            parserId++
        }
        if (parserId == 1) {
            val fieldParsing = line.split(": ")
            val rules = fieldParsing[1].split(" or ")
            val rulesLow = rules[0].split("-")
            val rulesHigh = rules[1].split("-")
            fields.add(TicketField(index,
                    fieldParsing[0],
                    rulesLow[0].toInt(),
                    rulesLow[1].toInt(),
                    rulesHigh[0].toInt(),
                    rulesHigh[1].toInt()))
        }
        if (parserId == 2) {
            if (line != "your ticket:" && line != ""){
                val rules = line.split(",").map { it.toInt() }
                for (number in rules)
                    yourTicket.add(number)
            }
        }
        if (parserId == 3) {
            if (line != "nearby tickets:" && line != ""){
                val nearbyTicket = line.split(",").map { it.toInt() }
                nearbyTickets.add(nearbyTicket)
            }
        }
    }
}

fun readInput(filename: String): List<String> = File(filename).useLines { it.toList() }