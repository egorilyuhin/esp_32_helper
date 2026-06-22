from machine import Pin, I2C
import ssd1306_display
import framebuf
import time

# Настройка I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Создание объекта дисплея (128x64, адрес обычно 0x3C)
oled = ssd1306_display.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Очистка экрана
oled.fill(0)

# Вывод текста
oled.text('ESP32', 0, 0)
oled.text('English Display!', 0, 16)
oled.text('Mac OS', 80, 57)

# Показываем на экране
oled.show()