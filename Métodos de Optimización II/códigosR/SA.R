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

#' Algoritmo de Busqueda aleatoria localizada para continuos
#' @param x es un vector solucion inicial
#' @param K es el maximo numero de iteraciones (escalar)

Busq_AL <- function(x, K, Temp){
  k <- 0
  #cat('iter=', k, 'x1= ', x[1],'x2= ',x[2], 'objetivo=',fobj(x),'\n')
  points(x[1], x[2], col='blue', pch=19)
  #Sys.sleep(0.5)
  
  while(k < K){
    k <- k + 1
    #' Paso 1
    d <- rnorm(2, 0, 0.6) # cuantos, media, desv
    xhat <- x + d

    if(fobj(xhat) < fobj(x)){
      points(xhat[1], xhat[2], col='red', pch=19)
      #cat('iter=', k, 'x1= ',xhat[1],'x2= ',xhat[2], 'objetivo=',fobj(xhat),'\n')
      x <- xhat
    }else{
    r <- runif(1,0,1)
    if(r < exp((fobj(x)-fobj(xhat))/Temp)){
      x <- xhat
      points(xhat[1], xhat[2], col='green', pch=19)
      #cat('iter=', k, 'x1= ',xhat[1],'x2= ',xhat[2], 'objetivo=',fobj(xhat),'\n')
    }
    }
    Temp <- 0.99*Temp 
  }
  cat('T_final=', Temp, '\n' )
  return(x)
}


#' Correr la funcion de busqueda aleatoria
graficar()
x_mejor <- Busq_AL(c(4, 4), 1000, 200)

print('La mejor solucion encontrada es: \n')
cat('x1= ',x_mejor[1],'x2= ',x_mejor[2], 'objetivo=',fobj(x_mejor), '\n')




