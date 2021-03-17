
getwd()
library(reticulate)
conda_list()
use_condaenv("r-reticulate")

library(tidyverse)
library(keras)
data <- dataset_fashion_mnist()

x_train <- data$train$x
y_train <- data$train$y

x_test <- data$test$x
y_test <- data$test$y

x_train <- array_reshape(x_train, c(nrow(x_train), 28, 28, 1))
x_test  <- array_reshape(x_test,  c(nrow(x_test),  28, 28, 1))

x_train <- x_train / 255
x_test  <- x_test  / 255

y_train <- to_categorical(y_train, 10)
y_test  <- to_categorical(y_test,  10)

model <- keras_model_sequential() 
model %>% 
  layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = "relu", input_shape = c(28, 28, 1)) %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = "relu") %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  layer_flatten() %>%
  layer_dense(units = 50, activation = "relu") %>%
  layer_dropout(rate = 0.5) %>% 
  layer_dense(units = 20, activation = "relu") %>%
  layer_dense(units = 10, activation = "softmax")

summary(model)

model %>% compile(
  loss = 'categorical_crossentropy',
  optimizer = "adam",
  metrics = c('accuracy')
)

model %>% 
  fit(
    x_train, y_train, 
    epochs = 15, 
    batch_size = 200,
    validation_split = 0.2,
    workers = 7
  )

score <- evaluate(model, x_test, y_test)
