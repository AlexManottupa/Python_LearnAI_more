import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# Cargar el archivo GeoJSON o Shapefile que contiene los datos catastrales de Cusco
gdf = gpd.read_file('cusco_catastral.geojson')

# Configurar el sistema de coordenadas para estar en el formato adecuado (usualmente EPSG:4326)
gdf = gdf.to_crs(epsg=3857)

# Crear el mapa con matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, alpha=0.5, edgecolor='k')

# Añadir un fondo de mapa usando contextily
ctx.add_basemap(ax, source=ctx.providers.Stamen.Terrain)

# Mostrar el plano catastral
plt.title("Plano Catastral de la Ciudad del Cusco")
plt.show()
