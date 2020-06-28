# OCR-PyTesseract
This Repository contains a basic OCR created using Pytesseract and Opencv2 libraries for python.

    BasicOCR.py has the code.
    test.png and test1.png are images used to test the code.
    testresult.PNG is the result obtained after using image test.png


Topic: Create a Basic OCR using Pytesseract and OpenCV2 in Python.

To Do: Extract Text and/or data from the image(s).

Link to my GitHub Repository: https://github.com/eternaldemon/OCR-PyTesseract

    Programming Language Used: Python 3.7

    Software/Editor Used: Spyder 4.1.0 on Anaconda Navigator

    Libraries used : Pytesseract and opencv-python
    

    How to Install OpenCV-Python in Windows:
    1.Open cmd(command prompt) as administrator from windows search taskbar located on left bottom of screen. Or press CTRL + R, type cmd.exe and press Enter.

    2.Type the following: pip install opencv-python.Wait for it to finish and opencv2 has been installed for python.
       
Note: If any error occurs it is mostly due to cmd not being open with administrative rights.



    How to install and set-up PyTesseract in Windows:
    1.Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
    2.Choose the installer out of 32 and 64 bit according to your system. To check you PC type, type System Info in Windows search bar and press Enter. Find System Type of the       page and download accordingly.
    3.During Installation, check in which directory it was installed and add that directory to the path variable under the Environment variables.
    4.Now, open cmd with administrative privileges, type pip install pytesseract and press enter. PyTesseract shall be installed shortly.
    5.Hopefully, any code using the pytesseract library after importing it will run. But if it still doesn't run then after importing the library put the following line in the code file.
      pytesseract.pytesseract.tesseract_cmd = r'PATH TO tesseract.exe installed from step 1'
      Example:
      pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

