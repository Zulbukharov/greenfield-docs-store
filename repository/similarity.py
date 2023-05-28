from typing import List

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document

from config import CONFIGURATION

DOCSEARCH_DIRECTORY = "docsearch"

class DocumentStoreRepository:
    vectordb: Chroma

    def __init__(self):
        embedding = OpenAIEmbeddings(openai_api_key=CONFIGURATION.open_api_key)
        self.vectordb = Chroma(persist_directory=DOCSEARCH_DIRECTORY, embedding_function=embedding)

    def similarity_search(self, query, limit=4) -> List[Document]:
        return self.vectordb.similarity_search(query, limit=limit)
    
class CommandStoreRepository:
    def __init__(self):
        pass

    def similarity_search(self, query, limit=4) -> List[Document]:
        documents: List[Document] = [
            Document(page_content='Group Operations\nThe group commands is used to create group, update group members, delete group and query group info.\n\n// create group\ngnfd-cmd group create gnfd://groupname\n\n// update group member\ngnfd-cmd group update --add-members 0xca807A58caF20B6a4E3eDa3531788179E5bc816b gnfd://groupname\n\n// head group member\ngnfd-cmd group head-member --head-member 0xca807A58caF20B6a4E3eDa3531788179E5bc816b gnfd://groupname\n\n// delete group\ngnfd-cmd group delete gnfd://group-name', metadata={}),
            Document(page_content='Policy Operations\n// The object policy action can be "create", "delete", "copy", "get" , "execute", "list" or "all".\n// The bucket policy actions can be "update", "delete", "create", "list", "update", "getObj", "createObj" and so on.\n// The actions info can be set with combined string like "create,delete" by --actions\n// The policy effect can set to be allow or deny by --effect\n\n// grant object operation permissions to a group\ngnfd-cmd policy put-object-policy --group-id 128  --actions get,delete  gnfd://gnfd-bucket/gnfd-object\n\n// grant object operation permissions to an account\ngnfd-cmd policy put-object-policy --grantee 0x169321fC04A12c16...  --actions get,delete gnfd://gnfd-bucket/gnfd-object\n\n// grant bucket operation permissions to a group\ngnfd-cmd policy put-bucket-policy --group-id 130 --actions delete,update,createObj  gnfd://gnfd-bucket\n\n// grant bucket operation permissions to an account\ngnfd-cmd policy put-bucket-policy  --grantee 0x169321fC04A12c16...  --actions delete,update  gnfd://gnfd-bucket', metadata={}),
            Document(page_content='List Operations\n// list buckets\ngnfd-cmd bucket ls\n\n// list objects\ngnfd-cmd object ls gnfd://gnfd-bucket', metadata={}),
            Document(page_content='Delete Operations\n// delete bucekt\ngnfd-cmd bucket delete gnfd://gnfd-bucket\n\n//delete object\ngnfd-cmd object delete gnfd://gnfd-bucket/gnfd-object', metadata={}),
            Document(page_content='Head Operations\n// head bucekt\ngnfd-cmd bucket head gnfd://gnfd-bucket\n\n// head object\ngnfd-cmd object head gnfd://gnfd-bucket/gnfd-object\n\n// head Group\ngnfd-cmd group head gnfd://groupname', metadata={}),
            Document(page_content="Payment Operations\n// get quota info\ngnfd-cmd payment quota-info gnfd://gnfd-bucket\n\n// buy quota\ngnfd-cmd payment buy-quota --charged-quota 1000000 gnfd://gnfd-bucket\n\n// deposit from owner's account to the payment account \ngnfd-cmd payment deposit --to-address 0xF678C3734F0EcDCC56cDE2df2604AC1f8477D55d --amount 12345\n\n// witharaw from a payment account to owner's account\ngnfd-cmd payment withdraw --from-address 0xF678C3734F0EcDCC56cDE2df2604AC1f8477D55d --amount 12345", metadata={}),
            Document(page_content='Hash Operations\n// compute integrity hash\ngnfd-cmd object get-hash file-path', metadata={}),
            Document(page_content='Crosschain Operations\n// crosschain transfer some tokens to an account in BSC\ngnfd-cmd crosschain transfer-out --to-address "0x2eDD53b48726a887c98aDAb97e0a8600f855570d" --amount 12345\n\n// mirror a group to BSC\ngnfd-cmd crosschain mirror --resource group --id 1\n\n// mirror a bucket to BSC\ngnfd-cmd crosschain mirror --resource bucket --id 1\n\n// mirror a object to BSC\ngnfd-cmd crosschain mirror --resource object --id 1', metadata={}),
        ] 
        return documents
    

    