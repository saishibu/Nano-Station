import time,Adafruit_SSD1306
import Adafruit_GPIO.SPI as SPI

import Image
import ImageDraw
import ImageFont


RST=18
DC=15
SPI_PORT=0
SPI_DEVICE=0

disp= Adafruit_SSD1306.SSD1306_128_32(rst=RST,dc=DC,spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE,max_speed_hz=8000000))

disp.begin()
disp.clear()
disp.display()

width=disp.width
height=disp.height


image =Image.new('1',(width,height))
draw =ImageDraw.Draw(image)

padding=1
shape_width=20
top=padding
bottom=height-padding
x=padding

font = ImageFont.load_default()

draw.text((x,top), 'Hello', font=font,fill=255)
time.sleep(2)
disp.image(image)
disp.display()
