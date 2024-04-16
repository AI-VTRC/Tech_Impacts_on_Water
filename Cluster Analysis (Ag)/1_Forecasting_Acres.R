library(timetk)
library(sweep)
library(forecast)
library(tidyquant)
library(tidyverse)

acres = read_excel("1_Acres.xlsx")

sum(is.na(acres))

acres_1 = acres %>% 
  select('Year', 'State', 'Value') %>%
  mutate(
    Year = as.Date(as.character(acres$Year), format = "%Y"),
    State = as.factor(State),
    Value = as.numeric(gsub(",","",Value)) )


acres_2 <- acres_1 %>%
  group_by(State) %>%
  nest()

acres_3 = acres_2 %>%
  mutate(data.ts = map(.x       = data, 
                       .f       = tk_ts,
                       select = -Year,
                       start = 2012,
                       freq = 1))

model_fit <- acres_3 %>%
  mutate(fit.ets = map(data.ts, auto.arima))

model_fit 

model_fit  %>%
  mutate(tidy = map(fit.ets, sw_tidy)) %>%
  unnest(tidy) %>%
  spread(key = State , value = estimate)

model_fit %>%
  mutate(glance = map(fit.ets, sw_glance)) %>%
  unnest(glance)

model_fcast <- model_fit %>%
  mutate(fcast.ets = map(fit.ets, forecast, h = 2))

model_fcast$fcast.ets

sw_glance(model_fcast$fcast.ets)

library (plyr)
df <- ldply (model_fcast$fcast.ets, data.frame)
a = df$Point.Forecast

output = 0
j = 1
for(i in seq(from = 1, to = 100, by = 2)){
  output[j] = df$Point.Forecast[i]
  j = j + 1
}

write.csv(output, "Forceast_Acres.csv")
