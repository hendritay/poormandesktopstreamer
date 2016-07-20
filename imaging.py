import threading
import os
import time
import pyscreenshot as ImageGrab

pathtowww = "c:/xampp/htdocs"

secondsToRefresh = 2
secondsToImage = 3
# setup
index = os.path.join(pathtowww, "index.html")

fileindex = open(index, "w")

fileindex.write('''
<html>



   <body>
     <img id='abc' src=''>
    </body>

    <script type="text/javascript" src="jquery.min.js"></script>

    <script type="text/javascript">
        $(document).ready(function() {
            refreshImage();
            setInterval(refreshImage, %d);
        });

        function refreshImage() {
            $("#abc").attr('src', 'im.png?' + new Date().getTime());
        }

    </script>

</html>
''' % (secondsToRefresh * 1000, ))
fileindex.close()


def hello():

    print 'takePic()'
    ImageGrab.grab_to_file(os.path.join(pathtowww, 'im.png'))

if __name__ == '__main__':


    while True:
        try :
            hello()
        except Exception as ex:
            print ex


        time.sleep(secondsToImage)
