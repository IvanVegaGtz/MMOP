
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


pob_inicial <- function(N, nvar){
   pob <- c()
   for(i in 1:N){
      pob <- rbind(pob, runif(nvar,-4,4))    
   }
   return(pob)
}

evaluar <- function(pob, N){
   eval <- c()
   for(i in 1:N){
      eval <- rbind(eval, fobj(pob[i,]))
   }
   return(cbind(pob, eval))
}


seleccion <- function(pob, M, nvar){
    pob_orden <- pob[order(pob[,nvar+1]), ]
    pselec <- pob_orden[1:M,]
    return(pselec)
}

estimacion <- function(pselec){
   #medias <- colMeans(pselec[,-3])   	
   medias <- c(mean(pselec[,1]), mean(pselec[,2]))   	
   stdDev <- c(sd(pselec[,1]), sd(pselec[,2]))
   return(c(medias,stdDev))
}


muestreo <- function(param, N){
   pob <- cbind(rnorm(N,param[1],param[3]), rnorm(N,param[2],param[4]))
   return(pob)    
}


UMDA <- function(N, M, iter){
   nvar <- 2
   pob <- pob_inicial(N,nvar)
   graficar()
   points(pob[,1], pob[,2], col='blue', pch=19)
   
   for(i in 1:iter){
      pob <- evaluar(pob, N)
      pselec <- seleccion(pob, M, nvar)
      param <- estimacion(pselec)
      cat(param, 'fobj:', fobj(c(param[1],param[2])), 'iter', i,'\n')
      pob <- muestreo(param, N)
      Sys.sleep(0.2)
      graficar()
      points(pob[,1], pob[,2], col='blue', pch=19)
   }

print('La mejor solucion encontrada es: \n')
pob <- evaluar(pob, N)
pob_orden <- pob[order(pob[,nvar+1]), ]
cat('x1= ',pob_orden[1,1],'x2= ',pob_orden[1,2], 'objetivo=',fobj(pob_orden[1,]), '\n')
}

UMDA(100, 50, 50)


