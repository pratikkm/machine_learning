

dataset= read.csv('50_Startups.csv')


#categorical data

dataset$State = factor(dataset$State,
                         levels = c('New York','California','Florida') ,
                         labels = c(1,2,3)
                        )

#spliting data

#install.packages('caTools')

library(caTools)
set.seed(123)
split =sample.split(dataset$Profit , SplitRatio = 0.8)
training_set = subset(dataset , split==TRUE)
test_set= subset(dataset , split==FALSE)

#fiting training data to linear regression
regressor = lm(formula = Profit ~ .,
               data = training_set)
# here . means every column except profit
#we can write it also as
#regressor =lm(formula = Profit ~ R.M.spend + Administrative + Marketing.spend +State ,
#              data = training_set)

#predicting the test set result
y_pred = predict(regressor ,newdata=test_set)

#Building the optimal model using backward elimination
regressor = lm(formula = Profit ~R.D.Spend + Administration + Marketing.Spend +State ,
               data=dataset)
summary(regressor)

regressor = lm(formula = Profit ~R.D.Spend + Administration + Marketing.Spend ,
               data=dataset)
summary(regressor)

regressor = lm(formula = Profit ~R.D.Spend + Marketing.Spend  ,
               data=dataset)
summary(regressor)

regressor = lm(formula = Profit ~R.D.Spend  ,
               data=dataset)
summary(regressor)

y_prep = predict(regressor , newdata = test_set)


