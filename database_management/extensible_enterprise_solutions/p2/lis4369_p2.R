sink("lis4369_p2_output.txt")
# Developer Samuel Freed
# LIs 4369

library(ggplot2)

url = "http://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv"

mtcars <- read.csv(file=url,head=TRUE,sep=',')

# 1) Display all data from file:
mtcars

# 2) Display first 10 records:
head(mtcars,10)

# 3) Display last 10 records:
tail(mtcars,10)

# 4) Display file structure:
str(mtcars)

# 5) Display column names:
names(mtcars)

# 6) Display 1st record/row with column names:
head(mtcars,1)

# 7) Display 2nd column data (mpg), using column number:
mtcars[2]

# 8) Display column data (cyl), using column name:
mtcars$cyl

# 9) Display row/column data (3,4), that is, one field, using square bracket notation:
mtcars[3,4]

# 10) Display all data for cars having greater than 4 cylinders:
cyl4 <- mtcars$cyl > 4
mtcars[cyl4,]

# 11) Display all cars having more than 4 cylinders *and* 5 gears or more:
gear5 <- mtcars$gear>=5
mtcars[cyl4 & gear5,]

# 12) Display all cars having more than 4 cylinders *and* exactly 4 gears: 
gear4 <- mtcars$gear==4
mtcars[cyl4 & gear4,]

# 13) Display all cars having more than 4 cylinders *or* exactly 4 gears:
mtcars[cyl4 | gear4,]

# 14) Display all cars having more than 4 cylinders that do *not* have 4 gears:
mtcars[cyl4 & !gear4,]

# 15) Display total number of rows (only the number):
nrow(mtcars)

# 16) Display total number of columns (only the number):
ncol(mtcars)

# 17) Display total number of dimensions (i.e., rows and columns):
dim(mtcars)

# 18) Display data frame structure - same as info in Python:
str(mtcars)

# 19) Get mean, median, minimum, maximum, quantiles, variance, and standard deviation of horsepower:
mean(mtcars$hp, na.rm=TRUE)
median(mtcars$hp, na.rm=TRUE)
min(mtcars$hp, na.rm=TRUE)
max(mtcars$hp, na.rm=TRUE)
quantile(mtcars$hp, na.rm=TRUE)
var(mtcars$hp, na.rm=TRUE)
sd(mtcars$hp, na.rm=TRUE)

# 20) summary() function prints min, max, mean, median, and quantiles (also, number of NA's, if any.):
summary(mtcars$hp)

# qplot():
qplot(disp,mpg,
      data=mtcars,
      main="Samuel Freed: Displacement vs MPG",
      xlab="Displacement",
      ylab="MPG")

# plot():
plot(mtcars$wt,mtcars$mpg,
     main="Samuel Freed: Weight vs MPG",
     xlab="Weight in Thousands",
     ylab="MPG")

