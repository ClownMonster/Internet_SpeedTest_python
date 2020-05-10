import pyspeedtest
 # server not found can be resolved by specifying your server name

class GetData():
    def __init__(self):

        self.test = pyspeedtest.SpeedTest() 

    def get_ping(self):
        my_ping = self.test.ping()
        print('Ping : ',my_ping)
    
    def get_download_speed(self):
        download_speed = self.test.download()
        print('Download Speed : ',download_speed)

    def get_upload_speed(self):
        upload_speed = self.test.upload()
        print('Download Speed : ',upload_speed)

    def get_threads(self):
        download_threads = self.test.downloadthread
        upload_threads = self.test.uploadthread
        print('Download Threads : ', download_threads)
        print('Upload Threads : ', upload_threads)

    def get_server(self):
        print('Server : ',self.test.host)



# creating object instance
ob = GetData()
ob.get_ping()
ob.get_server()
ob.get_upload_speed()
ob.get_download_speed()
ob.get_threads()
