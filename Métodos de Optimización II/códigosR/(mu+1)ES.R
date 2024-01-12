require(colorRamps)
my.cols <- matlab.like(9)

#' Funcion graficar
graficar <- function(texto){ 
  x <- seq(-4, 4, length.out=100)
  y <- seq(-4, 4, length.out=100)
  z <- fobj2(expand.grid(x, y))
  contour(x, y, matrix(z$Var, length(x)), xlab='x1', ylab='x2', col=my.cols, 
          lwd=1.3, lty =1, nlevels = 14, main=texto)
}

#' Funcion objetivo
#' @param x es un vector solucion

fobj <- function(x){
  objetivos = rep(0, length(x[,1]))
  for(i in 1:length(x[,1])){
    objetivos[i] = 0.5*((x[i,1]^4 - 16*x[i,1]^2 +5*x[i,1])+(x[i,2]^4 - 16*x[i,2]^2 +5*x[i,2]))    
  }
return(objetivos)
}

fobj2 <- function(x){
 0.5*((x[1]^4 - 16*x[1]^2 +5*x[1])+(x[2]^4 - 16*x[2]^2 +5*x[2]))    
}

#' Algoritmo de Busqueda aleatoria localizada para continuos
#' @param x es un vector solucion inicial
#' @param K es el maximo numero de iteraciones (escalar)

Busq_ES <- function(xpob, K, sigma){
  k <- 0
  points(xpob[,1], xpob[,2], col='blue', pch=19)
  
  while(k < K){
    k <- k + 1

    #' seleccinar dos padres
    padres = sample(1:length(xpob[,1]), 2)

    #' Recombina padres (discreta local)
   # x = rep(0,2)
   # for (j in 1:2) {
   #   if(runif(1) < 0.5){
   #     x[j] = xpob[padres[1],j]    
   #   }else{
   #     x[j] = xpob[padres[2],j]
   #   }
   # }

    #' Recombina padres (intermedia local)
    x <- xpob[padres[1],1:2] + runif(1)*(xpob[padres[2],1:2] - xpob[padres[1],1:2])

         
    d <- rnorm(2, 0, sigma) # cuantos, media, desv
    xhat <- x + d
    xhat = c(xhat, fobj2(xhat))

    if(xhat[3] < max(xpob[,3])){
      xpob[which.max(xpob[,3]),] <- xhat
    }

    mejor = min(xpob[,3])
    graficar(as.character(paste('iteracion', k,'fobj=', mejor)))
    points(xpob[,1], xpob[,2], col='blue', pch=19)
    points(xpob[which.min(xpob[,3]),1], xpob[which.min(xpob[,3]),2], col='green', pch=19) # mejor padre
    points(xpob[which.max(xpob[,3]),1], xpob[which.max(xpob[,3]),2], col='red', pch=19) # peor padre
    
    Sys.sleep(0.1)
  }
  #return(x)
}

#' Correr la funcion 
npob <- 10
xpob = matrix(runif(npob*2,-4,4), ncol=2, nrow=npob)
xpob = cbind(xpob, fobj(xpob))
mejor = min(xpob[,3])
graficar(as.character(paste('iteracion',0,'fobj=', mejor)))
Busq_ES(xpob, 300, 0.5)



