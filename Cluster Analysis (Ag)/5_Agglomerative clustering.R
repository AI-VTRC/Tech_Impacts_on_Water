library(tidyverse)
library(cluster)  
library(factoextra)
library(dendextend) 
library(readxl)
library(stats)
library(usmap)
library(ggplot2)
library(ggrepel)

# Data import and pre-processing
final_data = as.data.frame(read_excel("Ajay_Irrigation_Final_Data.xlsx"))
colnames(final_data)[7] = "Drought_Level"
final_data$Drought_Level = as.factor(final_data$Drought_Level)
str(final_data)

State = final_data$State
fips = final_data$fips
rownames(final_data) = final_data$State

numerical_data = final_data  %>% select(c(-State, -Drought_Level, -fips))
scale_data = as.data.frame(scale(numerical_data))

data = data.frame()
data = cbind(scale_data, final_data$Drought_Level)
colnames(data)[8] = "Drought_Level"

# Distance calculation by Gower distance
distance_matrix = daisy(data, metric = "gower")
summary(distance_matrix)
# Metric :  mixed ;  Types = I, I, I, I, I, I, I, N 
# Number of objects : 50

# Agglomerative Hierarchical Clustering
m = c( "average", "single", "complete", "ward")
names(m) = c( "average", "single", "complete", "ward")

# function to compute coefficient
ac <- function(x) {
  agnes(distance_matrix, method = x)$ac
}

map_dbl(m, ac)

#   average    single  complete      ward 
# 0.8682730 0.8385248 0.9013513 0.9306132 

fviz_nbclust(data, FUN = hcut, method = "silhouette")
fviz_nbclust(data, FUN = hcut, method = "wss")

# Cluster Analysis: 3
hc <- agnes(distance_matrix, method = "ward")
pltree(hc, cex = 0.5, hang = -1, main = "Dendrogram")
rect.hclust(hc, k = 3, border = 2:5)
sub_grp <- cutree(hc, k = 3)
table(sub_grp)
#  1  2  3 
# 41  2  7 

data_3 = data.frame()
data_3 = final_data %>%
  mutate(cluster = sub_grp,
         fips = fips)

# Map for three clusters
data_3$cluster = as.factor(data_3$cluster)
data_3$Acres = data_3$`AG Land, (Excl Harvested Cropland) - Acres` +
  data_3$`AG Land (Cropland, Harvested) - Acres`
data_3$`Cloud and Data Centers` = data_3$Semiconductor + data_3$DataCenter
colnames(data_3)[8] = "Semiconductor Factories"

write.csv(data_3, "cluster_3.csv", row.names = FALSE)

p1 <- plot_usmap(data = data_3,
                 values = "cluster",
                 labels = TRUE,
                 exclude = c("HI", "DC"),
                 alpha = 0.8) +
  labs(title = "Cluster Analysis: 3 Clusters", fill = "Clusters") + #subtitle = "This is a blank map of the United States.") + 
  theme(legend.position = "right")

p1$layers[[2]]$aes_params$size <- 2.5
print(p1)

# Cluster Analysis: 5
hc_5 <- agnes(distance_matrix, method = "ward")
pltree(hc_5, cex = 0.5, hang = -1, main = "Dendrogram")
rect.hclust(hc_5, k = 5, border = 2:6)
sub_grp_5 <- cutree(hc, k = 5)
table(sub_grp_5)
#  1  2  3  4  5 
# 18 14  9  2  7 

data_5 = data.frame()
data_5 = final_data %>%
  mutate(cluster = sub_grp_5)

data_5$cluster = as.factor(data_5$cluster)

write.csv(data_5, "cluster_5.csv", row.names = FALSE)

p6 <- plot_usmap(data = data_5,
                 values = "cluster",
                 labels = TRUE,
                 exclude = c("HI", "DC"),
                 alpha = 0.8) +
  labs(title = "Cluster Analysis: 5 Clusters", fill = "Clusters") + #subtitle = "This is a blank map of the United States.") + 
  theme(legend.position = "right")

p6$layers[[2]]$aes_params$size <- 2.5
print(p6)


# Spatial Plots for variables
citypop <- usmap_transform(citypop)

p2 <- plot_usmap(data = data_3,
           values = "Drought_Level",
           labels = TRUE,
           exclude = c("HI", "DC"),
           alpha = 0.8)  +
  labs(title = "Drought Levels Across the US",
       fill = "Drought Levels") + #subtitle = "This is a blank map of the United States.") + 
  theme(legend.position = "right")

p2$layers[[2]]$aes_params$size <- 2.5
print(p2)

p3 <- plot_usmap(data = data_3,
           values = "Acres",
           labels = TRUE,
           exclude = c("HI", "DC"),
           alpha = 0.8) +
  labs(title = "Total Agriculure Land") + #subtitle = "This is a blank map of the United States.") + 
  theme(legend.position = "right")

p3$layers[[2]]$aes_params$size <- 2.5
print(p3)

p4 <- plot_usmap(data = data_3,
           values = "Cloud and Data Centers",
           labels = TRUE,
           exclude = c("HI", "DC"),
           alpha = 0.8) +
  labs(title = "Total Number of Cloud and Data Centers") + #subtitle = "This is a blank map of the United States.") + 
  theme(legend.position = "right")

p4$layers[[2]]$aes_params$size <- 2.5
print(p4)

p5 <- plot_usmap(data = data_3,
           values = "Semiconductor Factories",
           labels = TRUE,
           exclude = c("HI", "DC"),
           alpha = 0.8) +
  labs(title = "Total Number of Semiconductor Factories")+ #subtitle = "This is a blank map of the United States.") + 
  theme(legend.position = "right")

p5$layers[[2]]$aes_params$size <- 2.5
print(p5)
       
# Cluster validation using Dunn Index

library(clValid)

## Retrieve Dunn's index for given matrix and clusters
dunn(distance = distance_matrix, sub_grp)
# 0.252037

dunn(distance = distance_matrix, sub_grp_5)
# 0.2656923

dunn(distance = distance_matrix, sub_grp_2)
# 0.1537085
