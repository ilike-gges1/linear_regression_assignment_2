#Reading the csv file

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_var <- args[2]
y_var <- args[3]
    
lr_data<-read.csv(filename)
print(lr_data)
#assigning the data in the csv as a variable and printing said variable

#creating the scatterplot with the plot command

formula <- as.formula(paste(y_var, "~", x_var))
model <- lm(formula, data = lr_data)

library(ggplot2)
plot <- ggplot(lr_data, aes(.data[[x_var]], .data[[y_var]])) +
  geom_point(color = "blue") +
  geom_smooth(method = "lm", color = "green") +
  ggtitle(paste(y_var, "vs", x_var)) +
  xlab(x_var) +
  ylab(y_var)
summary(model) #How we are evaluating our model
ggsave("linear_regression_r_output.png", plot)
print(plot)
#adding a line to the data


