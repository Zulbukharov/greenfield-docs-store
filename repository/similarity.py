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
            Document(page_content='Generate Keystore\nBefore generate keystore, you should export your private key from MetaMask and write it into a local file as plaintext . You need also write your password on the password file which set by the "passwordFile" field in the config file.\n\nAssuming that the current private key hex string is written as plaintext in the file key.txt, the following command can be used to generate a keystore file called key.json:\n\n// generate keystore key.json\ngnfd-cmd create-keystore --privKeyFile key.txt key.json\nAfter the keystore file has been generated, you can delete the private key file which contains the plaintext of private key.', metadata={}),
            Document(page_content='Account Operations\n// transfer to an account in Greenfield\ngnfd-cmd bank transfer --to-address 0xF678C3734F0EcDCC56cDE2df2604AC1f8477D55d --amount 12345\n\n// query the balance of account\ngnfd-cmd bank balance --address 0xF678C3734F0EcDCC56cDE2df2604AC1f8477D55d\n\n// create a payment account\ngnfd-cmd payment create-account\n\n// list payment accounts under owner or a address with optional flag --user \ngnfd-cmd payment ls --owner 0x5a64aCD8DC6Ce41d824638419319409246A9b41A', metadata={}),
            Document(page_content='Storage Provider Operations\nTHis command is used to list the SP and query the information of SP.\n\n// list storage providers\ngnfd-cmd sp ls\n\n// get storage provider info\ngnfd-cmd sp head https://gnfd-testnet-sp-1.nodereal.io\n\n// get quota and storage price of storage provider:\ngnfd-cmd sp get-price https://gnfd-testnet-sp-1.nodereal.io', metadata={}),
            Document(page_content='Bucket Operations\nBefore creating bucket, It is recommended to first run the "sp ls" command to obtain the SP list information of Greenfield, and then select the target SP to which the bucket will be created on.\n\n// create bucket. \n// The targt primary SP address to which the bucket will be created on need to be set by --primarySP flag.\n// If the primary SP has not been not set, the cmd will choose first SP in the SP list which obtain from chain as the primary SP.\ngnfd-cmd bucket create gnfd://gnfd-bucket\n\n// update bucket visibility, charged quota or payment address\n(1) gnfd-cmd bucket update --visibility=public-read gnfd://gnfd-bucket\n(2) gnfd-cmd bucket update --charge-quota 50000 gnfd://gnfd-bucket', metadata={}),
            Document(page_content='Upload/Download Operations\n(1) put Object\n\nThe "object put" command is used to upload a file from local which is less than 2G. The bucket name and object name should be replaced with specific names and the file-path should replace by the file path of local system.\n\ngnfd-cmd object put --content-type "text/xml" --visibility private file-path gnfd://gnfd-bucket/gnfd-object\nif the object name has not been set, the command will use the file name as object name. If you need upload a file to the folder, you need to run "object put" command with "--folder" flag.\n\nThe tool also support create a folder on bucket by "object create-folder" command.\n\ngnfd-cmd object create-folder gnfd://gnfd-bucket/testfolder\n(2) download object\n\nThe "object get" command is used to download an object to local path. This command will return the local file path where the object will be downloaded and the file size after successful execution.\n\ngnfd-cmd object get gnfd://gnfd-bucket/gnfd-object file-path \nThe filepath can be a specific file path, a directory path, or not set at all. If not set, the command will download the content to a file with the same name as the object name in the current directory. If it is set as a directory, the command will download the object file into the directory.', metadata={}),
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
    

    