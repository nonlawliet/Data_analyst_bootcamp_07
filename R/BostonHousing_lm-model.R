library(caret)
library(ggplot2)
library(tidyverse)
library(MLmetrics)

data("BostonHousing")
df <- BostonHousing

glimpse(df)
as_tibble(df)

sum(is.na.data.frame(df))

summarise(df, min(medv), max(medv), mean(medv), median(medv))

(quantiles <- quantile(df$medv, probs = c(0.25, 0.5, 0.75)))
(IQR <- IQR(df$medv))
(lower <- quantiles[[1]] - 3*IQR)
(upper <- quantiles[[3]] + 3*IQR)

new_df <- subset(df, df$medv > lower & df$medv < upper)

## 1. split data

train_test_split <- function(data, trainRatio = 0.8) {
  set.seed(42)
  n <- nrow(data)
  id <- sample(n, size=trainRatio*n)
  train_data <- data[id, ]
  test_data <- data[-id, ]
  return(list(train = train_data, test = test_data))
}

split_data <- train_test_split(new_df)
train_data <- split_data$train
test_data <- split_data$test

## 2. train model
ctrl <- trainControl(method = "cv",
                     number = 10,
                     verboseIter = TRUE)
set.seed(42)
(lm_model <- train(medv ~.,
                   data = train_data,
                   method = "lm",
                   preProcess = c("center", "scale"),
                   trControl = ctrl))

## 3. score
p <- predict(object = lm_model, newdata = test_data)

## 4. evaluate

R2_Score(p, test_data$medv)
RMSE(p, test_data$medv)

ggplot() +
  geom_point(aes(x = p, y = test_data$medv)) +
  labs(x = "Predict medv", y = "Test medv") +
  theme_classic()
