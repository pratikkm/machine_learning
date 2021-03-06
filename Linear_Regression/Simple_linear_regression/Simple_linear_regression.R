
dataset = read.csv('Salary_Data.csv')


library(caTools)
set.seed(123)
split =sample.split(dataset$Salary , SplitRatio = 2/3)
training_set = subset(dataset , split==TRUE)
test_set= subset(dataset , split==FALSE)

#fiting simple regression to the trainin set 

regressor = lm(formula = Salary ~ YearsExperience,
               data =training_set)

#predicting training set data

y_pred = predict(regressor , newdata = test_set)

#visualization of linear simple regresion

#install.packages('ggplot2')
library(ggplot2)

ggplot() +
  geom_point(aes(x=training_set$YearsExperience ,y = training_set$Salary),
             colour='red') +
  geom_line(aes(x=training_set$YearsExperience , y= predict(regressor , newdata=training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience(Training set)') +
  xlab('years of experience') +
  ylab('salary')


  