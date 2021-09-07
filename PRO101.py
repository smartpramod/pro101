import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'adli9u0bKNYAAAAAAAAAAWKJ3fbt9Qr7fDVdoHrxDjcKriFZJCZ2teS6JpMRdx3T'
    transferData = TransferData(access_token)

    file_from = input("Enter the file name you want to upload")
    file_to = input("Enter the path name you want to upload to dropbox")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file uploaded")

if __name__ == '__main__':
    main()