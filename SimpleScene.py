
import mitsuba as mi
import matplotlib.pyplot as plt

# Set the variant of the renderer
mi.set_variant('scalar_rgb')

# Load a scene
print("Load Scene")
scene = mi.load_file("./data/scene.xml")

# Render the scene
print("Render Scene")
img = mi.render(scene, spp=32)
# Write the rendered image to an EXR file

print("Show Image")
plt.axis('off')
# approximate sRGB tonemapping
plt.imshow(img ** (1.0 / 2.2))
plt.show()


print("Done")

