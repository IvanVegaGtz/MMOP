# Cargamos las librerias
library(univariateML)
library(survival)
library(KMsurv)
library(survMisc)
library(survminer)
library(ggfortify)
library(flexsurv)
library(actuar)
library(dplyr)
library(fitdistrplus)

# Cargamos la base de datos

datos = read_excel("/Users/ivanvegagutierrez/Desktop/CIMAT/SEGUNDO/MODEST2/tareas/02_examen/datos.xlsx",  
                 col_types = c("numeric", "numeric", "numeric"))

# Grafico de dispersion

gdisp <- ggplot(datos, aes(Temperatura, Tiempo)) + 
geom_point(aes(color = factor(Censura))) + theme_bw() +
ggtitle("Tiempo de falla") 
#+ theme(plot.title = element_text(face = "bold"))
gdisp

# Estimacion de distribuciones individuales

# Categoias de los datos
temp170 <- as.numeric(unlist(Datos[1:20,2]))
temp150 <- as.numeric(unlist(Datos[21:40,2]))
temp130 <- as.numeric(unlist(Datos[41:60,2]))
temp110 <- as.numeric(unlist(Datos[61:80,2]))
# Ajuste de distribuciones por categorias
# Criterio de información bayesiano
# Temperatura 170
comparacion_bic_170 <- BIC(
  mlexp(datos$Tiempo[1:20]),
  mlnorm(datos$Tiempo[1:20]),
  mllnorm(datos$Tiempo[1:20]),
  mlweibull(datos$Tiempo[1:20])
)
# Comparacion 150
comparacion_bic_150 <- BIC(
  mlexp(datos$Tiempo[21:40]),
  mlnorm(datos$Tiempo[21:40]),
  mllnorm(datos$Tiempo[21:40]),
  mlweibull(datos$Tiempo[21:40])
)
# Comparacion 130
comparacion_bic_130 <- BIC(
  mlexp(datos$Tiempo[41:60]),
  mlnorm(datos$Tiempo[41:60]),
  mllnorm(datos$Tiempo[41:60]),
  mlweibull(datos$Tiempo[41:60])
)
# Comparacion 110
comparacion_bic_110 <- BIC(
  mlexp(datos$Tiempo[61:80]),
  mlnorm(datos$Tiempo[61:80]),
  mllnorm(datos$Tiempo[61:80]),
  mlweibull(datos$Tiempo[61:80])
)
comparacion_bic_170
comparacion_bic_150
comparacion_bic_130
comparacion_bic_110
# Criterio de información de Akaike
# Temperatura 170
comparacion_aic_170 <- AIC(
  mlexp(datos$Tiempo[1:20]),
  mlnorm(datos$Tiempo[1:20]),
  mllnorm(datos$Tiempo[1:20]),
  mlweibull(datos$Tiempo[1:20])
)
# Comparacion 150
comparacion_aic_150 <- AIC(
  mlexp(datos$Tiempo[21:40]),
  mlnorm(datos$Tiempo[21:40]),
  mllnorm(datos$Tiempo[21:40]),
  mlweibull(datos$Tiempo[21:40])
)
# Comparacion 130
comparacion_aic_130 <- AIC(
  mlexp(datos$Tiempo[41:60]),
  mlnorm(datos$Tiempo[41:60]),
  mllnorm(datos$Tiempo[41:60]),
  mlweibull(datos$Tiempo[41:60])
)
# Comparacion 110
comparacion_aic_110 <- AIC(
  mlexp(datos$Tiempo[61:80]),
  mlnorm(datos$Tiempo[61:80]),
  mllnorm(datos$Tiempo[61:80]),
  mlweibull(datos$Tiempo[61:80])
)
comparacion_aic_170
comparacion_aic_150
comparacion_aic_130
comparacion_aic_110

# Ajuste no parametric
dist170 = fitdist(datos$Tiempo[1:20],'weibull')
dist150 = fitdist(datos$Tiempo[21:40],'lnorm')
dist130 = fitdist(datos$Tiempo[41:60],'lnorm')
dist110 = fitdist(datos$Tiempo[61:80],'weibull')

grafica_170 = ggplot(data=datos[datos$Temperatura %in% "170", ],aes(x=Tiempo))+
  stat_ecdf(size=1,colour='forestgreen')+
  ggtitle(label='Temperatura = 170')+
  geom_function(fun=pweibull,colour='red4',lwd=1,
                args = list(shape = dist170$estimate[1], scale =dist170$estimate[2]))+
  theme(plot.title = element_text(hjust = 0.5))+
  xlab('Tiempo de falla')+
  ylab('Distribucion acumulada')
grafica170
dist150

grafica_170 =ggplot(data=datos[datos$Temperatura %in% "170", ],aes(x=Tiempo))+
  stat_ecdf(size=1,colour='black')+
  ggtitle(label='Temperatura de 170')+
  geom_function(fun=pweibull,colour='blue',lwd=1,
                args = list(shape = dist170$estimate[1], scale =dist170$estimate[2]))+
  theme(plot.title = element_text(hjust = 0.5))+
  xlab('Tiempo de falla')+
  ylab('Riesgo acumulado')
grafica_170

grafica_150 = ggplot(data=datos[datos$Temperatura %in% "150", ],aes(x=Tiempo))+
  stat_ecdf(size=1,colour='black')+
  ggtitle(label='Temperatura de 150')+
  geom_function(fun=plnorm,colour='red',lwd=1,
                args = list(meanlog = dist150$estimate[1], sdlog =dist150$estimate[2]))+
  theme(plot.title = element_text(hjust = 0.5))+
  xlab('Tiempo de falla')+
  ylab('Riesgo acumulado')
grafica_150

grafica_130 = ggplot(data=datos[datos$Temperatura %in% "130", ],aes(x=Tiempo))+
  stat_ecdf(size=1,colour='black')+
  ggtitle(label='Temperatura de 130')+
  geom_function(fun=plnorm,colour='red',lwd=1,
                args = list(meanlog = dist130$estimate[1], sdlog =dist130$estimate[2]))+
  theme(plot.title = element_text(hjust = 0.5))+
  xlab('Tiempo de falla')+
  ylab('Riesgo acumulado')
grafica_130

grafica_110 =ggplot(data=datos[datos$Temperatura %in% "110", ],aes(x=Tiempo))+
  stat_ecdf(size=1,colour='black')+
  ggtitle(label='Temperatura de 110')+
  geom_function(fun=pweibull,colour='blue',lwd=1,
                args = list(shape = dist110$estimate[1], scale =dist110$estimate[2]))+
  theme(plot.title = element_text(hjust = 0.5))+
  xlab('Tiempo de falla')+
  ylab('Riesgo acumulado')
grafica_110


comparacion_figura =ggarrange(grafica_170 , grafica_150 , grafica_130, grafica_110 ,ncol=2,nrow=2)
comparacion_figura

# Kaplan Meier
datos.surv <- Surv(datos$Tiempo, datos$Censura)
datos.km <- survfit(datos.surv ~ Temperatura, data = datos, type = "kaplan-meier") 
summary(datos.km)


km_170 = ggsurvplot(fit = datos.km[4], data = datos, conf.int = T, 
           title = "Curva de Supervivencia para 170 grados ", 
           xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
           legend.labs = "Kaplan-Meier")
km_150 = ggsurvplot(fit = datos.km[3], data = datos, conf.int = T, 
           title = "Curva de Supervivencia para 150 grados", 
           xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
           legend.labs = "Kaplan-Meier")
km_130 = ggsurvplot(fit = datos.km[2], data = datos, conf.int = T, 
           title = "Curva de Supervivencia para 130 grados", 
           xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
           legend.labs = "Kaplan-Meier")
km_110 = ggsurvplot(fit = datos.km[1], data = datos, conf.int = T, 
           title = "Curva de Supervivencia para 110 grados", 
           xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
           legend.labs = "Kaplan-Meier")

ggsurvplot(fit = datos.km, data = datos, conf.int = T, title = "Curva de Supervivencia", 
           xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
           legend.labs = c("Kaplan-Meier","Kaplan-Meier","Kaplan-Meier","Kaplan-Meier"))

# Temperatura 170
datos.surv_170 <- Surv(datos$Tiempo[1:20], datos$Censura[1:20])
datos.km_170 <- survfit(datos.surv ~ Temperatura, data = datos, type = "kaplan-meier") 
summary(datos.km_170)

           
# Temperatura 150
datos.surv_150 <- Surv(datos$Tiempo[21:40], datos$Censura[21:40])
datos.km_150 <- survfit(datos.surv ~ 1, data = datos, type = "kaplan-meier") 
#summary(datos.km_150)
# Temperatura 130
datos.surv_130 <- Surv(datos$Tiempo[41:60], datos$Censura[41:60])
datos.km_130 <- survfit(datos.surv ~ 1, data = datos, type = "kaplan-meier") 
#summary(datos.km_130)
# Temperatura 110
datos.surv_110 <- Surv(datos$Tiempo[61:80], datos$Censura[61:80])
datos.km_110 <- survfit(datos.surv ~ 1, data = datos, type = "kaplan-meier") 
#summary(datos.km_110)

# Grafica Kaplan Meier

plot(datos.km)
plot(datos.km_110)
summary(datos.km_110)
plot(datos.km_170)
summary(datos.km_170)

total = ggsurvplot(fit = datos.km, data = datos, conf.int = T, title = "Curva de Supervivencia", 
           xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
           legend.labs = "Kaplan-Meier")

t_170 = ggsurvplot(fit = datos.km_170, data = datos$Temperatura[1:20], conf.int = T, title = "Curva de Supervivencia", 
           xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
           legend.labs = "Kaplan-Meier")
t_150 = ggsurvplot(fit = datos.km_150, data = datos$Temperatura[21:40], conf.int = T, title = "Curva de Supervivencia", 
                   xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
                   legend.labs = "Kaplan-Meier")
t_130 = ggsurvplot(fit = datos.km_130, data = datos, conf.int = T, title = "Curva de Supervivencia", 
                   xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
                   legend.labs = "Kaplan-Meier")
t_110 = ggsurvplot(fit = datos.km_110, data = datos$Temperatura[61:80], conf.int = T, title = "Curva de Supervivencia", 
                   xlab = "Tiempo", ylab = "Probabilidad de supervivencia", legend.title = "Estimación", 
                   legend.labs = "Kaplan-Meier")
t_170
t_150
t_130
t_110
total








