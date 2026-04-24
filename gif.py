import imageio.v3 as iio
filenames = ['catlook.png', 'catconfused.png']
images = []
for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('cat.gif', images, duration = 500, loop = 0)