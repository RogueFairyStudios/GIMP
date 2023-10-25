#!/usr/bin/env python

from gimpfu import *
import json


def export_layers_to_json(churubebas, tchurubebas, image, drawable, output_folder):
    gimp.progress_init("Saving to '" + output_folder + "'...")
    layers_info = []

    for i, layer in enumerate(image.layers):
        layer_info = {
            "name": layer.name,
            "x": layer.offsets[0],
            "y": layer.offsets[1],
            "width": layer.width,
            "height": layer.height,
        }
        layers_info.append(layer_info)

        # Save each layer as PNG
        png_filename = output_folder + "\\layer_" + str(i + 1) + ".png"
        pdb.file_png_save(image, layer, png_filename,
                          png_filename, 0, 9, 0, 0, 0, 0, 0)

    json_data = {"layers": layers_info}
    json_file_path = output_folder + "\\file.json"

    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

    gimp.message("Export to: " + output_folder)


register(
    "export_layers_to_json",
    "Export Layer Info to JSON and Create Composition Image",
    "Export layer information to JSON and create a composition image",
    "Rogue Fairy Studios - GIMP Tools",
    "Edward Facundo",
    "21/10/2023",
    "<Image>/Rogue Fairy Plugins/Export Layers to JSON",
    "RGB*, GRAY*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None),
        (PF_DIRNAME, "output_folder", "Output Folder", "")
    ],
    [],
    export_layers_to_json)

main()
