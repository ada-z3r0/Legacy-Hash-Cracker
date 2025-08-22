# dehash.py
# Herramienta para revertir hashes generados por el algoritmo XOR rotacional.

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
            original_char_ord = unxored_char_ord - i
            
            # Asegurarse de que el caracter esté en el rango a-z
            if 97 <= original_char_ord <= 122:
                original_text += chr(original_char_ord)
            else:
                # Si algo sale mal, devuelve un error
                return "Error: Caracter fuera de rango. ¿Clave incorrecta?"

        return original_text

    except Exception as e:
        return f"Error procesando el hash: {e}. Asegúrate de que el formato y la clave son correctos."

if __name__ == "__main__":
    print("--- Legacy Dehasher v1.0 ---")
    
    input_hash = input("Introduce el hash (formato xx-xx-xx-xx): ")
    input_key = input("Introduce la clave XOR (formato 0xXX): ")
    
    flag = dehash(input_hash, input_key)
    
    print("-" * 30)
    print(f"Flag recuperada: {flag}")
