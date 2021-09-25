import dropbox

class tranferData:
    def __init__ (self, access_token):
        self.access_token = access_token
    def uploadFile(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(fileFrom,'rb')
        dbx.files_upload(f.read(), fileTo)

def main():
    access_token = 'sl.A5LPnaOZ8X6quAC7CTDTdHVtYAmrJGE-Xo8cIrq2X7_ym2rFswR-eeAJoQUiRqgM2Giv_h_v6MqNJopZyHmmxJ1IILpj_jW4bbmfTi8qLPnsn-SPwS2MupM4nwSnAehmce2MpYc'
    transfer = transferData(access_token)
    fileFrom = input('ENTER THE FILE PATH TO TRANSFER')
    fileTo - input('ENTER THE FULL PATH TO UPLOAD TO DROPBOX')
    transfer.uploadFile(fileFrom, fileTo)
    print("TRANSFER WAS SUCCESFUL")
    
main()