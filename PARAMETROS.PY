import numpy as np

parametros = {
	'Linear Regression': { 'classifier__fit_intercept':[True, False],
		'classifier__normalize': [True, False]
	},

	'Logistic Regression':{'classifier__Penalty': [11, 12],
		'classifier__C': [0.0001, 0.01, 100],
	},

	'k-neighbors':{'classifier__n_neighbors':[2,4,8,16],
		'classifier__p': [2,3]
	},
	'Random Forest':{'classifier__n_estimators': [120, 300, 500, 800, 1200],
		'classifier__max_depth': [5, 8, 15, 25, 30],
		'classifier__min_samples_split': [1, 2, 5, 10, 15, 100],
		'classifier__min_samples_leaf': [1, 2, 5, 10],
		'classifier__maxfeatres': ['log2', 'sqrt', 'None']
	}
}

