import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# 1. Load data
df = pd.read_csv('final_cleaned_data.csv')

# 2. Define churn: withdraw or waitlisted means they dropped out
df['churned'] = df['Status Description'].str.lower().isin(['withdraw', 'waitlisted']).astype(int)

# 3. Select features to analyze
features = ['Gender', 'Age_at_Application_Int', 'continent',
            'Institution_Participation_Count', 'days_to_apply', 'Opportunity Category']

# 4. Clean data
df_clean = df.dropna(subset=features + ['churned']).copy()

# 5. Encode categorical features
le_dict = {}
for col in ['Gender', 'continent', 'Opportunity Category']:
    le = LabelEncoder()
    df_clean[col + '_enc'] = le.fit_transform(df_clean[col])

# 6. Prepare data for model
X = df_clean[['Gender_enc', 'Age_at_Application_Int', 'continent_enc',
              'Institution_Participation_Count', 'days_to_apply', 'Opportunity Category_enc']]
y = df_clean['churned']

# Scale the data (important for models like KNN and Logistic Regression)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 7. Train 5 models
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "K-Nearest Neighbors": KNeighborsClassifier()
}

results = []

print("=" * 60)
print("MODEL ACCURACY RESULTS")
print("=" * 60)

for name, model in models.items():
    # Use scaled data for LR and KNN
    if name in ["Logistic Regression", "K-Nearest Neighbors"]:
        model.fit(X_train_s, y_train_s)
        acc = model.score(X_test_s, y_test_s)
    else:
        model.fit(X_train, y_train)
        acc = model.score(X_test, y_test)

    results.append({'Model': name, 'Accuracy': acc})
    print(f"{name:25s} {acc:.4f}")

print("=" * 60)

# Create visualization
results_df = pd.DataFrame(results).sort_values(by='Accuracy', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x='Accuracy', y='Model', data=results_df, palette='Blues_r')
plt.xlim(0.9, 1.0)
plt.title('Which Model Predicts Churn Best?', fontsize=14, fontweight='bold')
plt.xlabel('Accuracy Score', fontsize=12)
plt.ylabel('')
plt.tight_layout()
plt.savefig('churn_model_comparison.png', dpi=300)
print("\n✓ Chart saved as 'churn_model_comparison.png'")