# dehash.py
# Herramienta para revertir hashes generados por el algoritmo XOR rotacional.
# Versión 2.0 - Acepta argumentos desde la línea de comandos.

import sys

def dehash(hashed_string, key):
    """
    Revierte el hash XOR rotacional para encontrar el texto original.
    El formato del hash esperado es 'xx-xx-xx-xx'.
    """
    try:
        # Convierte la clave de hexadecimal (ej. '0x2A') a un entero
        key_int = int(key, 16)
        
        # Divide el hash en sus componentes hexadecimales
        hex_parts = hashed_string.split('-')
        
        # Convierte cada parte del hash de hexadecimal a un entero
        byte_values = [int(part, 16) for part in hex_parts]
        
        original_text = ""
        for i, byte in enumerate(byte_values):
            # 1. Revertir la operación XOR
            unxored_char_ord = byte ^ key_int
            
            # 2. Revertir la rotación
            # El alfabeto es a-z (97 a 122). La rotación es `i` (la posición).
            # Para revertir, restamos i
            original_char_ord = unxored_char_ord - i
            
            # Asegurarse de que el caracter esté en el rango a-z
            # (Usamos lower() para la flag, así que solo comprobamos minúsculas)
            if 97 <= original_char_ord <= 122:
                original_text += chr(original_char_ord)
            else:
                # Si algo sale mal, devuelve un error
                return f"Error: Caracter '{chr(unxored_char_ord)}' fuera de rango. ¿Clave incorrecta?"

        # La flag es la palabra que encontramos, pero en mayúsculas para que sea más impactante.
        return original_text.upper()

    except Exception as e:
        return f"Error procesando el hash: {e}. Asegúrate de que el formato y la clave son correctos."

# --- Bloque principal modificado ---
if __name__ == "__main__":
    # Comprobamos si el usuario ha proporcionado los 2 argumentos necesarios (hash y clave)
    if len(sys.argv) != 3:
        print("--- Legacy Dehasher v2.0 ---")
        print("Error: Número de argumentos incorrecto.")
        print("Uso: python dehash.py <hash> <clave_hex>")
        print("Ejemplo: python dehash.py 15-0b-11-1a-0e 0x2A")
        sys.exit(1) # Salir del script con un código de error
    
    # Asignar los argumentos a las variables
    input_hash = sys.argv[1]
    input_key = sys.argv[2]
    
    # Llamar a la función con los argumentos
    flag = dehash(input_hash, input_key)
    
    print("-" * 30)
    print(f"Flag recuperada: {flag}")
