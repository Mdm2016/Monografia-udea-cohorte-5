import os


class Path:
    modelos = os.path.join('output', 'modelos')
    bernulli = os.path.join(modelos, 'BernoulliNB.joblib')
    decision_tree = os.path.join(modelos, 'DecisionTreeClassifier.joblib')
    gaussian = os.path.join(modelos, 'GaussianNB.joblib')
    random_forest = os.path.join(modelos, 'modelo_random_forest.joblib')
    multinomial = os.path.join(modelos, 'MultinomialNB.joblib')
    neural_network = os.path.join(modelos, 'NeuralNetwork.joblib')
    random_forest_classifier = os.path.join(
        modelos, 'RandomForestClassifier.joblib'
    )
