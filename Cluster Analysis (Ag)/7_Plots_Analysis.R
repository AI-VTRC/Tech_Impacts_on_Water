library(tidyverse)
library(cluster)  
library(factoextra)
library(dendextend) 
library(readxl)
library(stats)
library(usmap)
library(ggplot2)
library(ggrepel)

# Agglomerative Clustering
# Data import
c_3 = read.csv("New_results/Agglomerative/cluster_3.csv")
c_3$cluster = as.factor(c_3$cluster)

c_5 = read.csv("New_results/Agglomerative/cluster_5.csv")
c_5$cluster = as.factor(c_5$cluster)

total_op = c_3$AG.Land...Excl.Harvested.Cropland....Number.of.Opreations + 
  c_3$AG.Land..Cropland..Harvested.....Number.of.Opreations

#------------------------------------
# Agglomerative Clustering
# Cluster - 3
#------------------------------------
c_3 = cbind(c_3, total_op)

c_3 %>%
  group_by(cluster) %>%
  summarise(avg_acres = mean(Acres),
            avg_count = mean(total_op),
         avg_semi = mean(Semiconductor.Factories),
         avg_dc_cl = mean(Cloud.and.Data.Centers))

	
# cluster avg_acres avg_count avg_semi avg_dc_cl
#  1        760263.     3397.     2.80      41.1
#  2       5672118.    36492.     28.5      282. 
#  3       1938904.    14850.     3.57      37  

c_3 %>%
  group_by(cluster) %>%
  count(Drought_Level)

# cluster Drought_Level     n
#    1      D0              6
#    1      D1              9
#    1      D2              9
#    1      D3              2
#    1      D4              1
#    1     None            14

#    2      D0              1
#    2      D3              1

#    3      D1              4
#    3      D2              2
#    3      D3              1

c_3 %>%
  ggplot(aes(x = State, y = Acres, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 10) +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Agriculture Land in Acres") 

c_3 %>%
  ggplot(aes(x = State, y = total_op, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 20) +
  ylab("Agriculture Operations") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Agriculture Operations") 

c_3 %>%
  ggplot(aes(x = State, y = Cloud.and.Data.Centers, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 10) +
  ylab("Cloud Infrastructure and Data Centers") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Cloud Infrastructure and Data Centers") 

c_3 %>%
  ggplot(aes(x = State, y = Semiconductor.Factories, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 20) +
  ylab("Semiconductor Factories") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Semiconductor Factories") 


#------------------------------------
# Agglomerative Clustering
# Cluster - 5
#------------------------------------

c_5 = cbind(c_5, total_op)

c_5 %>%
  group_by(cluster) %>%
  summarise(avg_acres = mean(Acres),
            avg_count = mean(total_op),
            avg_semi = mean(Semiconductor),
            avg_dc_cl = mean(Cloud.and.Data.Centers))

# cluster avg_acres avg_count avg_semi avg_dc_cl
#   1       1118727.    4909.     2         37.2
#   2       145604.     1794.     1.71      36.3
#   3       999471.     2868.     6.11      56.4
#   4       5672118.    36492.    28.5      282. 
#   5       1938904.    14850.     3.57      37  

c_5 %>%
  group_by(cluster) %>%
  count(Drought_Level)

# cluster Drought_Level     n
#   1       D0              6
#   1       D2              9
#   1       D3              2
#   1       D4              1

#   2     None             14

#   3       D1              9

#   4       D0              1
#   4       D3              1

#   5       D1              4
#   5       D2              2
#   5       D3              1

c_5 %>%
  ggplot(aes(x = State, y = Acres, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel() +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Agriculture Land in Acres") 

c_5 %>%
  ggplot(aes(x = State, y = total_op, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 20) +
  ylab("Agriculture Operations") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Agriculture Operations") 

c_5 %>%
  ggplot(aes(x = State, y = Cloud.and.Data.Centers, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 10) +
  ylab("Cloud Infrastructure and Data Centers") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Cloud Infrastructure and Data Centers") 

c_5 %>%
  ggplot(aes(x = State, y = Semiconductor, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 20) +
  ylab("Semiconductor Factories") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Semiconductor Factories") 


#------------------------------------
# Divisive Clustering
# Cluster - 5
#------------------------------------

c_5 = read.csv("New_results/Divisive/cluster_div_5.csv")
c_5$cluster = as.factor(c_5$cluster)

total_op = c_5$AG.Land...Excl.Harvested.Cropland....Number.of.Opreations + 
  c_5$AG.Land..Cropland..Harvested.....Number.of.Opreations

c_5 = cbind(c_5, total_op)

c_5 %>%
  group_by(cluster) %>%
  summarise(avg_acres = mean(Acres),
            avg_count = mean(total_op),
            avg_semi = mean(Semiconductor),
            avg_dc_cl = mean(Cloud.and.Data.Centers))

#cluster avg_acres avg_count avg_semi avg_dc_cl
#   1       509097.     2660.     3.38      46.3
#   2       1367247.     5180.    1.42      28.4
#   3       7875987.    53486.    36        308  
#   4       1938904.    14850.    3.57      37  
#   5       3468249.    19497.    21        257  

c_5 %>%
  group_by(cluster) %>%
  count(Drought_Level)

# cluster Drought_Level     n
#   1       D0                6
#   1       D1                9
#   1       None             14

#   2       D2                9
#   2       D3                2
#   2       D4                1

#   3       D0                1

#   4       D1                4
#   4       D2                2
#   4       D3                1

#   5       D3                1


c_5 %>%
  ggplot(aes(x = State, y = Acres, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel() +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Agriculture Land in Acres") 

c_5 %>%
  ggplot(aes(x = State, y = total_op, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 20) +
  ylab("Agriculture Operations") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Agriculture Operations") 

c_5 %>%
  ggplot(aes(x = State, y = Cloud.and.Data.Centers, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 10) +
  ylab("Cloud Infrastructure and Data Centers") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Cloud Infrastructure and Data Centers") 

c_5 %>%
  ggplot(aes(x = State, y = Semiconductor, group = cluster, label = State)) +
  geom_point() +
  geom_text_repel(max.overlaps = 20) +
  ylab("Semiconductor Factories") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()) + #axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  facet_wrap(~cluster) +
  ggtitle("Total Semiconductor Factories") 
