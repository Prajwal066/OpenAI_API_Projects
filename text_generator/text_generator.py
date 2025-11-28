from transformers import  pipeline
gpt2_pipelines = pipeline(task = "text-generation",model = "openai-community/gpt2")

#To generate text output with a maimum length of 10 tokens

results = gpt2_pipelines("What if computer",max_new_tokens=10,num_return_sequences=2)

for result in results:
     print(result['generated_text'])