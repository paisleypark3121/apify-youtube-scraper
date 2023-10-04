import os
from dotenv import load_dotenv

from langchain.document_loaders.base import Document
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import ApifyDatasetLoader
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()

# it is necessary to LOAD the dataset associated (in this case a youtube scraper: streamers/youtube-scraper)
# please note that if i want to ask about the views, the page_content must be the views
loader = ApifyDatasetLoader(
    dataset_id=os.environ["dataset_id"],
    dataset_mapping_function=lambda dataset_item: Document(
        page_content=dataset_item["viewCount"], metadata={"source": dataset_item["title"]}
    ),
)

# loader = loader.load()

# from langchain.text_splitter import RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 1200,
#     chunk_overlap  = 200
# )
# docs_chunks = text_splitter.split_documents(loader)

# embeddings = OpenAIEmbeddings()
# persist_directory="chroma_schoolsin_scraper"
# vectordb=Chroma.from_documents(
#         documents=docs_chunks, 
#         embedding=embeddings, 
#         persist_directory=persist_directory)
        
# query = "Which are the videos with the hightest number of views?"
# llm = ChatOpenAI(temperature=0.0)

# qa = RetrievalQA.from_chain_type(
#     llm=llm, 
#     chain_type="refine", 
#     retriever=vectordb.as_retriever()
# )    

# result=qa.run(query)
# print(result)

index = VectorstoreIndexCreator().from_loaders([loader])
query = "Which is the title with the highest number of views?"
result = index.query_with_sources(query)

print(result["answer"])
#print(result["sources"])