#' Leer el archivo
#myData = read.delim(".txt", header = FALSE)
library(readxl)
datos <- read_excel("K_centros.xlsx", col_types = c("numeric", "numeric", "numeric"))

# Funcion calcular distancias
distancias <- function(datos){
  dij = as.matrix(dist(datos[,2:3], method = "euclidean"))
  return(dij)
}

#' Funcion objetivo
#' @param x es un vector solucion

fobj <- function(x, dij){
  sum(x*dij)
}

# Construir solucion aleatoria
solRandom <- function(){
  # solucion inicial aleatoria
  centros <- sample(1:240, 10, replace = F)
  #centros <- c(23,76,89,103,108,120,160,170,192,237)
  x <- matrix(0, nrow = 240, ncol=240)
  puntos <- setdiff(1:240,centros)
  for(i in centros){
    x[i,i] = 1
  }
  
  centros2 <- sample(centros, 10, replace = F)
  for(i in centros2){
    etiqueta <- c()
    for(j in puntos){
      x[i,j] <- rbinom(1,1,0.5)
      if(x[i,j]==1){
        etiqueta <- rbind(etiqueta, j)          
      }
    }
    puntos <- setdiff(puntos,etiqueta)
  }
  return(x)
}

#' Algoritmo de Busqueda aleatoria simple para continuos
#' @param x es un matriz solucion inicial
#' @param K es el maximo numero de iteraciones (escalar)

Busq_AS <- function(dij, K){
  k <- 0
  x <- solRandom()
  cat('iter=', k, 'objetivo=', fobj(x, dij),'\n')

  while(k < K){
    k <- k + 1
    #' Paso 1
    xhat <- solRandom()

    if(fobj(xhat,dij) < fobj(x,dij)){
      cat('iter=', k, 'objetivo=', fobj(x, dij),'\n')
      x <- xhat
    }
  }
  return(x)
}

#' Correr la funcion de busqueda aleatoria
dij <- distancias(datos)
Busq_AS(dij, 1000)

# optimo 27139.084

