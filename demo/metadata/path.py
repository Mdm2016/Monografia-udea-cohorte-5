import os


class Path:

    modelos = os.path.join('output', 'modelos')

    bernulli = os.path.join(modelos, 'BernoulliNB.pkl')

    decision_tree = os.path.join(modelos, 'DecisionTreeClassifier.pkl')

    gaussian = os.path.join(modelos, 'GaussianNB.pkl')

    random_forest = os.path.join(modelos, 'modelo_random_forest.pkl')

    multinomial = os.path.join(modelos, 'MultinomialNB.pkl')

    neural_network = os.path.join(modelos, 'NeuralNetwork.pkl')
    
    random_forest_classifier = os.path.join(
        modelos, 'RandomForestClassifier.pkl'
    )
