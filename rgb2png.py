from PIL import Image

rgbArray = [[[0,194,24], [0,194,24], [0,186,82], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [0,194,24], [0,194,24], [0,194,24], [98,210,0], ],
[[32,202,0], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,178,131], [0,178,131], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [0,194,24], [32,202,0], ],
[[0,194,24], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [32,202,0], ],
[[0,194,24], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,178,131], [0,178,131], [0,178,131], [0,178,131], [0,186,82], [0,178,131], [0,186,82], [0,178,131], [0,186,82], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], ],
[[0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], ],
[[0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,178,131], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], ],
[[0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [0,194,24], [32,202,0], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,194,24], [0,194,24], [0,194,24], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], ],
[[0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,178,131], [0,178,131], [0,178,131], [0,178,131], [0,186,82], [0,194,24], [32,202,0], [98,210,0], [0,194,24], [0,178,131], [0,178,131], [0,186,82], [32,202,0], [32,202,0], [32,202,0], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,178,131], [0,178,131], [0,186,82], ],
[[0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [32,202,0], [230,141,0], [238,72,0], [98,210,0], [0,194,24], [0,178,131], [0,186,82], [230,141,0], [255,0,0], [230,141,0], [172,218,0], [0,194,24], [0,194,24], [32,202,0], [98,210,0], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], ],
[[0,186,82], [0,178,131], [0,178,131], [0,178,131], [0,186,82], [0,178,131], [0,178,131], [0,186,82], [0,186,82], [0,194,24], [230,141,0], [238,72,0], [172,218,0], [0,194,24], [0,178,131], [0,178,131], [230,141,0], [255,0,0], [230,141,0], [172,218,0], [0,194,24], [32,202,0], [222,210,0], [172,218,0], [32,202,0], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], ],
[[0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [32,202,0], [238,72,0], [255,0,0], [230,141,0], [98,210,0], [0,178,131], [0,186,82], [230,141,0], [255,0,0], [238,72,0], [172,218,0], [98,210,0], [222,210,0], [255,0,0], [238,72,0], [98,210,0], [32,202,0], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], ],
[[0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [0,194,24], [32,202,0], [222,210,0], [238,72,0], [230,141,0], [172,218,0], [0,178,131], [0,186,82], [238,72,0], [255,0,0], [230,141,0], [172,218,0], [172,218,0], [222,210,0], [255,0,0], [238,72,0], [98,210,0], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], ],
[[0,194,24], [0,194,24], [0,194,24], [0,194,24], [0,186,82], [0,194,24], [32,202,0], [172,218,0], [230,141,0], [222,210,0], [222,210,0], [238,72,0], [238,72,0], [230,141,0], [0,186,82], [32,202,0], [255,0,0], [255,0,0], [230,141,0], [172,218,0], [222,210,0], [238,72,0], [255,0,0], [230,141,0], [32,202,0], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], ],
[[0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [98,210,0], [222,210,0], [230,141,0], [222,210,0], [172,218,0], [230,141,0], [255,0,0], [238,72,0], [32,202,0], [98,210,0], [255,0,0], [255,0,0], [230,141,0], [172,218,0], [230,141,0], [238,72,0], [230,141,0], [222,210,0], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,178,131], [0,186,82], [0,186,82], ],
[[0,194,24], [0,194,24], [0,194,24], [0,194,24], [0,194,24], [0,194,24], [230,141,0], [238,72,0], [230,141,0], [172,218,0], [172,218,0], [230,141,0], [255,0,0], [255,0,0], [172,218,0], [222,210,0], [255,0,0], [255,0,0], [238,72,0], [238,72,0], [255,0,0], [255,0,0], [230,141,0], [172,218,0], [0,194,24], [0,194,24], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], ],
[[0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,194,24], [32,202,0], [230,141,0], [238,72,0], [222,210,0], [98,210,0], [98,210,0], [222,210,0], [255,0,0], [255,0,0], [222,210,0], [230,141,0], [255,0,0], [255,0,0], [238,72,0], [238,72,0], [255,0,0], [255,0,0], [222,210,0], [98,210,0], [0,194,24], [0,186,82], [0,178,131], [0,186,82], [0,186,82], [0,186,82], [0,186,82], [0,186,82], ],
[[0,194,24], [0,194,24], [0,194,24], [0,194,24], [98,210,0], [222,210,0], [255,0,0], [238,72,0], [98,210,0], [32,202,0], [98,210,0], [222,210,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [172,218,0], [32,202,0], [0,194,24], [0,194,24], [0,194,24], [32,202,0], [0,194,24], [0,194,24], [0,186,82], [0,186,82], ],
[[0,194,24], [0,194,24], [0,194,24], [0,194,24], [172,218,0], [222,210,0], [238,72,0], [238,72,0], [98,210,0], [32,202,0], [98,210,0], [222,210,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [238,72,0], [98,210,0], [32,202,0], [0,194,24], [32,202,0], [172,218,0], [172,218,0], [32,202,0], [0,194,24], [0,186,82], [0,194,24], ],
[[32,202,0], [32,202,0], [98,210,0], [98,210,0], [238,72,0], [255,0,0], [255,0,0], [255,0,0], [238,72,0], [238,72,0], [238,72,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [230,141,0], [32,202,0], [32,202,0], [172,218,0], [222,210,0], [238,72,0], [230,141,0], [32,202,0], [32,202,0], [32,202,0], [0,194,24], ],
[[0,194,24], [0,194,24], [32,202,0], [98,210,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [238,72,0], [238,72,0], [238,72,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [238,72,0], [222,210,0], [32,202,0], [32,202,0], [222,210,0], [230,141,0], [238,72,0], [222,210,0], [32,202,0], [0,194,24], [0,186,82], [0,194,24], ],
[[32,202,0], [32,202,0], [172,218,0], [222,210,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [222,210,0], [172,218,0], [222,210,0], [222,210,0], [238,72,0], [238,72,0], [230,141,0], [172,218,0], [32,202,0], [32,202,0], [0,194,24], [32,202,0], ],
[[0,194,24], [32,202,0], [32,202,0], [172,218,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [238,72,0], [172,218,0], [172,218,0], [222,210,0], [230,141,0], [238,72,0], [230,141,0], [172,218,0], [98,210,0], [32,202,0], [0,194,24], [0,194,24], [0,194,24], ],
[[172,218,0], [172,218,0], [222,210,0], [222,210,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [238,72,0], [230,141,0], [230,141,0], [255,0,0], [255,0,0], [230,141,0], [172,218,0], [32,202,0], [32,202,0], [0,194,24], [0,194,24], [32,202,0], [32,202,0], ],
[[172,218,0], [172,218,0], [222,210,0], [230,141,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [255,0,0], [238,72,0], [238,72,0], [230,141,0], [238,72,0], [238,72,0], [230,141,0], [172,218,0], [98,210,0], [0,194,24], [0,194,24], [0,194,24], [32,202,0], [32,202,0], [172,218,0], ],
]

newimage = Image.new('RGB', (len(rgbArray[0]), len(rgbArray)))
newimage.putdata([tuple(p) for row in rgbArray for p in row])
newimage.save("ir_cam_output.png")

