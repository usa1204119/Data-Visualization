import pygal.maps.world 
wm = pygal.maps.world.World()
wm.title = 'North America Census 2010'
wm.add('North America',{'ca':34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_america.svg')