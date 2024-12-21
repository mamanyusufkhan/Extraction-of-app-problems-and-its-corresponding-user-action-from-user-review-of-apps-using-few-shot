import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('Evaluation_data.csv')

# Filter the dataframe to include only reviews with score = 1
df_score_1 = df[df['score'] == 1]

# Extract the content column
content_column = df_score_1['content']

# Randomly select 100 reviews with score = 1
random_reviews_score_1 = content_column.sample(n=200, random_state=42)  # Use random_state for reproducibility

# Filter the dataframe to include only reviews with score > 1

# Create a new dataframe with the selected reviews
selected_reviews_df = pd.DataFrame(random_reviews_score_1, columns=['content'])

# Save the selected reviews to a new CSV file
selected_reviews_df.to_csv('selected_reviews.csv', index=False)