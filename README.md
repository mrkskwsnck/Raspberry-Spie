Raspberry-Spie
==============

Web application to provide a video stream by the Raspberry Pi's official camera module.


Hardware requirements
---------------------

* Raspberry Pi with camera interface (CSI)
* [Camera Module](https://www.raspberrypi.org/products/camera-module/)


Software requirements
---------------------

* Raspbian Jessie
* Python 3

Install prerequisites:

    $ sudo apt update
    $ sudo apt install git python3 python3-picamera


Getting started
---------------

Clone the project's repository and change to its directory:

    $ git clone https://github.com/MrksKwsnck/Raspberry-Spie.git
    $ cd Raspberry-Spie

Start the application server by running the following command:

    $ python3 -m http.server --cgi 8000

That way the server is listening on the default port 8000 (adjust the port number for your needs) for incoming requests.

Now the application can be accessed using your favourite web browser by visiting the URL scheme [http://localhost:8000/](http://localhost:8000/) or replace localhost with the IP address of your Raspberry Pi (e.g. for watching the stream from another computer on the network).

To shutdown the server again pass the SIGINT signal to interrupt it or simply press Ctrl+C in the terminal window running the application.
