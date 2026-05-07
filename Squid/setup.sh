echo "SQUID - This acronym means something"


# CHECK THAT XERYONS INSTALLED LOCALLY (i havent dont this)
wget https://xeryon.com/download-files/Xeryon%20Python-Matlab%20Library.zip -O lib/Xeryon_libs.zip
# then extract libraries into folder
mkdir -pv lib/Xeryon
unzip lib/Xeryon_libs.zip -d lib/Xeryon
# this can now be called by lib.Xeryon in python

# initialise
conda activate SQUID-3.12-04-26

