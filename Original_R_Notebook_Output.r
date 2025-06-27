#Reading the csv file

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3 {
    stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_var <- args[2]
y_var <- args[3]
    
lr_data<-read.csv(filename)
print(lr_data)
#assigning the data in the csv as a variable and printing said variable

#creating the scatterplot with the plot command

plot(lr_data$x_var, #Pulls X value data
     lr_data$y_var, #pulls Y value data
     col="red", #color of the dots
     xlab = x_var, #x axis label
     ylab = y_var, #y axis label
     main = "graph", #graph title
     pch = 21) #type of data point

#adding a line to the data

plot(lr_data$x_var, 
     lr_data$y_var, 
     col="red", 
     xlab = "Years of Experience (Years)", 
     ylab = "Salary (USD)", 
     main = "Years of Experience vs Salary", 
     pch = 21) #redoing the plot because it looks fun

model <- lm(y_var ~ x_var, data=lr_data) #creating the linear model

library(ggplot2)
ggplot() +
  geom_point(aes(x = lr_data$x_var, y = lr_data$y_var), colour = 'red') +
  geom_line(aes(x = lr_data$x_var, y = predict(model, newdata = lr_data)), colour = 'blue') +
  ggtitle('Salary vs Experience') +
  xlab(x_var) +
  ylab(y_var)

summary(model) #How we are evaluating our model

ggsave("linear_regression_r_output.png", plot)
print(plot)

