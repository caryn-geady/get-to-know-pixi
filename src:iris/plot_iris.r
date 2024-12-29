library(ggplot2)
if (!require("ggplot2")) {
  print("ggplot2 is not installed. but it would be if you used pixi properly.")
}

# Define the URL and temporary file path
url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
temp_file <- tempfile(fileext = ".csv")

# Download the data
download.file(url, temp_file)

# Read the data into R
column_names <- c("Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species")
iris_data <- read.csv(temp_file, header = FALSE, col.names = column_names)

# Create the first plot: Sepal Length vs Sepal Width
plot1 <- ggplot(iris_data, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point() +
  labs(title = "Sepal Length vs Sepal Width", x = "Sepal Length", y = "Sepal Width")

# Create the second plot: Petal Length vs Petal Width
plot2 <- ggplot(iris_data, aes(x = Petal.Length, y = Petal.Width, color = Species)) +
  geom_point() +
  labs(title = "Petal Length vs Petal Width", x = "Petal Length", y = "Petal Width")

# Save the plots to files
# make directory if it doesn't exist
dir.create("images", showWarnings = FALSE)

ggsave("images/iris_r1.png", plot = plot1)
ggsave("images/iris_r2.png", plot = plot2)