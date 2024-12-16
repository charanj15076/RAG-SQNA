from rouge_score import rouge_scorer

# Reference (large paragraph) from web
reference_text = """
Artificial Intelligence (AI) has rapidly evolved over the past few decades, transforming industries, economies, and 
everyday life. AI technologies, such as machine learning and deep learning, power applications ranging from autonomous 
vehicles, healthcare diagnostics, and personalized marketing to financial forecasting and smart assistants. AI's 
capability to process vast amounts of data at unprecedented speeds allows businesses to gain actionable insights and 
improve decision-making. In healthcare, AI systems analyze medical images, predict patient outcomes, and assist in 
drug discovery. Autonomous vehicles rely on AI for real-time object recognition and navigation. AI-driven automation 
also enhances productivity by handling repetitive tasks, allowing humans to focus on creative and strategic work. 
Despite its benefits, concerns persist regarding job displacement, data privacy, and ethical considerations surrounding 
bias in AI algorithms. Governments and organizations are increasingly working to establish regulations and frameworks 
that ensure AI is used responsibly for societal benefit.
"""

# LLM Predicted Summary # copy pasted here to check its accuracy
predicted_text = """
Artificial Intelligence (AI) has revolutionized industries like healthcare, transportation, and business by automating 
tasks, analyzing large datasets, and improving decision-making. While AI boosts productivity and enables technologies 
like autonomous vehicles and medical diagnostics, it raises concerns about job loss, data privacy, and ethical biases. 
Efforts are ongoing to regulate AI for responsible and beneficial use.
"""

# Initialize ROUGE scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2'], use_stemmer=True)

# Compute ROUGE scores
scores = scorer.score(reference_text, predicted_text)

# Print Results
print("ROUGE-1 Recall:", round(scores['rouge1'].recall, 2))
print("ROUGE-1 Precision:", round(scores['rouge1'].precision, 2))
print("ROUGE-1 F-Score:", round(scores['rouge1'].fmeasure, 2))

print("ROUGE-2 Recall:", round(scores['rouge2'].recall, 2))
print("ROUGE-2 Precision:", round(scores['rouge2'].precision, 2))
print("ROUGE-2 F-Score:", round(scores['rouge2'].fmeasure, 2))