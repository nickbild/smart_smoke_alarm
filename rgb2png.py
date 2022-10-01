from PIL import Image

rgbArray = [[[0,89,156], [0,89,156], [0,89,156], [0,89,156], [0,89,156], [0,89,156], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,89,156], [0,0,139], [0,89,156], [0,0,139], [0,89,156], [0,0,139], [0,89,156], [0,89,156], [0,190,49], ],
[[0,174,148], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,89,156], [0,89,156], ],
[[0,89,156], [0,89,156], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,89,156], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,89,156], [0,0,139], [0,0,139], [0,0,139], [0,89,156], ],
[[0,89,156], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,89,156], ],
[[0,0,139], [0,89,156], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,89,156], ],
[[0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], ],
[[0,89,156], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], ],
[[0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,89,156], ],
[[0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [0,0,139], ],
[[0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], ],
[[0,89,156], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], ],
[[0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], ],
[[0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [0,0,139], ],
[[0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,89,156], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], ],
[[0,89,156], [0,89,156], [0,89,156], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,174,148], [0,174,148], ],
[[0,174,148], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [0,0,139], [74,0,123], [74,0,123], [74,0,123], [0,0,139], [0,0,139], [74,0,123], [0,0,139], [0,0,139], [0,89,156], [0,89,156], [0,174,148], ],
]


newimage = Image.new('RGB', (len(rgbArray[0]), len(rgbArray)))
newimage.putdata([tuple(p) for row in rgbArray for p in row])
newimage.save("ir_cam_output.png")

