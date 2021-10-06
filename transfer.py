import dropbox
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
           dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
           

def main():
    access_token = "-G7rs_0ftzsAAAAAAAAAAVOGAInkPXEVlvJDr6XAuBlZ2fE4TGKFW2Xxpvc4Dc25"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
     
    file_to = input("enter the full path to upload to dropbox:- ")
    # API v2
    transferData.upload_file(file_from, file_to)
    print("File Uploaded !!!")


main()