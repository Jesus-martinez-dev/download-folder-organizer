import os
import shutil

ORIGEN = os.path.expanduser('~/Descargas')

CATEGORIAS = {
    'imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp', '.tiff'],
    'documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.csv', '.odt', '.pptx', '.rtf'],
    'archivos': ['.zip', '.rar', '.7z', '.tar.gz', '.tar', '.gz', '.bz2'],
    'instaladores': ['.deb', '.exe', '.msi', '.dmg', '.pkg'],
    'multimedia': ['.mp3', '.mp4', '.avi', '.mkv', '.mov', '.wav', '.flac']
}

def organizar_descargas():
    if not os.path.exists(ORIGEN):
        print(f"Error: No existe la carpeta {ORIGEN}")
        return

    mapa_extensiones = {}
    for categoria, extensiones in CATEGORIAS.items():
        for extension in extensiones:
            mapa_extensiones[extension] = categoria

    print(f"Organizando: {ORIGEN}")
    exitos = 0
    errores = 0

    for elemento in os.listdir(ORIGEN):
        ruta_completa = os.path.join(ORIGEN, elemento)

        if os.path.isdir(ruta_completa):
            continue

        nombre, extension = os.path.splitext(elemento)
        extension = extension.lower()

        categoria = mapa_extensiones.get(extension)

        if not categoria:
            continue

        carpeta_destino = os.path.join(ORIGEN, categoria)
        os.makedirs(carpeta_destino, exist_ok=True)

        archivo_destino = os.path.join(carpeta_destino, elemento)

        if os.path.exists(archivo_destino):
            contador = 1
            while os.path.exists(archivo_destino):
                nuevo_nombre = f"{nombre}_{contador}{extension}"
                archivo_destino = os.path.join(carpeta_destino, nuevo_nombre)
                contador += 1

        try:
            shutil.move(ruta_completa, archivo_destino)
            print(f"✓ {elemento} → {categoria}/")
            exitos += 1
        except PermissionError:
            print(f"✗ Sin permisos: {elemento}")
            errores += 1
        except Exception as error:
            print(f"✗ Error con {elemento}: {error}")
            errores += 1

    print(f"\nCompletado: {exitos} archivos organizados, {errores} errores")

if __name__ == "__main__":
    organizar_descargas()