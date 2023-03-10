import mlflow
import streamlit as st
from sklearn.datasets import load_diabetes, load_iris, load_wine
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import f1_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def selectbox_without_default(label, options):
    options = [""] + options
    format_func = lambda x: "Select one option" if x == "" else x
    if label == "๐ Choose a dataset":
        help_str = "Select dataset from a list"
    else:
        help_str = "Select ML model from a list"

    return st.selectbox(label, options, format_func=format_func, help=help_str)


@st.cache
def load_data(key):
    data = DATA[key](as_frame=True)
    df = data["data"]
    df["target"] = data["target"]
    return df


DATA = {"iris": load_iris, "wine": load_wine, "diabetes": load_diabetes}

PROBLEMS = {
    "iris": "classification",
    "wine": "classification",
    "diabetes": "regression",
}

MODELS = {
    "classification": {
        "KNearest Neighbors": KNeighborsClassifier,
        "Support Vector Machine": SVC,
    },
    "regression": {
        "Linear Regression": LinearRegression,
        "Random Forest Regression": RandomForestRegressor,
    },
}


def main():
    # Title
    st.title("๐งช PoC: Model Experimentation with Streamlit & MLflow")

    # Choose dataset
    data_options = list(DATA.keys())
    data_choice = selectbox_without_default("๐ Choose a dataset", data_options)
    if not data_choice:
        st.stop()
    df = load_data(data_choice)
    st.write(df)

    # Model selection
    problem_type = PROBLEMS[data_choice]
    model_options = list(MODELS[problem_type].keys())
    model_choice = selectbox_without_default("๐งฉ Choose a model", model_options)
    if not model_choice:
        st.stop()

    # Feature selection
    feature_options = df.columns.drop("target").tolist()
    feature_choice = st.multiselect(
        "๐ท๏ธ Choose some features",
        feature_options,
        help="Select relevant features for your model",
    )

    # Mlflow tracking
    track_with_mlflow = st.checkbox(
        "๐ Track with mlflow? ", help="Mark to track experiment with MLflow"
    )

    # Model training
    start_training = st.button("๐ช Start training", help="Train and evaluate ML model")
    if not start_training:
        st.stop()

    if track_with_mlflow:
        mlflow.set_experiment(data_choice)
        mlflow.start_run()
        mlflow.log_param("model", model_choice)
        mlflow.log_param("features", feature_choice)

    X = df[feature_choice].copy()
    y = df["target"].copy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    model = MODELS[problem_type][model_choice]()
    model.fit(X_train, y_train)

    # Model evaluation
    preds_train = model.predict(X_train)
    preds_test = model.predict(X_test)
    if problem_type == "classification":
        metric_name = "f1_score"
        metric_train = f1_score(y_train, preds_train, average="micro")
        metric_test = f1_score(y_test, preds_test, average="micro")
    else:
        metric_name = "r2_score"
        metric_train = r2_score(y_train, preds_train)
        metric_test = r2_score(y_test, preds_test)
    st.write(metric_name + "_train", round(metric_train, 3))
    st.write(metric_name + "_test", round(metric_test, 3))

    if track_with_mlflow:
        mlflow.log_metric(metric_name + "_train", metric_train)
        mlflow.log_metric(metric_name + "_test", metric_test)
        mlflow.end_run()


if __name__ == "__main__":
    main()
