import mitsuba as mi
import matplotlib.pyplot as plt

# Set the variant of the renderer
mi.set_variant('scalar_rgb')

# Load a scene
print("Load Scene")
cornell_box = mi.cornell_box()
# print(cornell_box)
scene = mi.load_dict(cornell_box)

# Render the scene
print("Render Scene")
img = mi.render(scene, spp=512)
# Write the rendered image to an EXR file

print("Show Image")
plt.axis('off')
# approximate sRGB tonemapping
plt.imshow(img ** (1.0 / 2.2))
plt.show()

print("Save Image")
mi.Bitmap(img).write('cornell_box.exr')

print("Done")
