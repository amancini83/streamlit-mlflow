# PoC: Streamlit + MLFlow Integration with docker

- [Streamlit](https://github.com/streamlit) is the fastest way to build and share data apps. Streamlit lets you turn data scripts into shareable web apps. It’s all Python, open-source, and free. Once you’ve created an app you can use the Community Cloud platform to deploy, manage, and share your app.

- [MLflow](https://github.com/mlflow) is an open source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry.

In this repo i have built a simple demonstration of how you could use streamlit and MLflow for model prototyping as a simple demonstration of how you can use streamlit to experiment with a couple of machine learning models and mlflow to keep track of your experiments.

## Scope

This PoC use the `sklearn.datasets` package that embeds some small toy datasets.<br>
This package also features helpers to fetch larger datasets commonly used by the machine learning community to benchmark algorithms on data that comes from the "real world".<br>

### Availables datasets:

- **Iris**: This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 `numpy.ndarray`. <br>
  The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.
- **Diabetes**: Ten baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements were obtained for each of n = 442 diabetes patients, as well as the response of interest, a quantitative measure of disease progression one year after baseline.
- **Wine**: The data is the results of a chemical analysis of wines grown in the same region in Italy by three different cultivators. There are thirteen different measurements taken for different constituents found in the three types of wine.

## Availables models:

- We use Iris and Wine datasets for a classification problem. Specifically the PoC support KNN and SVM models.
- We use Diabetes dataset for a regression problem: predict a quantitative measure of disease progression one year after baseline.

> **Note**
>
> Model performance are not the key objective, we are only interested in streamlit & MLFlow integration!

## How to use?

- **Step 1:** Build docker containers for the streamlit and mlflow services and run the services.

  ```
  docker-compose up --build
  ```

- **Step 2:** Explore.

  - Open http://localhost:8501 to interact with the streamlit app.
  - Open http://localhost:5000 to access the mlflow user interface.

- **Step 3:** What to expect?

  ![Alt Text](demo.gif)
