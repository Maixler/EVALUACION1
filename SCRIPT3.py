aclNum = int(input("¿Cuál es el número de ACL? "))
if aclNum >= 1 and aclNum <= 99:
    print("Esta es una ACL estándar.")
elif aclNum >=100 and aclNum <= 199:
    print("Esta es una ACL extendida.")
else:
    print("El numero de ACL no corresponde .")
