# Get cleaner DS slides :)

This script was quickly written as an ad hoc solution to the repetitive DS slides, so don't judge it.

To use it, do the following:

1. Create some folder where the script and the slides will be.
2. Download the code.
a) Click on the green "Code" button and choose "Download ZIP".
b) Extract the file script.py from the downloaded ZIP file, and copy it into the folder you created above.
3. Download the DS slides from Moodle and copy them into the same folder from the previous step.
4. Rename the slides to "folien.pdf". (this is because the code is bad and I hard-coded the name of the file)
5. Get a linux environment, either WSL, Ubuntu, or whatever you want, and open the terminal in the folder from above.
6. Make sure to have python3, pip and PyMuPDF installed.
  a) Run "sudo apt install python3" to install python3.
  b) Run "sudo apt install python3-pip" to install pip.
  c) Run "pip install PyMuPDF" to install PyMuPDF.
7. Everything should be ready. Run "python3 script.py" to execute the script.
8. Now you should find a file named "output.pdf" in the same folder, with all duplicate slides removed :)


Disclaimers:

1. Don't judge the code, it may be ugly and small, but it has a good personality.
2. If, at any point during the installations, you get any errors, google them, I'm sure you'll find the answers.
3. Try doing it yourself. I just read the documentation for a while and came up with something which will make my life better. That's the fun in programming.
4. Have a good semester :)
