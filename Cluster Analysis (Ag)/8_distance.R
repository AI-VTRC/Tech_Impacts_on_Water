library(tidyverse)
library(cluster)  
library(factoextra)
library(dendextend) 
library(readxl)
library(stats)
library(usmap)
library(ggplot2)
library(ggrepel)

c_5 = read.csv("New_results/Agglomerative/cluster_5.csv")
c_5$cluster = as.factor(c_5$cluster)

total_op = c_5$AG.Land...Excl.Harvested.Cropland....Number.of.Opreations + 
  c_5$AG.Land..Cropland..Harvested.....Number.of.Opreations

rownames(c_5) = c_5$State

c_5 = cbind(c_5, total_op)

one = c_5 %>%
  filter(cluster == 1) %>%
  select(c(15, 17, 16, 11, 17, 8, 9,10))

avg_1 = c(890414, 3687, 59.9, 4, 47.06000,70.16923,48.72308)
one = rbind(one, avg_1)
d1<- dist(one)
View(as.matrix(d1))

two = c_5 %>%
  filter(cluster == 2) %>%
  select(c(15, 17, 16, 11, 17, 8, 9,10))

avg_2 = c(1347315, 4920, 30.6, 3.46, 23.00077, 64.46923, 40.42308)
two = rbind(two, avg_2)
d2<- dist(two)
View(as.matrix(d2))

three = c_5 %>%
  filter(cluster == 3) %>%
  select(c(15, 17, 16, 11, 17, 8, 9,10))

avg_3 = c(5672118, 36492, 282, 28.5, 24.92000, 75.65000, 51.35000)
three = rbind(three, avg_3)
d3 <- dist(three)
View(as.matrix(d3))

four = c_5 %>%
  filter(cluster == 4) %>%
  select(c(15, 17, 16, 11, 17, 8, 9,10))

avg_4 = c(1938904, 14850, 37.6, 4.14, 23.93143, 58.78571, 35.07143)
four = rbind(four, avg_4)
d4 <- dist(four)
View(as.matrix(d4))


five = c_5 %>%
  filter(cluster == 5) %>%
  select(c(15, 17, 16, 11, 17, 8, 9,10))

avg_5 = c(156626, 1896, 1.77, 39, 54.02692, 64.17692, 43.71538)
five = rbind(five, avg_5)
d5 <- dist(five)
View(as.matrix(d5))
