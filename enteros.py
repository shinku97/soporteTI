#entero
5 , 0, 42

#flotante
3.14, 0.0, -2.71



#str
"Hola,mundo!", "python3", "12345"
# ...existing code...
# Ejemplos de conversión de float a str
f = 3.14

s1 = str(f)            # "3.14"
s2 = "{:.2f}".format(f)  # "3.14" con 2 decimales (ejemplo)
s3 = f"{f:.2f}"        # f-string con 2 decimales
s4 = repr(f)           # representación, similar a str para floats

print(s1, s2, s3, s4)

# lista de floats a lista de strings
floats = [3.14, 0.0, -2.71]
strs = list(map(str, floats))        # ['3.14', '0.0', '-2.71']
csv = ",".join(map(str, floats))     # "3.14,0.0,-2.71"
print(strs, csv)