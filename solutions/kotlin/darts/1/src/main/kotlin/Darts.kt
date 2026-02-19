object Darts {

    fun score(x: Number, y:Number): Int {
       var radius = Math.pow((Math.pow(x.toDouble(),2.0) + Math.pow(y.toDouble(),2.0)),0.5)
      
        return when{
            radius > 10 -> 0
            radius >5 -> 1
            radius >1 -> 5
            else -> 10
        }
    }
}
