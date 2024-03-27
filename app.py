import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()


prompt=PromptTemplate(
    input_variables=['text'],
    template="""
You are an AI trained to analyze customer feedback and extract positive and negative aspects from the text. Your task is to identify specific aspects of the service or product that the customer found satisfying (positive) or unsatisfying (negative). 

Consider this example:

Text:
Tires where delivered to the garage of my choice,the garage notified me when they had been delivered. A day and time was arranged with the garage and I went and had them fitted,a Hassel free experience.

    Positive:
    -garage service
    -ease of booking
    
text:
Easy Tyre Selection Process, Competitive Pricing and Excellent Fitting Service.

    Postive:
    -garage service
    -value for money
 
Text:    
Well priced and the lady in the office was brilliant trying to accommodate my requested time for fitting, ATS were also excellent.

    Positive:
    -advisor/agent service
    -value for money
    -garage service
    
Text:    
First time using this service. [REDACTED] changed my appointment three times.   

    Negative:
    -ease of booking
    -change of date  

Now, analyze the following text and extract the positive and negative aspects:

{text}
"""
)



llm=OpenAI(api_key=os.environ["OPEN_API_KEY"],temperature=0.0)



chain=LLMChain(llm=llm,prompt=prompt)

response=chain.run("Brilliant service, brilliant tyres, brilliant prices.Never use anyone else now")
print(response)


''' OUTPUT=
Positive:
- service
- tyres
- prices

Negative:
- none mentioned'''