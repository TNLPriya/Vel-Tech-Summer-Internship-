# Day 8 - Hyperparameter Tuning Project

Project

Course Dropout Early Warning System

Algorithm Used

XGBoost Classifier

Project Objective

To optimize the Course Dropout Early Warning System using GridSearchCV by tuning XGBoost hyperparameters and comparing model performance before and after optimization.

Baseline Performance

Accuracy Score: 0.7695 (76.95%)

Hyperparameter Tuning

GridSearchCV was implemented to improve model performance by selecting the best hyperparameter combination.

Hyperparameters Tuned

- learning_rate
- max_depth
- n_estimators

Best Parameters

- learning_rate = 0.1
- max_depth = 4
- n_estimators = 100

Tuned Model Performance

Accuracy Score: 0.7695 (76.95%)

Performance Comparison

- Baseline Accuracy: 76.95%
- Tuned Accuracy: 76.95%
- Improvement: Best hyperparameters were successfully identified using GridSearchCV.

Files Included

- "dataset.csv"
- "dropout_model.pkl"
- "label_encoder.pkl"
- "Day8_GridSearchCV.ipynb"
- "README.md"
- Screenshots

Conclusion

GridSearchCV was successfully implemented to optimize the XGBoost model by identifying the best hyperparameters. The model performance was evaluated and organized for GitHub deployment.
