import kotlin.math.hypot
object Darts {

    fun score(x: Number, y:Number): Int {
       var radius = hypot(x.toDouble(), y.toDouble())
      
        return when{
            radius > 10 -> 0
            radius >5 -> 1
            radius >1 -> 5
            else -> 10
        }
    }
}
