from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

def text_on_images(price_58k, tweet_image):

        # prepare to write the first line
        font_size = 80
        rotate_angle = 0
        paste_x_position = 265
        paste_y_position = 300

        tweet_image = Image.open(tweet_image)
        font = ImageFont.truetype("Silom.ttf",font_size)
        
        # Creating a temporary canvas, drawing the title line in it
        temporary_canvas = Image.new(mode='L', size=(1080,1080))
        text_on_temporary_canvas = ImageDraw.Draw(temporary_canvas)
        text_on_temporary_canvas.text((0, 0), "The current".upper(), font=font, fill=255)
        text_on_temporary_canvas.text((0, 80), "price of".upper(), font=font, fill=255)
        text_on_temporary_canvas.text((0, 160), "bitcoin is".upper(), font=font, fill=255)
        # rotated_text_on_temporary_canvas=temporary_canvas.rotate(rotate_angle, resample=3, expand=1)

        # pasting temporary canvas on main image
        # tweet_image.paste( ImageOps.colorize(rotated_text_on_temporary_canvas, (0,0,0), (242,169,0)), (paste_x_position,paste_y_position), rotated_text_on_temporary_canvas)

        # tweet_image.show()
        # tweet_image.save("58k_bot_with_text.png")

        # prepping to write the price of bitcoin
        # font_size = 80
        # rotate_angle = 0
        # paste_x_position = 265
        # paste_y_position = 700

        # tweet_image = Image.open("58k_bot_with_text.png")
        
        # Creating a temporary canvas, drawing the first line on it
        # temporary_canvas = Image.new(mode='L', size=(1080,1080))
        # text_on_temporary_canvas = ImageDraw.Draw(temporary_canvas)
        text_on_temporary_canvas.text((0, 320), price_58k, font=font, fill=255, align="center")
        # rotated_text_on_temporary_canvas=temporary_canvas.rotate(rotate_angle, resample=3, expand=1)

        # pasting temporary canvas on main image
        rotated_text_on_temporary_canvas=temporary_canvas.rotate(rotate_angle, resample=3, expand=1)
        tweet_image.paste( ImageOps.colorize(rotated_text_on_temporary_canvas, (0,0,0), (242,169,0)), (paste_x_position,paste_y_position), rotated_text_on_temporary_canvas)

        # tweet_image.show()
        tweet_image.save("58k_bot_with_text.png")

        return tweet_image

# if __name__ == "__main__":
#     image_draw_angled(5002, "assets/blank_belly_dark_mode/6.jpg")