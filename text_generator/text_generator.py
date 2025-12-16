from transformers import  pipeline 

print("Loading model......")

gpt2_pipelines = pipeline(task = "text-generation",model = "openai-community/gpt2")

#To generate text output with a maimum length of 10 tokens

results = gpt2_pipelines("What if computer",max_new_tokens=10,num_return_sequences=2,do_sample=True,
                                              temperature=0.8,
                                              top_p=0.9,
                                             repetition_penalty=1.1)

for result in results:
     print(result['generated_text'])