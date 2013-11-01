from PIL import Image
from PIL import ImageColor

def gen_mem_usage_image(chunk_iter, start, end, step, height=512):
    width = (end - start - 1) / step / height+ 1
    im = Image.new('RGB', (width, height), 'WHITE')
    red = ImageColor.getcolor('RED', 'RGB')
    green = ImageColor.getcolor('GREEN', 'RGB')

    for chunk in chunk_iter:
        chunk_start = chunk.as_address()
        chunk_end = chunk_start + chunk.chunksize()
        for p in xrange(chunk_start, chunk_end, step):
            x, y = p / step / height, p / step % height
            if chunk.is_in_use():
                im.putpixel((x, y), red)
            else:
                im.putpixel((x, y), green)

    return im





