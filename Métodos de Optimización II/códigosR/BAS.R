

require(colorRamps)
my.cols <- matlab.like(9)

#' Funcion graficar
graficar <- function(){ 
  x <- seq(-4, 4, length.out=100)
  y <- seq(-4, 4, length.out=100)
  z <- fobj(expand.grid(x, y))
  contour(x, y, matrix(z$Var, length(x)), xlab='x1', ylab='x2', col=my.cols, 
          lwd=1.3, lty =1, nlevels = 14)
}

#' Funcion objetivo
#' @param x es un vector solucion

fobj <- function(x){
  0.5*((x[1]^4 - 16*x[1]^2 +5*x[1])+(x[2]^4 - 16*x[2]^2 +5*x[2]))
}

#' Algoritmo de Busqueda aleatoria simple para continuos
#' @param x es un vector solucion inicial
#' @param K es el maximo numero de iteraciones (escalar)

Busq_AS <- function(x, K){
  k <- 0
  #cat('iter=', k, 'x1= ', x[1],'x2= ',x[2], 'objetivo=',fobj(x),'\n')
  #points(x[1], x[2], col='blue', pch=19)
  #Sys.sleep(0.5)
  
  while(k < K){
    k <- k + 1
    #' Paso 1
    xhat <- runif(2, -4, 4)
    #points(xhat[1], xhat[2], col='gray', pch=19)
    
    if(fobj(xhat) < fobj(x)){
     # points(xhat[1], xhat[2], col='green', pch=19)
      #cat('iter=', k, 'x1= ',xhat[1],'x2= ',xhat[2], 'objetivo=',fobj(xhat),'\n')
      x <- xhat
    }#else{
    #  points(x[1],x[2], col='pink', pch=19)
    #  cat('iter=', k, 'x1= ', x[1],'x2= ',x[2], 'objetivo=',fobj(x),'\n')
    #}
    #Sys.sleep(0.05)
  }
  return(x)
}

#' Correr la funcion de busqueda aleatoria
graficar()

for(replica in 1:50){
  x <- Busq_AS(c(4, 4), 100)
  cat('replica=', replica, 'x1= ',x[1],'x2= ',x[2], 'objetivo=',fobj(x),'\n')
}




