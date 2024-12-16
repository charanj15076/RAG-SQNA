
import pandas as pd
from rouge_score import rouge_scorer

# Sample outputs and references (replace these with actual data)
data = {
    "Modality": ["Text (Local Model)", "Audio (Hugging Face)", "Image (Hugging Face)", "RAG (AWS Bedrock)"],
    "Predictions": [
        "This is the text model output.", # copy paste outputs of each modalities
        "This is the audio output summary.",
        "This is the image summary output.", # has a reference model for results comparison 
        "This is the RAG-based model output."
    ],
    "References": [
        "This is the expected text output.",
        "This is the expected audio summary.",
        "This is the correct image summary.",
        "This is the correct RAG-based summary."
    ]
}


# Initialize ROUGE scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2'], use_stemmer=True)

# Initialize results storage
results = []

# Compute ROUGE scores
for i in range(len(data["Modality"])):
    modality = data["Modality"][i]
    prediction = data["Predictions"][i]
    reference = data["References"][i]
    
    scores = scorer.score(reference, prediction)
    
    rouge1 = scores['rouge1']
    rouge2 = scores['rouge2']
    
    results.append({
        "Modality": modality,
        "ROUGE-1 Recall": round(rouge1.recall, 2),
        "ROUGE-1 Precision": round(rouge1.precision, 2),
        "ROUGE-1 F-Score": round(rouge1.fmeasure, 2),
        "ROUGE-2 Recall": round(rouge2.recall, 2),
        "ROUGE-2 Precision": round(rouge2.precision, 2),
        "ROUGE-2 F-Score": round(rouge2.fmeasure, 2),
    })

# Create a DataFrame
df = pd.DataFrame(results)

# Display and save results
print(df)
df.to_csv("rouge_scores.csv", index=False)
print("Results saved")
