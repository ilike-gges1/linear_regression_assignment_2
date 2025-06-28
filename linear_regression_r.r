args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_var <- args[2]
y_var <- args[3]
    
lr_data<-read.csv(filename) #reading the csv and assigning it the lr_data variable
print(lr_data)
#assigning the data in the csv as a variable and printing said variable

#creating the scatterplot with the plot command
df <- data.frame(
    x_lr = array(lr_data[[x_var]]),
    y_lr = array(lr_data[[y_var]])
) #I made these arrays to try and solve some issues I had, I did not use them but I am too scared to remove them in case they break the code they are harmless they just need food twice a day and need to be let out every so often for exercise.

formula <- as.formula(paste(y_var, "~", x_var))
model <- lm(formula, data = lr_data) #making the linear regression model
slope <- coef(model)[2] #slope
intercept <- coef(model)[1] #y-intercept
pred <- predict(model) #making a prediction model
mse <- mean((pred - lr_data[[y_var]])^2) #making the MSE
corrcoef <- cor(lr_data[[x_var]], lr_data[[y_var]]) #making the correlation coefficient

library(ggplot2) #loading the ggplot2 library
plot <- ggplot(lr_data, aes(.data[[x_var]], .data[[y_var]])) + #plotting the graph
  geom_point(color = "blue") +
  geom_smooth(method = "lm", color = "green") +
  annotate("text", x = 1.5, y = max(lr_data[[y_var]]),  #annotating the graph
           label = paste("y +", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(corrcoef, 2), "\nMSE =", round(mse, 2)),
           size = 4) +
  ggtitle(paste(y_var, "vs", x_var)) +
  xlab(x_var) +
  ylab(y_var)
summary(model) #How we are evaluating our model
ggsave("linear_regression_r_output.png")
print(plot)


