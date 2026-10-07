# Eliminación de ruido con filtro Mediano
# Oscar Flores NC 1389
import cv2

# Cargar la imagen
imagen = cv2.imread("imagenes/mapache.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(imagen,5)
# Mostrar imágenes
cv2.imshow("mapache original 1389", imagen)
cv2.imshow("mapache con filtro de mediana 1389", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "resultado/mapache_mediana-1389.jpg",
    imagen_filtrada
) 

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("resultado/mapache_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("Programa realizado por Oscar Flores NC 1389")