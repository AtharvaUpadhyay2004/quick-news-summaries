from transformers import pipeline

summarizer = pipeline('summarization', model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")

def summarize_article(text):
    input_length = len(text.split())
    max_length = min(130, int(input_length * 0.8)) 
    min_length = min(30, int(input_length * 0.3))   

    if text:  
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    return "No content available, please try again."
