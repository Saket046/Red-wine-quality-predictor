### Project Title: **Red Wine Quality Prediction and Deployment**  

#### **Data Collection**  
- Sourced dataset from Kaggle: [Red Wine Quality Dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009).  
- Dataset contains 1,599 rows, 11 input features (e.g., fixed acidity, pH, alcohol) and 1 target variable (quality).  

#### **Exploratory Data Analysis (EDA) and Data Preparation**  
1. **Data Formatting:** Verified column data types and statistical descriptions using `.describe()`.  
2. **Missing Values:** Found no missing data, requiring no imputation or removal.  
3. **Duplicates:** Identified and removed 240 duplicate rows, retaining only the first occurrence.  
4. **Outlier Handling:** Used Interquartile Range (IQR) to detect and remove outliers with custom functions.

#### **Feature Engineering**  
1. **Feature Selection:**  
   - Created a correlation matrix and heatmap to analyze relationships between features.  
   - Dropped low-impact features ('pH', 'fixed acidity', 'citric acid', 'free sulfur dioxide') based on their correlation with the target variable.  
2. **Feature Scaling:** Applied MinMaxScaler to standardize data, enabling effective performance for Euclidean distance-based models.  
3. **Target Encoding:** Binarized wine quality scores (Good: >7, Bad: ≤7).  

#### **Data Balancing**  
- Addressed class imbalance (125 "Good" vs. 860 "Bad") using SMOTE (Synthetic Minority Oversampling Technique) to ensure balanced training data.  

#### **Model Development and Evaluation**  
1. **Train-Test Split:** Divided data into 80% training and 20% testing sets.  
2. **Model Selection:** Compared five classifiers using accuracy scores:  
   - Random Forest (93.8%)
   - XGBoost (94.4%)
   - K-Nearest Neighbors (94.7%)
   - Decision Tree (90.1%)
   - SGD Classifier (84.6%)
   - Selected **XGBoost** as the best performer through 10-fold cross-validation with a mean accuracy of 92.8%.
 
3. **Hyperparameter Tuning:** Optimized parameters (learning_rate, max_depth, min_child_weight, gamma) using RandomizedSearchCV and GridSearchCV for peak performance.  

4. **Performance Metrics:**
   - Precision: 0.91
   - Recall: 0.95
   - F1 Score: 0.93
   - Test Accuracy: 94.5%
   - Confusion Matrix:
     ```
     [619  66]  
     [ 32 659]
     ```

#### **Model Deployment**  
1. **Model Pickling:** Saved the trained model as a pickle file and verified functionality with dummy scaled inputs.  
2. **Flask Web Application:**  
   - Developed a user-friendly webpage with a form for inputting wine parameters.
   - Validated inputs using Python's `try` and `except` for error handling.
   - Scaled user inputs and fed them into the model to predict wine quality (Good/Bad).
   - Displayed prediction results with a help table for parameter guidance and contact information.

3. **Deployment on Heroku:**  
   - Created `requirements.txt` and `Procfile` for dependency management and app configuration.
   - Uploaded codebase to GitHub and deployed the app on Heroku, enabling public accessibility.

#### **Impact**  
This project automates wine quality prediction, providing accurate and efficient insights for quality assurance. It integrates advanced machine learning with a user-friendly interface, showcasing end-to-end machine learning project deployment.
