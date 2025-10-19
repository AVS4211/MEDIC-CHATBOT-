from setuptools import find_packages, setup

setup(
    name="medic-chatbot",
    version="0.1.0",
    packages=find_packages(),
    author="Avs Narayana",
    author_email="avsn1122@gmail.com",
    install_requires=[
        "langchain==0.3.26",
        "flask==3.1.1",
        "sentence-transformers==4.1.0",
        "pypdf==5.6.1",
        "python-dotenv==1.1.0",
        "langchain-pinecone==0.2.8",
        "langchain-openai==0.3.26",
        "langchain-community==0.3.26",
    ],
)