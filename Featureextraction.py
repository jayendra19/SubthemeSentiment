import os 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI


def featureextraction(text):
    prompt=PromptTemplate(
    input_variables=[text],
    template="""
You are an AI Assitance trained to analyze {{text}} Extract any dates, addresses, and names.

Consider this example:

Text:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. John Doe lives at 123 Main St., Anytown, USA. The meeting is scheduled for June 15th, 2023.

Date:
June 15th, 2023

Name:
John Doe

Address:
123 Main St., Anytown, USA

Text:
Mr. Rajesh Kumar lives at Flat No. 301, Shanti Apartments, 12th Main Road, Koramangala, Bengaluru, Karnataka 560034, India. The date is June 15, 2023.

Name: 
Mr. Rajesh Kumar

Address: 
Flat No. 301, Shanti Apartments, 12th Main Road, Koramangala, Bengaluru, Karnataka 560034, India

Date: 
June 15, 2023

Text:
ABC Corporation Pvt. Ltd. is located at 5th Floor, Tower B, Cyber City, Gurgaon, Haryana 122002, India. The date is July 10, 2023.
Name: 
ABC Corporation Pvt. Ltd.

Address: 
5th Floor, Tower B, Cyber City, Gurgaon, Haryana 122002, India

Date: 
July 10, 2023


Now, analyze the following text Identify and extract any dates, addresses, and names from the provided text :

{text}""")
    
    llm=ChatGoogleGenerativeAI(google_api_key=os.environ["GOOGLE_API_KEY"], model="gemini-pro", temperature=0.3)



    chain=LLMChain(llm=llm,prompt=prompt)

    response=chain.run(text)
    print(response)
    

