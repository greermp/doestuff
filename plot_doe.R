library(tidyverse)
library(GGally)

setwd("~/pymysql")
doe <- read.csv("CCD_DOE.csv")

z=doe %>% select(-X)

z%>% plot(doe)

plot(z , pch=20 , cex=1.5 , col="#154360")


