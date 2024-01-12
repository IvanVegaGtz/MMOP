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

Busq_ES <- function(x, K, c, sigma, h){
  k <- 0
  cat('iter=', k, 'x1= ', x[1],'x2= ',x[2], 'objetivo=',fobj(x),'sigma=', sigma,'\n')
  points(x[1], x[2], col='blue', pch=19)
  exito <- 0
  
  while(k < K){
    k <- k + 1
    #' Paso 1
    d <- rnorm(2, 0, sigma) # cuantos, media, desv
    xhat <- x + d
#    points(xhat[1], xhat[2], col='gray', pch=19)
    
    if(fobj(xhat) < fobj(x)){
      points(xhat[1], xhat[2], col='green', pch=19)
      cat('iter=', k, 'x1= ',xhat[1],'x2= ',xhat[2], 'objetivo=',fobj(xhat), 'sigma=', sigma,'\n')
      x <- xhat
      exito <- exito + 1 
    }else{
    #  points(x[1],x[2], col='gray', pch=19)
    #  cat('iter=', k, 'x1= ', x[1],'x2= ',x[2], 'objetivo=',fobj(x),'\n')
    }
    # Regla de exito 1/5
    if(k %% h == 0){
      ps <- exito/h
      if(ps < 1/5){
        sigma = sigma*c
      }else if(ps > 1/5){
        sigma = sigma/c
      }
      exito <- 0
      cat('iter= ', k,'Sigma = ', sigma,'\n')
    }

  }
  return(x)
}

#' Correr la funcion 
graficar()
Busq_ES(c(4, 4), 500, 0.917, 2, 10)



