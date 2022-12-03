import java.io.File
import java.lang.Exception

fun main() {
    val keys = ('a'..'z') + ('A'..'Z')
    val values = 1..52
    val lookup = keys.zip(values).toMap()

    val lines = getLinesFromFile("../demo-input.txt")

    val result = lines.map { line ->
        val size = line.length / 2
        val a = line.substring(0, size).toSet()
        val b = line.substring(size).toSet()
        val inter = a.intersect(b)
        assert(inter.size == 1)
        lookup.getValue(inter.first())
    }.sum()

    println(result)
}


fun printLineByLine(fileName: String)
        = File(fileName).forEachLine { println(it) }

fun getLinesFromFile(fileName: String): List<String>
        = File(fileName).useLines { it.toList() }